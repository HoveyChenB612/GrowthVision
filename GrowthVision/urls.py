"""
URL configuration for GrowthVision project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from mainsite.views import index, account, user, hot

urlpatterns = [
	# path('admin/', admin.site.urls),

	# 主页
	path("index/", index.index),

	# 平台账号
	path("account/auth/list/", account.account_auth_list),
	path("account/auth/douyin/", account.account_auth_douyin),
	path("account/auth/zhihu/", account.account_auth_zhihu),
	path("account/auth/baijiahao/",account.account_auth_baijiahao),
	path("account/auth/get/", account.account_auth_get),
	path("account/delete/", account.account_delete),
	path("account/data/list/", account.account_data_list),
	path("account/data/get/", account.account_data_get),
	path("account/data/update/", account.account_data_update),
	path("account/refresh/", account.account_auth_refresh),

	# 用户账号
	path("login/", user.login),
	path("image/code/", user.image_code),
	path("logout/", user.logout),
	path("register/", user.register),
	path("edit_pwd/", user.edit_pwd),

	# 热词搜索
	path("hot/list/", hot.hot_list)
]
