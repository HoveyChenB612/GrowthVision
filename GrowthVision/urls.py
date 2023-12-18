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
from mainsite.views import index, account, user, hot, task, check

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 主页
    path("index/", index.index),
    path("index/total/bilibili/", index.index_total_bilibili),
    path("index/total/zhihu/", index.index_total_zhihu),
    path("index/total/baijiahao/", index.index_total_baijiahao),
    path("index/echarts/", index.index_echarts),
    # 平台账号
    path("account/auth/list/", account.account_auth_list),
    path("account/auth/detail/", account.account_auth_detail),
    path("account/auth/douyin/", account.account_auth_douyin),
    path("account/auth/bilibili/", account.account_auth_bilibili),
    path("account/auth/zhihu/", account.account_auth_zhihu),
    path("account/auth/baijiahao/", account.account_auth_baijiahao),
    path("account/auth/get/", account.account_auth_get),
    path("account/delete/", account.account_delete),
    path("account/data/list/", account.account_data_list),
    path("account/data/get/", account.account_data_get),
    path("account/data/update/", account.account_data_update),
    path("account/refresh/", account.account_auth_refresh),
    path("account/auth/detail/echarts/", account.account_auth_detail_echarts),
    # 用户账号
    path("login/", user.login),
    path("image/code/", user.image_code),
    path("logout/", user.user_logout),
    path("register/", user.register),
    path("edit_pwd/", user.edit_pwd),
    # 热词搜索
    path("hot/list/", hot.hot_list),
    # 主页
    path("", index.main),
    # 敏感词检测
    path("check/article/", check.check_article),
    path("check/article/get/words/", check.check_article_get_words),
    path("check/article/save/words/", check.check_article_save_words),
    # 测试数据定时任务
    # path("history/data/update/", task.history_data_update),
]
