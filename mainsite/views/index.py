import os
import pandas as pd
from django.db.models import Sum, F
from django.http import JsonResponse
from django.shortcuts import redirect, render

from GrowthVision.settings import STATIC_ROOT
from mainsite import models
from mainsite.utils.statistics import statistics
from mainsite.utils.render_words_cloud import render_words_cloud


def index(request):
	"""获取数据总计"""

	# 前端选中标签与头部标签
	active_index = ""
	header_label = ""
	if request.path == "/index/":
		active_index = "active"
		header_label = "首页"

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	role = request.session.get("info").get("role")

	fields = [
		"like_count",
		"comment_count",
		"play_count",
		"download_rec_count",
		"share_vote_count",
		"forward_collect_count",
	]
	data_dict = {}
	top_10_douyin = {}
	for field in fields:
		if role:
			queryset = (
				models.PlatFormData.objects.all()
				.filter(platform=1)
				.aggregate(Sum(field))
			)

			# 排名前十的作品
			top_10_douyin = (
				models.PlatFormData.objects.all().filter(platform=1)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)
		else:
			queryset = (
				models.PlatFormData.objects.filter(uid_id=uid)
				.filter(platform=1)
				.aggregate(Sum(field))
			)

			# 排名前十的作品
			top_10_douyin = (
				models.PlatFormData.objects.filter(uid_id=uid).filter(platform=1)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)
		data_dict.update(queryset)

	update_time = "none"
	null_object = models.PlatFormData.objects.first()
	if null_object:
		update_time = null_object.update_time

	context = {
		"active_index": active_index,
		"header_label": header_label,
		"update_time": update_time,
		"data": data_dict,
		"current": "抖音",
		"dropdown": [
			{"platform": "知乎", "url": "/index/total/zhihu/"},
			{"platform": "百家号", "url": "/index/total/baijiahao/"},
			{"platform": "哔哩哔哩", "url": "/index/total/bilibili/"},
		],
		"top_10": top_10_douyin,
	}

	return render(request, "index.html", context)


def index_total_zhihu(request):
	"""获取数据总计"""

	# 前端选中标签与头部标签
	active_index = ""
	header_label = ""
	if request.path == "/index/total/zhihu/":
		active_index = "active"
		header_label = "首页"

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	role = request.session.get("info").get("role")

	fields = [
		"like_count",
		"comment_count",
		"play_count",
		"download_rec_count",
		"share_vote_count",
		"forward_collect_count",
	]
	data_dict = {}
	top10_zhihu = {}
	for field in fields:
		if role:
			queryset = (
				models.PlatFormData.objects.all()
				.filter(platform=2)
				.aggregate(Sum(field))
			)
			data_dict.update(queryset)

			# 排名前十的作品
			top10_zhihu = (
				models.PlatFormData.objects.all().filter(platform=2)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)
		else:
			queryset = (
				models.PlatFormData.objects.filter(uid_id=uid)
				.filter(platform=2)
				.aggregate(Sum(field))
			)
			data_dict.update(queryset)

			# 排名前十的作品
			top10_zhihu = (
				models.PlatFormData.objects.filter(uid_id=uid).filter(platform=2)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)

	update_time = "none"
	null_object = models.PlatFormData.objects.first()
	if null_object:
		update_time = null_object.update_time

	context = {
		"active_index": active_index,
		"header_label": header_label,
		"update_time": update_time,
		"data": data_dict,
		"current": "知乎",
		"dropdown": [
			{"platform": "抖音", "url": "/index/"},
			{"platform": "百家号", "url": "/index/total/baijiahao/"},
			{"platform": "哔哩哔哩", "url": "/index/total/bilibili/"},
		],
		"top_10": top10_zhihu,
	}

	return render(request, "index.html", context)


def index_total_bilibili(request):
	"""获取数据总计"""

	# 前端选中标签与头部标签
	active_index = ""
	header_label = ""
	if request.path == "/index/total/bilibili/":
		active_index = "active"
		header_label = "首页"

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	role = request.session.get("info").get("role")

	fields = [
		"like_count",
		"comment_count",
		"play_count",
		"download_rec_count",
		"share_vote_count",
		"forward_collect_count",
	]
	data_dict = {}
	top_10_bilibili = []
	for field in fields:
		if role:
			queryset = (
				models.PlatFormData.objects.all()
				.filter(platform=4)
				.aggregate(Sum(field))
			)
			data_dict.update(queryset)

			# 排名前十的作品
			top_10_bilibili = (
				models.PlatFormData.objects.all().filter(platform=4)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)
		else:
			queryset = (
				models.PlatFormData.objects.filter(uid_id=uid)
				.filter(platform=4)
				.aggregate(Sum(field))
			)
			data_dict.update(queryset)

			top_10_bilibili = (
				models.PlatFormData.objects.filter(uid_id=uid).filter(platform=4)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)

	update_time = "none"
	null_object = models.PlatFormData.objects.first()
	if null_object:
		update_time = null_object.update_time

	context = {
		"active_index": active_index,
		"header_label": header_label,
		"update_time": update_time,
		"data": data_dict,
		"current": "哔哩哔哩",
		"dropdown": [
			{"platform": "抖音", "url": "/index/"},
			{"platform": "百家号", "url": "/index/total/baijiahao/"},
			{"platform": "知乎", "url": "/index/total/zhihu/"},
		],
		"top_10": top_10_bilibili,
	}

	return render(request, "index.html", context)


def index_total_baijiahao(request):
	"""获取数据总计"""

	# 前端选中标签与头部标签
	active_index = ""
	header_label = ""
	if request.path == "/index/total/baijiahao/":
		active_index = "active"
		header_label = "首页"

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	role = request.session.get("info").get("role")

	fields = [
		"like_count",
		"comment_count",
		"play_count",
		"download_rec_count",
		"share_vote_count",
		"forward_collect_count",
	]
	data_dict = {}
	top_10_baijiahao = {}
	for field in fields:
		if role:
			queryset = (
				models.PlatFormData.objects.all()
				.filter(platform=3)
				.aggregate(Sum(field))
			)
			data_dict.update(queryset)

			# 排名前十的作品
			top_10_baijiahao = (
				models.PlatFormData.objects.all().filter(platform=3)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)
		else:

			queryset = (
				models.PlatFormData.objects.filter(uid_id=uid)
				.filter(platform=3)
				.aggregate(Sum(field))
			)
			data_dict.update(queryset)

			# 排名前十的作品
			top_10_baijiahao = (
				models.PlatFormData.objects.filter(uid_id=uid).filter(platform=3)
				.annotate(
					total_count=Sum(
						F("like_count")
						+ F("comment_count")
						+ F("play_count")
						+ F("download_rec_count")
						+ F("share_vote_count")
						+ F("forward_collect_count")
					)
				)
				.order_by("-total_count")[:10]
			)

	update_time = "none"
	null_object = models.PlatFormData.objects.first()
	if null_object:
		update_time = null_object.update_time

	context = {
		"active_index": active_index,
		"header_label": header_label,
		"update_time": update_time,
		"data": data_dict,
		"current": "百家号",
		"dropdown": [
			{"platform": "知乎", "url": "/index/total/zhihu/"},
			{"platform": "抖音", "url": "/index/"},
			{"platform": "哔哩哔哩", "url": "/index/total/bilibili/"},
		],
		"top_10": top_10_baijiahao,
	}

	return render(request, "index.html", context)

def main(request):
	"""根目录"""
	return redirect("/index/")

def data_screen_get(request):
	"""数据大屏接口"""

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	role = request.session.get("info").get("role")
	platform_name_dict = {key: value for key, value in models.PlatFormData.platform_choices}
	if role:
		queryset = models.PlatFormData.objects.all().values("platform", "like_count", "comment_count",
		                                                    "play_count", "download_rec_count",
		                                                    "share_vote_count", "forward_collect_count", "nickname")
	else:
		queryset = models.PlatFormData.objects.filter(uid=uid).values("platform", "like_count", "comment_count",
		                                                              "play_count", "download_rec_count",
		                                                              "share_vote_count", "forward_collect_count",
		                                                              "nickname")
	if not queryset.exists():
		return JsonResponse(
			{"status": False, "data": [], "message": "暂无数据，请前往<a href='/account/auth/list'>账号授权</a>页面"})

	platform_play_count = statistics(queryset, is_play_data=True, is_platform_data=True,
	                                 platform_name=platform_name_dict)
	platform_interaction_count = statistics(queryset, is_play_data=False, is_platform_data=True,
	                                        platform_name=platform_name_dict)
	account_play_count = statistics(queryset, is_play_data=True, is_platform_data=False,
	                                platform_name=platform_name_dict)
	account_interaction_count = statistics(queryset, is_play_data=False, is_platform_data=False,
	                                       platform_name=platform_name_dict)

	data = {
		"platform_play_count": platform_play_count,
		"platform_interaction_count": platform_interaction_count,
		"account_play_count": account_play_count,
		"account_interaction_count": account_interaction_count,
	}
	return JsonResponse({"status": True, "data": data, "mes": "数据获取成功"})


def data_screen_get_words_cloud(request):
	"""数据词云"""

	# 获取当前用户ID
	uid = request.session.get("info").get("uid")
	role = request.session.get("info").get("role")

	words_cloud_dir = os.path.join(STATIC_ROOT, "word_cloud_data/")
	user_list = [i.split(".")[0] for i in os.listdir(words_cloud_dir)]

	data = render_words_cloud(role, user_list, uid, words_cloud_dir)

	return JsonResponse(data)
