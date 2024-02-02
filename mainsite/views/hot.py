from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from mainsite import models
from mainsite.utils.search_dy_rank import searchDyRank
from urllib.parse import quote, unquote


def hot_list(request):
	"""热词搜索"""
	# 前端选中标签
	active_hot = ""
	header_label = ""
	if request.path == "/hot/list/":
		active_hot = "active"
		header_label = "搜索排行"

	context = {
		"active_hot": active_hot,
		"header_label": header_label,
	}

	return render(request, "hot_list.html", context)


def hot_list_get(request):
	"""获取热词列表"""

	keywords_value = request.GET.get("keywords")

	search_result = searchDyRank(keywords_value)
	if not search_result:
		data = {"total": 0, "rows": []}
		return JsonResponse(data)
	# 将数据发送到前端
	data = {"total": 0, "rows": []}
	for item in search_result:
		data["total"] += 1
		content = {
			"id": item["rank"],
			"avatar": item["avatar"],
			"nickname": item["nickname"],
			"title": item["title"],
			"digg_count": item["digg_count"],
			"comment_count": item["comment_count"],
			"collect_count": item["collect_count"],
			"share_count": item["share_count"],
			"download_count": item["download_count"],
			"create_time": item["create_time"],
			"share_url": item["share_url"],
		}
		data["rows"].append(content)
	return JsonResponse(data)
