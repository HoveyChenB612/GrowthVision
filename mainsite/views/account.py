import json

from django.shortcuts import render, HttpResponse, redirect
from mainsite import models
from django.utils import timezone
from django.http import JsonResponse
from mainsite.models import DataDouYin, User, PlatFormDouYin
from mainsite.utils.pagination import Pagination
from mainsite.utils.get_douyin_data import get_douyin_data
from datetime import datetime


def account_auth(request):
	"""账号授权"""

	# 获取当前登陆的用户uid
	data_dict = {"uid": request.session.get("info").get("uid")}

	# 搜索
	search_data = request.GET.get("keyword", "")
	if search_data:
		data_dict["nickname__contains"] = search_data

	queryset = models.PlatFormDouYin.objects.filter(**data_dict)

	# 分页
	page_object = Pagination(request, queryset, page_size=10)

	context = {
		"queryset": page_object.page_queryset,  # 分完页的数据
		"page_string": page_object.html(),  # 生成页码
		"now": timezone.now(),  # 当前时间
		"search_data": search_data,  # 搜索参数
	}

	return render(request, "account_auth.html", context)


def account_delete(request, oid):
	"""删除账号"""

	models.PlatFormDouYin.objects.filter(open_id=oid).delete()

	return redirect(f"/account/auth/")


def account_data(request):
	"""数据展示"""

	return render(request, "account_data.html")


def account_data_get(request):
	"""获取表格数据"""

	# 获取当前登陆的用户uid
	data_dict = {"uid": request.session.get("info").get("uid")}

	queryset = models.DataDouYin.objects.select_related('open_id').values(
		'open_id__nickname',
		'open_id__avatar',
		'item_id',
		'title',
		'video_status',
		'create_time',
		'media_type',
		'cover',
		'is_top',
		'share_url',
		'comment_count',
		'digg_count',
		'download_count',
		'forward_count',
		'play_count',
		'share_count'
	)

	data = {
		"total": 0,
		"rows": []
	}

	for index, item in enumerate(queryset):
		data["total"] += index
		content = {
			"id": index + 1,
			"nickname": item["open_id__nickname"],
			"title": item["title"],
			"digg_count": item["digg_count"],
			"comment_count": item["comment_count"],
			"download_count": item["download_count"],
			"play_count": item["play_count"],
			"forward_count": item["forward_count"],
			"share_count": item["share_count"],
			"share_url": item["share_url"]
		}
		data["rows"].append(content)

	return JsonResponse(data)


def account_data_update(request):
	"""更新数据"""
	# 通过Ajax更新列表，上传到数据库中，将时间格式改一下

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	platform_queryset = models.PlatFormDouYin.objects.filter(uid=uid)
	for queryset in platform_queryset:
		open_id = queryset.open_id
		access_token = queryset.access_token
		data = get_douyin_data(open_id, access_token)
		sql_item_id_list: list[tuple] = list(
			models.DataDouYin.objects.values_list("item_id"))  # [("item_id",),("item_id",)]
		sql_item_id_list = [i[0] for i in sql_item_id_list]  # ["item_id"]

		for item in data["VideoList"]:
			# 不公开的作品取不到media_type的值，默认指定4
			media_type = item.get("media_type", 4)
			# 格式化时间
			create_time = datetime.fromtimestamp(int(item["create_time"]))
			if item["item_id"] in sql_item_id_list:
				update_data = {
					"title": item["title"],
					"video_status": item["video_status"],
					"create_time": create_time,
					"media_type": media_type,
					"cover": item["cover"],
					"is_top": item["is_top"],
					"share_url": item["share_url"],
					"comment_count": item["statistics"]["comment_count"],
					"digg_count": item["statistics"]["digg_count"],
					"download_count": item["statistics"]["download_count"],
					"forward_count": item["statistics"]["forward_count"],
					"play_count": item["statistics"]["play_count"],
					"share_count": item["statistics"]["share_count"]
				}
				models.DataDouYin.objects.filter(item_id=item["item_id"]).update(**update_data)
			else:
				create_data = {
					"item_id": item["item_id"],
					"open_id": PlatFormDouYin.objects.get(open_id=open_id),
					"uid": User.objects.get(uid=uid),
					"title": item["title"],
					"video_status": item["video_status"],
					"create_time": create_time,
					"media_type": media_type,
					"cover": item["cover"],
					"is_top": item["is_top"],
					"share_url": item["share_url"],
					"comment_count": item["statistics"]["comment_count"],
					"digg_count": item["statistics"]["digg_count"],
					"download_count": item["statistics"]["download_count"],
					"forward_count": item["statistics"]["forward_count"],
					"play_count": item["statistics"]["play_count"],
					"share_count": item["statistics"]["share_count"]
				}

				models.DataDouYin.objects.create(**create_data)

		return JsonResponse({"status": True})

	return JsonResponse({"status": False})
