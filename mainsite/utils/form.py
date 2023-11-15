from mainsite import models

from django import forms
from django.utils import timezone  # 导入时间工具
from django.core.exceptions import ValidationError

from mainsite.utils.encrypt import md5


class AccountAuthForms(forms.ModelForm):
	"""授权账号表单"""

	class Meta:
		model = models.PlatFormDouYin
		fields = ["avatar", "nickname", "e_account_role", "expires_in"]


class LoginForm(forms.ModelForm):
	"""登陆表单"""

	username = forms.CharField(
		label="用户名",
		widget=forms.TextInput(
			attrs={"type": "text", "class": "form-control", "id": "username", "placeholder": "请输入您的用户名"}),
		required=True
	)
	password = forms.CharField(
		label="密码",
		widget=forms.PasswordInput(
			render_value=True,
			attrs={"type": "password", "class": "form-control", "id": "password", "placeholder": "请输入您的密码"}
		),
		required=True
	)

	code = forms.CharField(
		label="验证码",
		widget=forms.TextInput(
			attrs={"type": "text", "class": "form-control", "id": "image_code", "placeholder": "请输入验证码"}
		),
		required=True
	)

	class Meta:
		model = models.User  # 指定模型类
		fields = ["username", "password"]
		widgets = {

		}

	def clean_password(self):
		pwd = self.cleaned_data.get("password")
		return md5(pwd)


class RegisterForm(forms.ModelForm):
	"""注册表单"""

	username = forms.CharField(
		label="用户名",
		widget=forms.TextInput(
			attrs={"type": "text", "class": "form-control", "id": "username", "placeholder": "请输入您的用户名"}),
		required=True
	)
	password = forms.CharField(
		label="密码",
		widget=forms.PasswordInput(
			render_value=True,
			attrs={"type": "password", "class": "form-control", "id": "password", "placeholder": "请输入您的密码"}
		),
		required=True
	)
	confirm_password = forms.CharField(
		label="确认密码",
		widget=forms.PasswordInput(
			attrs={"type": "password", "class": "form-control", "id": "confirm_password",
			       "placeholder": "请确认您的密码"},
		)
	)

	class Meta:
		model = models.User
		fields = ["username", "password"]

	def clean_password(self):
		"""获取密码并加密"""
		pwd = self.cleaned_data.get("password")

		return md5(pwd)

	def clean_confirm_password(self):
		"""验证密码"""
		pwd = self.cleaned_data.get("password")
		confirm = md5(self.cleaned_data.get("confirm_password"))
		if confirm != pwd:
			raise ValidationError("密码不一致，请重新输入")

		return confirm

	def clean_username(self):
		"""验证用户名"""
		username = self.cleaned_data.get("username")
		exists = models.User.objects.filter(username=username).exists()
		if exists:
			raise ValidationError("用户名已存在")

		return username


class EditPwdForm(forms.ModelForm):
	"""修改密码表单"""

	password = forms.CharField(
		label="旧密码",
		widget=forms.TextInput(
			attrs={"type": "text", "class": "form-control", "id": "password", "placeholder": "请输入账号的原登陆密码"}),
		required=True)

	new_password = forms.CharField(
		label="新密码",
		widget=forms.PasswordInput(
			attrs={"type": "text", "class": "form-control", "id": "newPassword", "placeholder": "请输入新密码"}),
		required=True)

	confirm_password = forms.CharField(
		label="确认新密码",
		widget=forms.PasswordInput(
			attrs={"type": "text", "class": "form-control", "id": "confirm_password", "placeholder": "请再输入新密码"}),
		required=True)

	class Meta:
		model = models.User
		fields = ["password", "new_password", "confirm_password"]

	def clean_password(self):
		"""验证旧密码"""
		pwd = self.cleaned_data.get("password")
		md5_pwd = md5(pwd)
		# 去数据库校验当前密码和新输入的密码是否一致
		exists = models.User.objects.filter(uid=self.instance.pk, password=md5_pwd).exists()
		if not exists:
			raise ValidationError("密码错误")
		return md5_pwd

	def clean_new_password(self):
		"""验证新密码"""
		new_pwd = self.cleaned_data.get("new_password")
		md5_new_pwd = md5(new_pwd)

		exists = models.User.objects.filter(uid=self.instance.pk, password=md5_new_pwd).exists()
		if exists:
			raise ValidationError("新密码不能与之前密码相同")
		return md5_new_pwd

	def clean_confirm_password(self):
		"""验证密码"""
		new_pwd = self.cleaned_data.get("new_password")
		confirm = self.cleaned_data.get("confirm_password")
		md5_new_pwd = md5(confirm)
		if md5_new_pwd != new_pwd:
			raise ValidationError("密码不一致，请重新输入")

		return md5_new_pwd
