from datetime import datetime, timedelta
from urllib import parse

import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q

from mainsite import models
from mainsite.utils.get_douyin_data import get_douyin_data


def account_auth_list(request):
	"""账号授权列表"""

	# 前端选中标签与头部标签
	active_account_auth = ""
	header_label = ""
	if request.path == "/account/auth/list/":
		active_account_auth = "active"
		header_label = "授权管理"

	# 抖音授权
	client_key = "awpswfd65m22r59e"  # 应用唯一标识
	response_type = "code"  # 默认值 code
	scope = "user_info,data.external.user,video.list.bind,video.data.bind,renew_refresh_token,data.external.item,data.external.billboard_hot_video"  # 应用授权作用域
	# optionalScope = "user_info,1,data.external.user,1"  # 应用授权可选作用域&optionalScope={optionalScope}
	redirect_uri = "https://www.baidu.com"  # 授权成功后的回调地址
	get_accredit_url = f"https://open.douyin.com/platform/oauth/connect?client_key={client_key}&response_type={response_type}&scope={scope}&redirect_uri={redirect_uri}"

	context = {
		"now": timezone.now(),  # 当前时间
		"get_accredit_url": get_accredit_url,  # 抖音授权地址
		"active_account_auth": active_account_auth,
		"header_label": header_label
	}

	return render(request, "account_auth_list.html", context)


def account_auth_zhihu(request):
	"""账号授权知乎"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")

	if request.method == "POST":
		z_c0 = request.POST.get("z_c0")
		cookies = {"z_c0": z_c0}
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
		url = "https://www.zhihu.com/api/v4/me"
		response = requests.get(url, headers=headers, cookies=cookies)
		user_info = response.json()
		nickname = user_info.get("name")
		avatar = user_info.get("avatar_url")
		auth_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		expires_time = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d %H:%M:%S")
		zh_uid = user_info.get("id")

		user_info_dict = {
			"uid_id": uid,
			"nickname": nickname,
			"avatar": avatar,
			"auth_time": auth_time,
			"expires_time": expires_time,
			"z_c0": z_c0
		}
		exists = models.PlatFormZhiHu.objects.filter(zh_uid=zh_uid).exists()
		if exists:
			models.PlatFormZhiHu.objects.filter(zh_uid=zh_uid).update(**user_info_dict)
		else:
			user_info_dict["zh_uid"] = zh_uid
			models.PlatFormZhiHu.objects.create(**user_info_dict)

	return redirect("/account/auth/list/")


def account_auth_douyin(request):
	"""账号授权抖音"""

	# 获取当前登陆的用户uid
	data_dict = {"uid": request.session.get("info").get("uid")}

	# 获取用户授权信息
	if request.method == "POST":
		# 获取扫码后重定向的query参数
		redict_parse = request.POST.get("redict_parse")
		if redict_parse:
			url = parse.urlparse(redict_parse)
			query_dict = parse.parse_qs(url.query)
			code = query_dict.get("code")[0]
			if code:
				# 获取(access_token, open_id, refresh_token)
				access_token_url = "https://open.douyin.com/oauth/access_token/"
				access_token_json = {"grant_type": "authorization_code",
				                     "client_key": "awpswfd65m22r59e",
				                     "client_secret": "f801426192c924f33d6f67d702ba0099",
				                     "code": code}
				access_token_header = {"Content-Type": "application/json"}
				access_token_responses = requests.post(url=access_token_url, json=access_token_json,
				                                       headers=access_token_header)
				access_token_responses_responses_data = access_token_responses.json()

				access_token = access_token_responses_responses_data["data"]["access_token"]
				open_id = access_token_responses_responses_data["data"]["open_id"]
				refresh_token = access_token_responses_responses_data["data"]["refresh_token"]
				expires_in = access_token_responses_responses_data["data"]["expires_in"]

				# 获取用户基本信息()
				user_open_info_url = "https://open.douyin.com/oauth/userinfo/"
				user_open_info_json = {
					"access_token": access_token,
					"open_id": open_id
				}
				user_open_info_header = {"Content-Type": "application/x-www-form-urlencoded"}
				user_open_info_responses = requests.post(url=user_open_info_url, data=user_open_info_json,
				                                         headers=user_open_info_header)
				user_open_info_responses_data = user_open_info_responses.json()

				nickname = user_open_info_responses_data["data"]["nickname"]
				avatar = user_open_info_responses_data["data"]["avatar"]
				e_account_role = user_open_info_responses_data["data"]["e_account_role"]

				# 用户基本参数
				# 将时间转成datetime类型
				expires_time = datetime.now() + timedelta(seconds=expires_in)
				expires_time = datetime.strftime(expires_time, "%Y-%m-%d %H:%M:%S")
				auth_time = datetime.now()
				auth_time = datetime.strftime(auth_time, "%Y-%m-%d %H:%M:%S")
				e_account_role_identify = e_account_role if e_account_role else "None"
				user_info_dict = {
					"uid_id": data_dict.get("uid"),
					"nickname": nickname,
					"access_token": access_token,
					"refresh_token": refresh_token,
					"avatar": avatar,
					"e_account_role": e_account_role_identify,
					"expires_in": expires_time,
					"auth_time": auth_time
				}

				# 判断账号是否存在
				exists = models.PlatFormDouYin.objects.filter(open_id=open_id).exists()
				if exists:
					models.PlatFormDouYin.objects.filter(open_id=open_id).update(**user_info_dict)
				else:
					user_info_dict["open_id"] = open_id
					models.PlatFormDouYin.objects.create(**user_info_dict)

	return redirect("/account/auth/list/")


def account_auth_get(request):
	"""获取授权账号表格数据"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")

	row_id = 0
	data = {
		"total": 0,
		"rows": []
	}

	queryset_dy = models.PlatFormDouYin.objects.filter(uid=uid)
	for index, item in enumerate(queryset_dy):
		data["total"] += index
		row_id += 1
		content = {
			"id": row_id,
			"platform": "抖音",
			"nickname": item.nickname,
			"avatar": item.avatar,
			"auth_time": item.auth_time,
			"expires_time": item.expires_in,
			"status": item.expires_in > datetime.now(),
			"open_id": item.open_id
		}

		data["rows"].append(content)

	queryset_zh = models.PlatFormZhiHu.objects.filter(uid=uid)
	for index, item in enumerate(queryset_zh):
		data["total"] += index
		row_id += 1

		content = {
			"id": row_id,
			"platform": "知乎",
			"nickname": item.nickname,
			"avatar": item.avatar,
			"auth_time": item.auth_time,
			"expires_time": item.expires_time,
			"status": item.expires_time > datetime.now(),
			"zh_uid": item.zh_uid
		}

		data["rows"].append(content)

	return JsonResponse(data)


def account_delete(request):
	"""删除授权账号"""

	delete_id = request.GET.get("delete_id")

	dy_query = Q(open_id=delete_id)
	zh_query = Q(zh_uid=delete_id)

	# 利用 Q 对象，可以在一个查询中检查多个条件
	exists_dy = models.PlatFormDouYin.objects.filter(dy_query).exists()
	exists_zh = models.PlatFormZhiHu.objects.filter(zh_query).exists()

	if exists_dy:
		models.PlatFormDouYin.objects.filter(dy_query).delete()
		return JsonResponse({"status": True})
	elif exists_zh:
		models.PlatFormZhiHu.objects.filter(zh_query).delete()
		return JsonResponse({"status": True})

	return JsonResponse({"status": False})


def account_data_list(request):
	"""数据展示"""

	# 前端选中标签
	active_account_data = ""
	header_label = ""
	if request.path == "/account/data/list/":
		active_account_data = "active"
		header_label = "数据展示"

	context = {
		"active_account_data": active_account_data,
		"header_label": header_label
	}
	return render(request, "account_data_list.html", context)


def account_data_get(request):
	"""获取授权账号数据表格数据"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")

	data = {
		"total": 0,
		"rows": []
	}

	queryset_dy = models.DataDouYin.objects.filter(uid=uid).select_related('open_id').values(
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

	for index, item in enumerate(queryset_dy):
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
					"play_count": item["statistics"]["play_count"],
					"share_count": item["statistics"]["share_count"]
				}
				models.DataDouYin.objects.filter(item_id=item["item_id"]).update(**update_data)
			else:
				create_data = {
					"item_id": item["item_id"],
					"open_id": models.PlatFormDouYin.objects.get(open_id=open_id),
					"uid": models.User.objects.get(uid=uid),
					"title": item["title"],
					"video_status": item["video_status"],
					"create_time": create_time,
					"media_type": media_type,
					"cover": item["cover"],
					"is_top": item["is_top"],
					"share_url": item["share_url"],
					"comment_count": item["statistics"]["comment_count"],
					"digg_count": item["statistics"]["digg_count"],
					"play_count": item["statistics"]["play_count"],
					"share_count": item["statistics"]["share_count"]
				}

				models.DataDouYin.objects.create(**create_data)

	return JsonResponse({"status": True})


def account_auth_refresh(request):
	""" 刷新refresh_token """

	refresh_id = request.GET.get("refresh_id")

	exists_zh = models.PlatFormZhiHu.objects.filter(zh_uid=refresh_id).exists()
	if exists_zh:
		data = {
			"status": False,
			"data": {
				"stats": "刷新失败",
				"tips": "知乎账号刷新无效，如已过期，请删除后重新授权"
			}
		}
		return JsonResponse(data)

	row_object = models.PlatFormDouYin.objects.filter(open_id=refresh_id).first()

	rft_data = {
		"refresh_token": row_object.refresh_token,
		"client_key": "awpswfd65m22r59e"
	}
	rft_response = requests.post('https://open.douyin.com/oauth/renew_refresh_token/', data=rft_data)
	rft_response_data = rft_response.json().get("data", "")
	rft_response_message = rft_response.json().get("message", "")

	if rft_response_message == 'success':
		models.PlatFormDouYin.objects.filter(open_id=refresh_id).update(
			refresh_token=rft_response_data.get("refresh_token"))
		act_data = {
			'client_key': "awpswfd65m22r59e",
			'grant_type': "refresh_token",
			'refresh_token': rft_response_data.get("refresh_token"),
		}
		act_response = requests.post('https://open.douyin.com/oauth/refresh_token/', data=act_data)
		act_response_data = act_response.json().get("data", "")
		act_response_message = act_response.json().get("message")

		if act_response_message:
			access_token = act_response_data["access_token"]
			expires_in = act_response_data["expires_in"]
			expires_time = datetime.now() + timedelta(seconds=expires_in)
			expires_time = datetime.strftime(expires_time, "%Y-%m-%d %H:%M:%S")

			models.PlatFormDouYin.objects.filter(open_id=refresh_id).update(access_token=access_token,
			                                                                expires_in=expires_time)
			nickname = models.PlatFormDouYin.objects.filter(open_id=refresh_id).first().nickname
			print(nickname)
			data = {
				"status": True,
				"data": {
					"stats": "刷新成功",
					"tips": f"{nickname}将在{expires_time}后过期"
				}
			}
			return JsonResponse(data)

	data = {
		"status": False,
		"data": {
			"stats": "刷新失败",
			"tips": "refresh_token过期，请删除授权账号重新授权"
		}
	}
	return JsonResponse(data)
