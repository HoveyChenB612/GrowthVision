import ast
import datetime
import json
import os
import time
from datetime import datetime as dt, timedelta
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJob

from mainsite import models
from mainsite.utils.publish import get_user_info, publish


def video(request):
	"""视频视图"""
	# 前端选中标签与头部标签
	active_video = ""
	header_label = ""
	if request.path == "/video/":
		active_video = "active"
		header_label = "视频发布"

	context = {
		"active_video": active_video,
		"header_label": header_label,
	}

	return render(request, "video.html", context)


@csrf_exempt
def user_info(request):
	"""获取用户信息"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")

	cookies = request.POST.get("cookies")

	# {'status': True, 'code': 1, 'mes': '用户信息获取成功', 'data': {}, 'info': {'nickname': '四叶天代理IP001','avatar': '','douyinid': 'fourleafsky001','cookies': []}}

	data = get_user_info(cookies)

	if data["code"] != 0:

		data_object = {
			"uid_id": uid,
			"avatar": data["info"]["avatar"],
			"pid": data["info"]["douyinid"],
			"nickname": data["info"]["nickname"],
			"isChecked": True,
			"cookies": data["info"]["cookies"]
		}
		exists = models.CookieInfo.objects.filter(pid=data["info"]["douyinid"]).filter(uid_id=uid).exists()
		if exists:
			del data_object["pid"]
			models.CookieInfo.objects.filter(pid=data["info"]["douyinid"]).filter(uid_id=uid).update(**data_object)
			data["mes"] = "账号更新成功"
			return JsonResponse(data)

		data["mes"] = "账号添加成功"
		models.CookieInfo.objects.create(**data_object)
		return JsonResponse(data)

	return JsonResponse(data)


def load_user_info(request):
	"""加载授权账号信息"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")
	queryset = models.CookieInfo.objects.filter(uid_id=uid).all()
	auth_object = []
	for item in queryset:
		auth_dict = {
			"Avatar": item.avatar,
			"Cookies": item.cookies,
			"douyinNid": item.pid,
			"isChecked": item.isChecked,
			"nickName": item.nickname
		}
		auth_object.append(auth_dict)

	return JsonResponse({"status": True, "data": auth_object})


def delete_user_info(request):
	"""删除授权账号"""
	douyin_nid = request.GET.get("douyinNid")
	if douyin_nid:
		models.CookieInfo.objects.filter(pid=douyin_nid).delete()
		return JsonResponse({"status": True, "mes": "删除成功"})

	return JsonResponse({"status": False, "mes": "删除失败"})


@csrf_exempt
def publish_video(request):
	"""发布视频"""

	# 获取当前登陆的用户uid
	uid = request.session.get("info").get("uid")

	if request.method == "GET":
		return redirect("/video/")

	file_obj = request.FILES.get("file")

	if file_obj:
		# 获取文件名
		file_name = file_obj.name

		uid_folder = f"media/{uid}"
		if not os.path.exists(uid_folder):
			os.makedirs(uid_folder)

		# 检查是否已经存在同名文件
		if os.path.exists(f"media/{uid}/{file_name}"):
			# 如果存在，生成一个新的文件名
			base_name, extension = os.path.splitext(file_name)
			new_file_name = f"{base_name}_{int(time.time())}{extension}"

			# 重命名文件
			file_name = new_file_name

		file_path = f"media/{uid}/{file_name}"
		# 保存文件
		with open(file_path, "wb") as f:
			for chunk in file_obj.chunks():
				f.write(chunk)

		publish_params = json.loads(request.POST.get("data"))
		title = publish_params.get("title")
		keys = publish_params.get("keys")
		des = publish_params.get("des")
		auth_object = publish_params.get("authObject")
		publish_type = publish_params.get("publishType")
		datetime = publish_params.get("datetime")

		if publish_type == "now":
			data = {
				"title": title,
				"keys": keys,
				"text": des,
				"status": 1,
				"publish_type": 0,
				"file": file_path,
				"upload_time": timezone.now(),
				"publish_time": timezone.now(),
				"uid_id": uid,
				"task_id": str(time.perf_counter())
			}

			result = {}
			for item in auth_object:
				cookies = item["Cookies"]
				result = publish(cookies, file_path, title, keys, des)

				if not result["status"]:
					data["status"] = 0
					models.PublishVideo.objects.create(**data)
					return JsonResponse(result, safe=False)

			models.PublishVideo.objects.create(**data)
			return JsonResponse(result, safe=False)

		if publish_type == "after":
			dt_object = dt.strptime(datetime, "%Y-%m-%d %H:%M")

			# 实例化调度器
			scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
			# 调度器使用Django,任务将存在数据库中
			scheduler.add_jobstore(DjangoJobStore(), "default")
			for item in auth_object:
				cookies = item["Cookies"]
				one_minute = timedelta(minutes=1)
				dt_object += one_minute
				task_id = str(time.perf_counter())
				scheduler.add_job(publish, "date", run_date=dt_object, args=[cookies, file_path, title, keys, des],
				                  id=task_id)

				data = {
					"title": title,
					"keys": keys,
					"text": des,
					"status": 2,
					"publish_type": 1,
					"file": file_path,
					"upload_time": timezone.now(),
					"publish_time": dt_object,
					"uid_id": uid,
					"task_id": task_id
				}
				models.PublishVideo.objects.create(**data)

			# 调度器开始运行
			scheduler.start()

			return JsonResponse({"status": True, "mes": f"定时任务创建完成，任务将在{datetime}开始执行"})


def task_list(request):
	"""视频任务列表"""
	uid = request.session.get("info").get("uid")

	row_id = 0
	data = {"total": 0, "rows": []}

	# 检查任务
	publish_queryset_id = set()
	job_queryset_id = set()
	job_queryset_item = []
	publish_queryset = models.PublishVideo.objects.filter(uid_id=uid).filter(publish_type=1).all()
	for item in publish_queryset:
		publish_queryset_id.add(item.task_id)
	job_queryset = DjangoJob.objects.all()
	for item in job_queryset:
		job_queryset_id.add(item.id)

		# 删除过期任务
		if item.next_run_time < dt.now():
			DjangoJob.objects.filter(id=item.id).delete()
	over_id = publish_queryset_id - job_queryset_id
	for item in over_id:
		update_data = {
			"status": 1
		}
		models.PublishVideo.objects.filter(uid_id=uid).filter(task_id=item).update(**update_data)

	show_queryset = models.PublishVideo.objects.filter(uid_id=uid).all().order_by("-publish_time")
	for index, item in enumerate(show_queryset):
		row_id += 1
		data["total"] += index
		content = {
			"id": row_id,
			"title": item.title,
			"keys": ' '.join(map(str, ast.literal_eval(item.keys))),
			"file": item.file.name.split("/")[-1],
			"publish_time": item.publish_time.strftime("%Y-%m-%d %H:%M:%S"),
			"status": item.status,
			"task_id": item.task_id
		}

		data["rows"].append(content)

	return JsonResponse(data)


def task_delete(request):
	"""删除任务"""
	data = {'status': True, 'code': 1, 'mes': '任务删除成功'}
	uid = request.session.get("info").get("uid")
	task_id = float(request.GET.get("task_id"))
	if not task_id:
		data["status"] = False
		data["code"] = 0
		data["mes"] = "删除失败: 任务正在执行"
		return JsonResponse(data)

	job_exists = DjangoJob.objects.filter(id=task_id).exists()
	if not job_exists:
		pass
	else:
		DjangoJob.objects.filter(id=task_id).delete()

	publish_exists = models.PublishVideo.objects.filter(task_id=task_id).filter(uid_id=uid).exists()
	if not publish_exists:
		data["status"] = False
		data["code"] = 0
		data["mes"] = "删除失败: 任务不存在"
		return JsonResponse(data)
	else:
		models.PublishVideo.objects.filter(task_id=task_id).delete()
		return JsonResponse(data)
