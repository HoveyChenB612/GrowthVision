from django.shortcuts import render, redirect


def check_article(request):
	"""文章检测"""
	# 前端选中标签与头部标签
	active_check = ""
	header_label = ""
	if request.path == "/check/article/":
		active_check = "active"
		header_label = "文章检测"

	context = {
		"active_check": active_check,
		"header_label": header_label,
	}
	return render(request, "check_article.html", context)
