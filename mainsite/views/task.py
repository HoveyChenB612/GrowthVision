from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models import Sum
from django.http import JsonResponse
from django_apscheduler.jobstores import register_job, DjangoJobStore

from mainsite import models
from mainsite.utils.get_data import GetData

print("定时任务正在运行")

# 实例化调度器
scheduler = BackgroundScheduler(timezone="Asia/Shanghai")


# scheduler.add_jobstore(DjangoJobStore(), alias="default")


@register_job(scheduler, "cron", hour="6", minute="10", id="history_update")
def history_data_update():
	"""更新每日历史数据"""

	date = datetime.now()
	date = date.strftime("%Y-%m-%d")

	queryset = models.PlatFormData.objects.values_list("platform_uid")

	platform_uid_set = set()
	for platform_uid in queryset:
		platform_uid_set.add(platform_uid[0])

	for platform_uid in platform_uid_set:
		like_sum = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.aggregate(like_sum=Sum("like_count"))
			.get("like_sum")
		)
		comment_sum = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.aggregate(comment_sum=Sum("comment_count"))
			.get("comment_sum")
		)
		play_sum = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.aggregate(play_sum=Sum("play_count"))
			.get("play_sum")
		)
		download_rec_sum = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.aggregate(download_rec_sum=Sum("download_rec_count"))
			.get("download_rec_sum")
		)
		share_vote_sum = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.aggregate(share_vote_sum=Sum("share_vote_count"))
			.get("share_vote_sum")
		)
		forward_collect_sum = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.aggregate(forward_collect_sum=Sum("forward_collect_count"))
			.get("forward_collect_sum")
		)

		nickname = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.first()
			.nickname
		)
		platform = (
			models.PlatFormData.objects.filter(platform_uid=platform_uid)
			.first()
			.platform
		)
		uid = models.PlatFormData.objects.filter(platform_uid=platform_uid).first().uid
		if platform == 1:
			platform = "抖音"
		elif platform == 2:
			platform = "知乎"
		elif platform == 3:
			platform = "百家号"
		elif platform == 4:
			platform = "哔哩哔哩"

		data = {
			"date": date,
			"nickname": nickname,
			"platform_uid": platform_uid,
			"uid_id": uid,
			"platform": platform,
			"like_sum": like_sum,
			"comment_sum": comment_sum,
			"play_sum": play_sum,
			"download_rec_sum": download_rec_sum,
			"share_vote_sum": share_vote_sum,
			"forward_collect_sum": forward_collect_sum,
		}
		models.HistoryDate.objects.create(**data)
	print(f"历史数据更新完成-{date}")

	# 删除没有授权的历史纪录
	current_platform_uid_queryset = models.PlatFormData.objects.all()
	current_platform_uid_set = set()
	for item in current_platform_uid_queryset:
		current_platform_uid_set.add(item.platform_uid)

	sql_platform_uid_queryset = models.HistoryDate.objects.all()
	sql_platform_uid_set = set()
	for item in sql_platform_uid_queryset:
		sql_platform_uid_set.add(item.platform_uid)
	none_platform_uid_set = sql_platform_uid_set - current_platform_uid_set

	for platform_uid in none_platform_uid_set:
		models.HistoryDate.objects.filter(platform_uid=platform_uid).delete()
	print(f"无授权账号历史数据清理完成-{date}")

	return JsonResponse({"status": True})


@register_job(scheduler, "interval", minutes=2, id="new_data_update")
def new_data_update():
	"""10分钟更新数据"""

	gd = GetData()

	dy_param = []
	dy_queryset = models.PlatFormDouYin.objects.all()
	for item in dy_queryset:
		open_id = item.open_id
		access_token = item.access_token
		nickname = item.nickname
		uid = item.uid
		dy_param.append(
			{
				"nickname": nickname,
				"open_id": open_id,
				"access_token": access_token,
				"uid": uid,
			}
		)

	bz_param = []
	bz_queryset = models.PlatFormBilibili.objects.all()
	for item in bz_queryset:
		openid = item.openid
		access_token = item.access_token
		nickname = item.nickname
		uid = item.uid
		bz_param.append(
			{
				"nickname": nickname,
				"openid": openid,
				"access_token": access_token,
				"uid": uid,
			}
		)

	zh_param = []
	zh_queryset = models.PlatFormZhiHu.objects.all()
	for item in zh_queryset:
		z_c0 = item.z_c0
		zh_uid = item.zh_uid
		nickname = item.nickname
		uid = item.uid
		zh_param.append(
			{"nickname": nickname, "z_c0": z_c0, "zh_uid": zh_uid, "uid": uid}
		)

	bjh_param = []
	bjh_queryset = models.PlatFormBaiJiaHao.objects.all()
	for item in bjh_queryset:
		bjhstoken = item.bjhstoken
		bduss = item.bduss
		token = item.token
		app_id = item.app_id
		nickname = item.nickname
		uid = item.uid
		bjh_param.append(
			{
				"nickname": nickname,
				"bjhstoken": bjhstoken,
				"bduss": bduss,
				"token": token,
				"app_id": app_id,
				"uid": uid,
			}
		)
	dy_nickname = ""
	try:
		for param in dy_param:
			dy_nickname = param["nickname"]
			gd.get_douyin_data(
				param["nickname"], param["open_id"], param["access_token"], param["uid"]
			)
	except Exception as e:
		print(e)
		models.PlatFormDouYin.objects.filter(nickname=dy_nickname).update(expires_in=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		print(f"抖音-{dy_nickname}-数据更新失败{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

	try:
		for param in bz_param:
			gd.get_bilibili_data(
				param["nickname"], param["access_token"], param["openid"], param["uid"]
			)
	except Exception as e:
		print(e)
		print(f"Bilibili数据更新失败{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

	try:
		for param in zh_param:
			gd.get_zhihu_data(
				param["nickname"], param["z_c0"], param["zh_uid"], param["uid"]
			)
	except Exception as e:
		print(e)
		print(f"知乎数据更新失败{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

	try:
		for param in bjh_param:
			gd.get_baijiahao_data(
				param["nickname"],
				param["bjhstoken"],
				param["bduss"],
				param["token"],
				param["app_id"],
				param["uid"],
			)
	except Exception as e:
		print(e)
		print(f"百家号数据更新失败{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


	# 创建或更新数据
	for item in gd.works_list:
		exists = models.PlatFormData.objects.filter(item_id=item["item_id"]).exists()
		if exists:
			models.PlatFormData.objects.filter(item_id=item["item_id"]).update(**item)
		else:
			models.PlatFormData.objects.create(**item)

	# 判断原始数据有没有删除
	sql_item_id_list: list[tuple] = list(
		models.PlatFormData.objects.values_list("item_id")
	)  # [("item_id",),("item_id",)]
	sql_item_id_list = [i[0] for i in sql_item_id_list]  # ["item_id"]
	source_item_id_list = []
	for item in gd.works_list:
		source_item_id_list.append(item["item_id"])
	sql_item_id_set = set(sql_item_id_list)
	source_item_id_set = set(source_item_id_list)
	difference_id = sql_item_id_set - source_item_id_set
	for item_id in difference_id:
		models.PlatFormData.objects.filter(item_id=item_id).delete()

	print(f"数据更新完成{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	return JsonResponse({"status": True})


# 调度器开始运行
scheduler.start()
