from django.http import JsonResponse
from django.shortcuts import render
from mainsite import models


def hot_list(request):
	"""热词搜索"""
	# 前端选中标签
	active_hot = ""
	header_label = ""
	if request.path == "/hot/list/":
		active_hot = "active"
		header_label = "热搜排行"

	context = {
		"active_hot": active_hot,
		"header_label": header_label,
	}

	if request.method == "POST":
		keywords = request.POST.get("keywords")
		context["keywords"] = keywords

		uid = request.session.get("info").get("uid")
		row_object = models.PlatFormDouYin.objects.filter(uid_id=uid).first()
		open_id = row_object.open_id
		access_token = row_object.access_token

	# TODO
	return render(request, "hot_list.html", context)
