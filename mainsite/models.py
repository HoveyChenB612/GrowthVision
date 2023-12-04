from django.db import models


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
	auth_time = models.DateTimeField(verbose_name="授权时间", null="1995-12-15 06:15:00")
	e_account_role = models.CharField(verbose_name="企业号类型", null=True, max_length=255)
	nickname = models.CharField(verbose_name="昵称", max_length=64)
	avatar = models.CharField(verbose_name="头像", max_length=255)


class DataDouYin(models.Model):
	"""抖音账号数据表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	open_id = models.ForeignKey(verbose_name="open_id", to=PlatFormDouYin, on_delete=models.CASCADE)
	item_id = models.CharField(verbose_name="作品ID", max_length=255, primary_key=True)
	title = models.CharField(verbose_name="作品标题", max_length=255)
	video_status_choices = (
		(1, "已发布"),
		(2, "不适宜公开"),
		(4, "审核中")
	)
	video_status = models.SmallIntegerField(verbose_name="视频状态", choices=video_status_choices, default=1)
	create_time = models.CharField(verbose_name="创建时间", max_length=64)
	media_type_choices = (
		(2, "图集"),
		(4, "视频")
	)
	media_type = models.SmallIntegerField(verbose_name="媒体类型", choices=media_type_choices, default=4)
	cover = models.CharField(verbose_name="封面", max_length=500)
	is_top = models.BooleanField(verbose_name="是否置顶", default=False)
	share_url = models.CharField(verbose_name="分享url", max_length=500)
	comment_count = models.IntegerField(verbose_name="评论数", default=0)
	digg_count = models.IntegerField(verbose_name="点赞数", default=0)
	download_count = models.IntegerField(verbose_name="下载数", default=0)
	forward_count = models.IntegerField(verbose_name="收藏数", default=0)
	play_count = models.IntegerField(verbose_name="播放数", default=0)
	share_count = models.IntegerField(verbose_name="分享数", default=0)


class PlatFormZhiHu(models.Model):
	"""知乎账号授权表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	nickname = models.CharField(verbose_name="昵称", max_length=26)
	avatar = models.CharField(verbose_name="头像", max_length=255)
	expires_time = models.DateTimeField(verbose_name="过期时间")
	auth_time = models.DateTimeField(verbose_name="授权时间", null="1995-12-15 06:15:00")
	zh_uid = models.CharField(verbose_name="知乎用户ID", primary_key=True, max_length=255)
	z_c0 = models.CharField(verbose_name="授权cookies", max_length=500)


class DataZhiHu(models.Model):
	"""知乎账号数据表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	zh_uid = models.ForeignKey(verbose_name="知乎用户ID", to=PlatFormZhiHu, on_delete=models.CASCADE)
	item_id = models.CharField(verbose_name="作品ID", max_length=255, primary_key=True)
	title = models.CharField(verbose_name="作品标题", max_length=255)
	like_count = models.IntegerField(verbose_name="点赞数")
	comment_count = models.IntegerField(verbose_name="评论数")
	play_count = models.IntegerField(verbose_name="播放数")
	vote_up_count = models.IntegerField(verbose_name="赞同数")
	share_url = models.CharField(verbose_name="分享url", max_length=500)
	create_time = models.CharField(verbose_name="创建时间", max_length=64)
	type_choices = (
		(2, "文章"),
		(4, "视频")
	)
	type = models.SmallIntegerField(verbose_name="作品类型", choices=type_choices)


class PlatFormBaiJiaHao(models.Model):
	"""百家号账号授权表"""
	uid = models.ForeignKey(verbose_name="用户ID", to=User, on_delete=models.CASCADE)
	nickname = models.CharField(verbose_name="昵称", max_length=26)
	avatar = models.CharField(verbose_name="头像", max_length=255)
	expires_time = models.DateTimeField(verbose_name="过期时间")
	auth_time = models.DateTimeField(verbose_name="授权时间", null="1995-12-15 06:15:00")
	app_id = models.CharField(verbose_name="百家号用户ID", primary_key=True, max_length=255)
	bduss = models.CharField(verbose_name="授权cookies", max_length=500)
	token = models.CharField(verbose_name="授权token", max_length=500)
	bjhstoken = models.CharField(verbose_name="授权cookies", max_length=500, default=None)


class PlatFormData(models.Model):
	"""平台数据表"""
	platform_choices = ((0, "未知"), (1, "抖音"), (2, "知乎"), (3, "百家号"))
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
