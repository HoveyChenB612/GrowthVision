from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from mainsite import models
from django.db.models import Sum, F
from datetime import datetime, timedelta


def index(request):
    """获取数据总计"""

    # 前端选中标签与头部标签
    active_index = ""
    header_label = ""
    if request.path == "/index/":
        active_index = "active"
        header_label = "首页"

    # 获取当前用户ID
    uid = request.session.get("info").get("uid")

    fields = [
        "like_count",
        "comment_count",
        "play_count",
        "download_rec_count",
        "share_vote_count",
        "forward_collect_count",
    ]
    data_dict = {}
    for field in fields:
        queryset = (
            models.PlatFormData.objects.filter(uid_id=uid)
            .filter(platform=1)
            .aggregate(Sum(field))
        )
        data_dict.update(queryset)

    # 排名前十的作品
    top_10 = (
        models.PlatFormData.objects.filter(uid_id=uid)
        .annotate(
            total_count=Sum(
                F("like_count")
                + F("comment_count")
                + F("play_count")
                + F("download_rec_count")
                + F("share_vote_count")
                + F("forward_collect_count")
            )
        )
        .order_by("-total_count")[:10]
    )

    update_time = "none"
    null_object = models.PlatFormData.objects.first()
    if null_object:
        update_time = null_object.update_time

    context = {
        "active_index": active_index,
        "header_label": header_label,
        "update_time": update_time,
        "data": data_dict,
        "current": "抖音",
        "dropdown": [
            {"platform": "知乎", "url": "/index/total/zhihu/"},
            {"platform": "百家号", "url": "/index/total/baijiahao/"},
            {"platform": "哔哩哔哩", "url": "/index/total/bilibili/"},
        ],
        "top_10": top_10,
    }

    return render(request, "index.html", context)


def index_total_zhihu(request):
    """获取数据总计"""

    # 前端选中标签与头部标签
    active_index = ""
    header_label = ""
    if request.path == "/index/total/zhihu/":
        active_index = "active"
        header_label = "首页"

    # 获取当前用户ID
    uid = request.session.get("info").get("uid")

    fields = [
        "like_count",
        "comment_count",
        "play_count",
        "download_rec_count",
        "share_vote_count",
        "forward_collect_count",
    ]
    data_dict = {}
    for field in fields:
        queryset = (
            models.PlatFormData.objects.filter(uid_id=uid)
            .filter(platform=2)
            .aggregate(Sum(field))
        )
        data_dict.update(queryset)

    # 排名前十的作品
    top_10 = (
        models.PlatFormData.objects.filter(uid_id=uid)
        .annotate(
            total_count=Sum(
                F("like_count")
                + F("comment_count")
                + F("play_count")
                + F("download_rec_count")
                + F("share_vote_count")
                + F("forward_collect_count")
            )
        )
        .order_by("-total_count")[:10]
    )

    update_time = "none"
    null_object = models.PlatFormData.objects.first()
    if null_object:
        update_time = null_object.update_time

    context = {
        "active_index": active_index,
        "header_label": header_label,
        "update_time": update_time,
        "data": data_dict,
        "current": "知乎",
        "dropdown": [
            {"platform": "抖音", "url": "/index/"},
            {"platform": "百家号", "url": "/index/total/baijiahao/"},
            {"platform": "哔哩哔哩", "url": "/index/total/bilibili/"},
        ],
        "top_10": top_10,
    }

    return render(request, "index.html", context)


def index_total_bilibili(request):
    """获取数据总计"""

    # 前端选中标签与头部标签
    active_index = ""
    header_label = ""
    if request.path == "/index/total/bilibili/":
        active_index = "active"
        header_label = "首页"

    # 获取当前用户ID
    uid = request.session.get("info").get("uid")

    fields = [
        "like_count",
        "comment_count",
        "play_count",
        "download_rec_count",
        "share_vote_count",
        "forward_collect_count",
    ]
    data_dict = {}
    for field in fields:
        queryset = (
            models.PlatFormData.objects.filter(uid_id=uid)
            .filter(platform=4)
            .aggregate(Sum(field))
        )
        data_dict.update(queryset)

    # 排名前十的作品
    top_10 = (
        models.PlatFormData.objects.filter(uid_id=uid)
        .annotate(
            total_count=Sum(
                F("like_count")
                + F("comment_count")
                + F("play_count")
                + F("download_rec_count")
                + F("share_vote_count")
                + F("forward_collect_count")
            )
        )
        .order_by("-total_count")[:10]
    )

    update_time = "none"
    null_object = models.PlatFormData.objects.first()
    if null_object:
        update_time = null_object.update_time

    context = {
        "active_index": active_index,
        "header_label": header_label,
        "update_time": update_time,
        "data": data_dict,
        "current": "哔哩哔哩",
        "dropdown": [
            {"platform": "抖音", "url": "/index/"},
            {"platform": "百家号", "url": "/index/total/baijiahao/"},
            {"platform": "知乎", "url": "/index/total/zhihu/"},
        ],
        "top_10": top_10,
    }

    return render(request, "index.html", context)


def index_total_baijiahao(request):
    """获取数据总计"""

    # 前端选中标签与头部标签
    active_index = ""
    header_label = ""
    if request.path == "/index/total/baijiahao/":
        active_index = "active"
        header_label = "首页"

    # 获取当前用户ID
    uid = request.session.get("info").get("uid")

    fields = [
        "like_count",
        "comment_count",
        "play_count",
        "download_rec_count",
        "share_vote_count",
        "forward_collect_count",
    ]
    data_dict = {}
    for field in fields:
        queryset = (
            models.PlatFormData.objects.filter(uid_id=uid)
            .filter(platform=3)
            .aggregate(Sum(field))
        )
        data_dict.update(queryset)

    # 排名前十的作品
    top_10 = (
        models.PlatFormData.objects.filter(uid_id=uid)
        .annotate(
            total_count=Sum(
                F("like_count")
                + F("comment_count")
                + F("play_count")
                + F("download_rec_count")
                + F("share_vote_count")
                + F("forward_collect_count")
            )
        )
        .order_by("-total_count")[:10]
    )

    update_time = "none"
    null_object = models.PlatFormData.objects.first()
    if null_object:
        update_time = null_object.update_time

    context = {
        "active_index": active_index,
        "header_label": header_label,
        "update_time": update_time,
        "data": data_dict,
        "current": "百家号",
        "dropdown": [
            {"platform": "知乎", "url": "/index/total/zhihu/"},
            {"platform": "抖音", "url": "/index/"},
            {"platform": "哔哩哔哩", "url": "/index/total/bilibili/"},
        ],
        "top_10": top_10,
    }

    return render(request, "index.html", context)


def index_echarts(request) -> JsonResponse:
    """图表数据"""

    uid = request.session.get("info").get("uid")
    queryset = (
        models.HistoryDate.objects.filter(uid_id=uid)
        .values_list("date", flat=True)
        .distinct()
    )
    date_list = sorted(queryset)[-5:]

    data = []
    for date in date_list:
        queryset = (
            models.HistoryDate.objects.filter(uid_id=uid).filter(date=date).values()
        )
        data.append(queryset)

    # 初始化空的 series_dict
    series_dict = {}

    # 定义指标列表
    metrics = [
        "like_sum",
        "comment_sum",
        "play_sum",
        "download_rec_sum",
        "share_vote_sum",
        "forward_collect_sum",
    ]

    # 遍历每个 QuerySet
    for queryset in data:
        # 遍历每个数据项
        for item in queryset:
            # 生成标识符，例如 "抖音-四叶天代理IP001"
            identifier = f"{item['platform']}-{item['nickname']}"

            # 遍历每个指标
            for metric in metrics:
                # 初始化字典结构
                if metric not in series_dict:
                    series_dict[metric] = {"seriesData": {}}

                # 初始化平台-昵称键，如果不存在就创建一个空列表
                if identifier not in series_dict[metric]["seriesData"]:
                    series_dict[metric]["seriesData"][identifier] = []

                # 添加值到对应的列表中
                series_dict[metric]["seriesData"][identifier].append(item[metric])

    backend_data = {
        "categories": [i.strftime("%Y-%m-%d") for i in date_list],
        "seriesData": series_dict,
    }
    return JsonResponse({"status": True, "backendData": backend_data})


def main(request):
    """根目录"""
    return redirect("/index/")
