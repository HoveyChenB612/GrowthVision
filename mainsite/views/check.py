from django.shortcuts import render, redirect
from django.http import JsonResponse
from mainsite import models
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from datetime import datetime


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


def check_article_get_words(request):
	"""获取敏感词接口"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")
	words = ""
	exists = models.SensitiveWords.objects.filter(uid=uid).exists()
	if exists:
		queryset = models.SensitiveWords.objects.filter(uid=uid).first()
		words = queryset.words

	return JsonResponse({"status": True, "words": words})


@csrf_exempt
def check_article_save_words(request):
	"""保存敏感词接口"""
	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")
	tag_list_js = request.POST.get("list")
	tag_list = json.loads(tag_list_js)
	words = ""
	for word in tag_list:
		words += f"{word['tag']};"
	update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	group = 1  # 埋点分组
	data_dict = {
		"group": group,
		"update_time": update_time,
		"words": words
	}
	exists = models.SensitiveWords.objects.filter(uid=uid).exists()
	if exists:
		models.SensitiveWords.objects.filter(uid=uid).update(**data_dict)
	else:
		data_dict["uid_id"] = uid
		models.SensitiveWords.objects.create(**data_dict)
	return JsonResponse({"status": True, "mes": "Save Success"})


@csrf_exempt
def check_article_checking(request):
	"""检测文章接口"""
	article = json.loads(request.POST.get("article"))
	uid = request.session.get("info").get("uid")
	words = models.SensitiveWords.objects.filter(uid=uid).first().words
	words_list = words.split(";")
	words_list.pop()
	check_after = []
	words_count = 0
	for word in words_list:
		if word in article:
			text_template = f"<span class='alert alert-danger' style='padding:0 5px'>{word}</span>"
			check_after.append(text_template)
			article_list = article.split(word)
			article = text_template.join(article_list)
			words_count += 1
	return JsonResponse({"status": True, "article": article, "wordsCount": words_count})
