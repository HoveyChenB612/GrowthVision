import os
from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
	"""用户表"""
	uid = models.BigIntegerField(verbose_name="用户ID", primary_key=True)
	username = models.CharField(verbose_name="用户名", max_length=32)
	password = models.CharField(verbose_name="密码", max_length=64)
	status_choices = (
		(0, "禁用"),
		(1, "正常"))

	status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
	register_time = models.DateTimeField(verbose_name="注册时间", auto_now_add=True)
	last_login_time = models.DateTimeField(verbose_name="上次登陆时间", auto_now=True)


class PlatFormDouYin(models.Model):
	"""抖音账号授权表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	access_token = models.CharField(verbose_name="client_token 接口调用凭证", max_length=255)
	refresh_token = models.CharField(verbose_name="refresh_token", max_length=64)
	open_id = models.CharField(verbose_name="open_id", max_length=255, primary_key=True)
	expires_in = models.DateTimeField(verbose_name="过期时间")
	auth_time = models.DateTimeField(verbose_name="授权时间", default=timezone.now)
	e_account_role = models.CharField(verbose_name="企业号类型", null=True, max_length=255)
	nickname = models.CharField(verbose_name="昵称", max_length=64)
	avatar = models.CharField(verbose_name="头像", max_length=255)


class PlatFormBilibili(models.Model):
	"""Bilibili账号授权表"""
	openid = models.CharField(verbose_name="openid", max_length=255, primary_key=True)
	access_token = models.CharField(verbose_name="access_token", max_length=255)
	refresh_token = models.CharField(verbose_name="refresh_token", max_length=255)
	nickname = models.CharField(verbose_name="用户名", max_length=64)
	avatar = models.CharField(verbose_name="头像", max_length=255)
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	expires_in = models.DateTimeField(verbose_name="过期时间")
	auth_time = models.DateTimeField(verbose_name="授权时间", default=timezone.now)


class PlatFormZhiHu(models.Model):
	"""知乎账号授权表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	nickname = models.CharField(verbose_name="昵称", max_length=26)
	avatar = models.CharField(verbose_name="头像", max_length=255)
	expires_time = models.DateTimeField(verbose_name="过期时间")
	auth_time = models.DateTimeField(verbose_name="授权时间", default=timezone.now)
	zh_uid = models.CharField(verbose_name="知乎用户ID", primary_key=True, max_length=255)
	z_c0 = models.CharField(verbose_name="授权cookies", max_length=500)


class PlatFormBaiJiaHao(models.Model):
	"""百家号账号授权表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	nickname = models.CharField(verbose_name="昵称", max_length=26)
	avatar = models.CharField(verbose_name="头像", max_length=255)
	expires_time = models.DateTimeField(verbose_name="过期时间")
	auth_time = models.DateTimeField(verbose_name="授权时间", default=timezone.now)
	app_id = models.CharField(verbose_name="百家号用户ID", primary_key=True, max_length=255)
	bduss = models.CharField(verbose_name="授权cookies", max_length=500)
	token = models.CharField(verbose_name="授权token", max_length=500)
	bjhstoken = models.CharField(verbose_name="授权cookies", max_length=500, default=None)


class PlatFormData(models.Model):
	"""平台数据表"""
	platform_choices = ((0, "未知"), (1, "抖音"), (2, "知乎"), (3, "百家号"), (4, "哔哩哔哩"))
	platform = models.SmallIntegerField(verbose_name="平台名称", choices=platform_choices, default=0)
	item_id = models.CharField(verbose_name="作品ID", max_length=500, primary_key=True)
	title = models.CharField(verbose_name="作品标题", max_length=255)
	type = models.CharField(verbose_name="作品类型", max_length=64)
	create_time = models.DateTimeField(verbose_name="创建时间")
	update_time = models.DateTimeField(verbose_name="数据更新时间")
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	platform_uid = models.CharField(verbose_name="平台用ID", max_length=500)
	share_url = models.CharField(verbose_name="分享链接", max_length=500)
	like_count = models.IntegerField(verbose_name="点赞数")
	comment_count = models.IntegerField(verbose_name="评论数")
	play_count = models.IntegerField(verbose_name="播放数")
	download_rec_count = models.IntegerField(verbose_name="下载数/推荐数")
	share_vote_count = models.IntegerField(verbose_name="分享数/赞同数")
	forward_collect_count = models.IntegerField(verbose_name="转发数/收藏数")
	nickname = models.CharField(verbose_name="用户昵称", max_length=64)


class HistoryDate(models.Model):
	"""历史数据"""
	date = models.DateField(verbose_name="时间")
	nickname = models.CharField(verbose_name="用户名", max_length=64)
	platform_uid = models.CharField(verbose_name="平台用ID", max_length=500)
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	platform = models.CharField(verbose_name="平台", max_length=64)
	like_sum = models.IntegerField(verbose_name="点赞数")
	comment_sum = models.IntegerField(verbose_name="评论数")
	play_sum = models.IntegerField(verbose_name="播放数")
	download_rec_sum = models.IntegerField(verbose_name="下载数/推荐数")
	share_vote_sum = models.IntegerField(verbose_name="分享数/赞同数")
	forward_collect_sum = models.IntegerField(verbose_name="转发数/收藏数")


class SensitiveWords(models.Model):
	"""敏感词库"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	group = models.SmallIntegerField(verbose_name="分组")
	update_time = models.DateTimeField(verbose_name="更新时间")
	words = models.CharField(verbose_name="敏感词", max_length=2000)


def upload_path_handler(instance):
	return os.path.join('videos', instance.user.uid)


class PublishVideo(models.Model):
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	title = models.CharField(verbose_name="标题", max_length=120)
	keys = models.CharField(verbose_name="关键字", max_length=300)
	text = models.CharField(verbose_name="正文", max_length=2700)
	status_choices = (
		(0, "发布失败"),
		(1, "发布成功"),
		(2, "发布等待"),
	)
	publish_type_choices = (
		(0, "now"),
		(1, "after")
	)
	publish_type = models.SmallIntegerField(verbose_name="发布类型", choices=publish_type_choices)
	status = models.SmallIntegerField(verbose_name="发布状态", choices=status_choices)
	file = models.FileField(upload_to=upload_path_handler)
	upload_time = models.DateTimeField(verbose_name="上传时间", default=timezone.now)
	publish_time = models.DateTimeField(verbose_name="发布时间", default=timezone.now)
	task_id = models.CharField(verbose_name="任务ID", null=True, max_length=255)
	publish_nickname = models.CharField(verbose_name="发布账号用户名", max_length=255)
	publish_pid = models.CharField(verbose_name="发布账号平台ID", max_length=255)


class CookieInfo(models.Model):
	uid = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="用户ID")
	avatar = models.CharField(verbose_name="头像地址", max_length=255)
	pid = models.CharField(verbose_name="用户平台ID", max_length=255)
	nickname = models.CharField(verbose_name="用户名", max_length=255)
	isChecked = models.BooleanField(verbose_name="是否选中")
	cookies = models.JSONField(verbose_name="用户cookies")
	status_choices = (
		(0, "无效"),
		(1, "有效")
	)
	status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
