import random
from io import BytesIO
from django.utils import timezone
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from mainsite import models
from mainsite.utils.code import check_code
from mainsite.utils.encrypt import md5
from mainsite.utils.form import LoginForm, RegisterForm, EditPwdForm
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout


def login(request):
	"""用户登陆"""
	if request.method == "GET":
		form = LoginForm()
		return render(request, "user_login.html", {"form": form})

	form = LoginForm(data=request.POST)
	if form.is_valid():
		# 验证码的校验
		user_input_code = form.cleaned_data.pop('code')
		code = request.session.get('image_code', "")
		if code != user_input_code:
			form.add_error("code", "验证码错误")
			return render(request, 'user_login.html', {'form': form})

		# 去数据库校验用户名和密码是否正确，获取用户对象、None
		# admin_object = models.Admin.objects.filter(username=xxx, password=xxx).first()
		admin_object = models.User.objects.filter(**form.cleaned_data).first()
		if not admin_object:
			form.add_error("password", "用户名或密码错误")
			# form.add_error("username", "用户名或密码错误")
			return render(request, 'user_login.html', {'form': form})

		# 用户名和密码正确
		# 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；(新增用户角色)
		request.session["info"] = {'uid': admin_object.uid, 'username': admin_object.username, 'role': admin_object.role}
		# session可以保存5天
		request.session.set_expiry(60 * 60 * 24 * 5)

		# 修改用户登陆时间
		models.User.objects.filter(**form.cleaned_data).update(last_login_time=timezone.now())
		return redirect("/index/")

	return render(request, 'user_login.html', {'form': form})


def image_code(request):
	""" 生成图片验证码 """

	# 调用pillow函数，生成图片
	img, code_string = check_code()

	# 写入到自己的session中（以便于后续获取验证码再进行校验）
	request.session['image_code'] = code_string
	# 给Session设置60s超时
	request.session.set_expiry(60)

	stream = BytesIO()
	img.save(stream, 'png')
	return HttpResponse(stream.getvalue())


def user_logout(request):
	"""用户注销"""
	# request.session.clear()
	logout(request)
	return redirect('/login/')


@csrf_exempt
def register(request):
	"""用户注册"""

	if request.method == "GET":
		form = RegisterForm()
		return render(request, "user_register.html", {"form": form})

	form = RegisterForm(data=request.POST)
	if form.is_valid():
		# 生成随机uid
		date = datetime.now().strftime("%Y%m%d")
		random_int_4 = f"{random.randint(0000, 9999):04}"
		form.instance.uid = int(date + random_int_4)
		form.save()
		return JsonResponse({"status": True})

	return JsonResponse({"status": False, "errors": form.errors})


@csrf_exempt
def edit_pwd(request):
	"""修改密码"""

	if request.method == "GET":
		form = EditPwdForm()
		return render(request, 'user_edit_pwd.html', {"form": form})

	uid = request.session.get("info").get("uid")
	row_object = models.User.objects.get(pk=uid)

	form = EditPwdForm(data=request.POST, instance=row_object)
	if form.is_valid():
		password = form.cleaned_data.get("new_password")
		models.User.objects.filter(pk=uid).update(password=password)
		return JsonResponse({"status": True})

	return JsonResponse({"status": False, "errors": form.errors})
