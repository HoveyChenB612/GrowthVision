from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse


def index(request):
	"""主页"""

	# 前端选中标签与头部标签
	active_index = ""
	header_label = ""
	if request.path == "/index/":
		active_index = "active"
		header_label = "首页"

	context = {
		"active_index": active_index,
		"header_label": header_label,
	}

	return render(request, "index_main.html", context)
