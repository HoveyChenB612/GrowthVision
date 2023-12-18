import asyncio
import time
from datetime import datetime, timedelta
from urllib import parse

import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.db.models import Q, Sum
from asgiref.sync import sync_to_async, async_to_sync

from mainsite import models
from mainsite.utils.get_data import GetData


def account_auth_list(request):
    """账号授权列表"""

    # 前端选中标签与头部标签
    active_account_auth = ""
    header_label = ""
    if request.path == "/account/auth/list/":
        active_account_auth = "active"
        header_label = "授权管理"

    # 抖音授权
    client_key = "awpswfd65m22r59e"  # 应用唯一标识
    response_type = "code"  # 默认值 code
    scope = "user_info,data.external.user,video.list.bind,video.data.bind,renew_refresh_token,data.external.item,data.external.billboard_hot_video"  # 应用授权作用域
    # optionalScope = "user_info,1,data.external.user,1"  # 应用授权可选作用域&optionalScope={optionalScope}
    redirect_uri = "https://www.baidu.com"  # 授权成功后的回调地址
    get_accredit_url = f"https://open.douyin.com/platform/oauth/connect?client_key={client_key}&response_type={response_type}&scope={scope}&redirect_uri={redirect_uri}"

    context = {
        "now": timezone.now(),  # 当前时间
        "get_accredit_url": get_accredit_url,  # 抖音授权地址
        "active_account_auth": active_account_auth,
        "header_label": header_label,
    }

    return render(request, "account_auth_list.html", context)


def account_auth_zhihu(request):
    """账号授权知乎"""

    # 获取当前登陆的用户uid
    uid = request.session.get("info").get("uid")

    if request.method == "POST":
        z_c0 = request.POST.get("z_c0")
        if z_c0:
            cookies = {"z_c0": z_c0}
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
            }
            url = "https://www.zhihu.com/api/v4/me"
            response = requests.get(url, headers=headers, cookies=cookies)
            user_info = response.json()
            nickname = user_info.get("name")
            avatar = user_info.get("avatar_url")
            auth_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            expires_time = (datetime.now() + timedelta(days=180)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            zh_uid = user_info.get("id")
            user_info_dict = {
                "uid_id": uid,
                "nickname": nickname,
                "avatar": avatar,
                "auth_time": auth_time,
                "expires_time": expires_time,
                "z_c0": z_c0,
            }
            exists = models.PlatFormZhiHu.objects.filter(zh_uid=zh_uid).exists()
            if exists:
                models.PlatFormZhiHu.objects.filter(zh_uid=zh_uid).update(
                    **user_info_dict
                )
            else:
                user_info_dict["zh_uid"] = zh_uid
                models.PlatFormZhiHu.objects.create(**user_info_dict)

    return redirect("/account/auth/list/")


def account_auth_douyin(request):
    """账号授权抖音"""

    # 获取当前登陆的用户uid
    data_dict = {"uid": request.session.get("info").get("uid")}

    # 获取用户授权信息
    if request.method == "POST":
        # 获取扫码后重定向的query参数
        redict_parse = request.POST.get("redict_parse")
        if redict_parse:
            url = parse.urlparse(redict_parse)
            query_dict = parse.parse_qs(url.query)
            code_option = query_dict.get("code")
            if code_option:
                code = code_option[0]
                # 获取(access_token, open_id, refresh_token)
                access_token_url = "https://open.douyin.com/oauth/access_token/"
                access_token_json = {
                    "grant_type": "authorization_code",
                    "client_key": "awpswfd65m22r59e",
                    "client_secret": "f801426192c924f33d6f67d702ba0099",
                    "code": code,
                }
                access_token_header = {"Content-Type": "application/json"}
                access_token_responses = requests.post(
                    url=access_token_url,
                    json=access_token_json,
                    headers=access_token_header,
                )
                access_token_responses_responses_data = access_token_responses.json()

                access_token = access_token_responses_responses_data["data"][
                    "access_token"
                ]
                open_id = access_token_responses_responses_data["data"]["open_id"]
                refresh_token = access_token_responses_responses_data["data"][
                    "refresh_token"
                ]
                expires_in = access_token_responses_responses_data["data"]["expires_in"]

                # 获取用户基本信息()
                user_open_info_url = "https://open.douyin.com/oauth/userinfo/"
                user_open_info_json = {"access_token": access_token, "open_id": open_id}
                user_open_info_header = {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
                user_open_info_responses = requests.post(
                    url=user_open_info_url,
                    data=user_open_info_json,
                    headers=user_open_info_header,
                )
                user_open_info_responses_data = user_open_info_responses.json()

                nickname = user_open_info_responses_data["data"]["nickname"]
                avatar = user_open_info_responses_data["data"]["avatar"]
                e_account_role = user_open_info_responses_data["data"]["e_account_role"]

                # 用户基本参数
                # 将时间转成datetime类型
                expires_time = datetime.now() + timedelta(seconds=expires_in)
                expires_time = datetime.strftime(expires_time, "%Y-%m-%d %H:%M:%S")
                auth_time = datetime.now()
                auth_time = datetime.strftime(auth_time, "%Y-%m-%d %H:%M:%S")
                e_account_role_identify = e_account_role if e_account_role else "None"
                user_info_dict = {
                    "uid_id": data_dict.get("uid"),
                    "nickname": nickname,
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "avatar": avatar,
                    "e_account_role": e_account_role_identify,
                    "expires_in": expires_time,
                    "auth_time": auth_time,
                }

                # 判断账号是否存在
                exists = models.PlatFormDouYin.objects.filter(open_id=open_id).exists()
                if exists:
                    models.PlatFormDouYin.objects.filter(open_id=open_id).update(
                        **user_info_dict
                    )
                else:
                    user_info_dict["open_id"] = open_id
                    models.PlatFormDouYin.objects.create(**user_info_dict)

    return redirect("/account/auth/list/")


def account_auth_bilibili(request):
    """账号授权 Bilibili"""

    # 获取当前登陆的用户uid
    uid = request.session.get("info").get("uid")

    # 获取用户授权信息
    if request.method == "POST":
        # 获取扫码后重定向的query参数
        return_url = request.POST.get("return_url")
        if return_url:
            url = parse.urlparse(return_url)
            query_dict = parse.parse_qs(url.query)
            code_option = query_dict.get("code")
            if code_option:
                code = code_option[0]
                access_token_url = "https://api.bilibili.com/x/account-oauth2/v1/token"
                access_token_json = {
                    "client_id": "302763bae0404eee",
                    "client_secret": "aef73864a09a42bcbe1bbec8130ee5ed",
                    "grant_type": "authorization_code",
                    "code": code,
                }
                access_token_response = requests.post(
                    url=access_token_url, json=access_token_json
                )
                access_token_result = access_token_response.json()
                if access_token_result.get("code") == 0:
                    data = access_token_result.get("data")
                    access_token = data.get("access_token", "")
                    expires_in = data.get("expires_in", "")
                    refresh_token = data.get("refresh_token", "")

                    # 获取用户信息
                    user_info_url = (
                        "https://member.bilibili.com/arcopen/fn/user/account/info"
                    )
                    user_info_param = {
                        "client_id": "302763bae0404eee",
                        "access_token": access_token,
                    }
                    user_info_response = requests.get(
                        url=user_info_url, params=user_info_param
                    )
                    user_info_result = user_info_response.json()
                    if user_info_result.get("code") == 0:
                        data = user_info_result.get("data")
                        nickname = data.get("name", "")
                        avatar = data.get("face", "")
                        openid = data.get("openid", "")

                        time_object = datetime.utcfromtimestamp(expires_in)
                        expires_time = time_object.strftime("%Y-%m-%d %H:%M:%S")
                        auth_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        row_object = {
                            "access_token": access_token,
                            "refresh_token": refresh_token,
                            "nickname": nickname,
                            "avatar": avatar,
                            "expires_in": expires_time,
                            "auth_time": auth_time,
                            "uid_id": uid,
                        }

                        exists = models.PlatFormBilibili.objects.filter(
                            openid=openid
                        ).exists()
                        if exists:
                            models.PlatFormBilibili.objects.filter(
                                openid=openid
                            ).update(**row_object)
                        else:
                            row_object["openid"] = openid
                            models.PlatFormBilibili.objects.create(**row_object)

                    else:
                        mes = user_info_result.get("message")
                        print(mes)

                else:
                    mes = access_token_result.get("message")
                    print(mes)

    return redirect("/account/auth/list/")


def account_auth_baijiahao(request):
    """账号授权百家号"""

    # 获取当前登陆的用户uid
    uid = request.session.get("info").get("uid")

    if request.method == "POST":
        bduss = request.POST.get("bduss")
        token = request.POST.get("token")
        bjhstoken = request.POST.get("bjhstoken")
        cookies = {"BDUSS": bduss}
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "token": token,
        }
        response = requests.get(
            "https://baijiahao.baidu.com/builder/app/appinfo",
            cookies=cookies,
            headers=headers,
        )
        result = response.json()
        errno = result.get("errno")
        if errno != 0:
            return HttpResponse("BDUSS 或 token 错误")
        nickname = result["data"]["user"]["name"]
        avatar = result["data"]["user"]["avatar"].replace("//", "https://")
        auth_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expires_time = (datetime.now() + timedelta(days=60)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        app_id = result["data"]["user"]["app_id"]

        user_info_dict = {
            "nickname": nickname,
            "avatar": avatar,
            "expires_time": expires_time,
            "auth_time": auth_time,
            "uid_id": uid,
            "bduss": bduss,
            "token": token,
            "bjhstoken": bjhstoken,
        }
        exists = models.PlatFormBaiJiaHao.objects.filter(app_id=app_id).exists()
        if exists:
            models.PlatFormBaiJiaHao.objects.filter(app_id=app_id).update(
                **user_info_dict
            )
        else:
            user_info_dict["app_id"] = app_id
            models.PlatFormBaiJiaHao.objects.create(**user_info_dict)

        return redirect("/account/auth/list/")


def account_auth_get(request):
    """获取授权账号表格数据"""

    # 获取当前登陆的用户uid
    uid = request.session.get("info").get("uid")

    row_id = 0
    data = {"total": 0, "rows": []}

    queryset_dy = models.PlatFormDouYin.objects.filter(uid=uid)
    for index, item in enumerate(queryset_dy):
        data["total"] += index
        row_id += 1
        content = {
            "id": row_id,
            "platform": "抖音",
            "nickname": item.nickname,
            "avatar": item.avatar,
            "auth_time": item.auth_time,
            "expires_time": item.expires_in,
            "status": item.expires_in > datetime.now(),
            "open_id": item.open_id,
        }

        data["rows"].append(content)

    queryset_bz = models.PlatFormBilibili.objects.filter(uid=uid)
    for index, item in enumerate(queryset_bz):
        data["total"] += index
        row_id += 1
        content = {
            "id": row_id,
            "platform": "哔哩哔哩",
            "nickname": item.nickname,
            "avatar": item.avatar,
            "auth_time": item.auth_time,
            "expires_time": item.expires_in,
            "status": item.expires_in > datetime.now(),
            "openid": item.openid,
        }

        data["rows"].append(content)

    queryset_zh = models.PlatFormZhiHu.objects.filter(uid=uid)
    for index, item in enumerate(queryset_zh):
        data["total"] += index
        row_id += 1

        content = {
            "id": row_id,
            "platform": "知乎",
            "nickname": item.nickname,
            "avatar": item.avatar,
            "auth_time": item.auth_time,
            "expires_time": item.expires_time,
            "status": item.expires_time > datetime.now(),
            "zh_uid": item.zh_uid,
        }

        data["rows"].append(content)

    queryset_bjh = models.PlatFormBaiJiaHao.objects.filter(uid=uid)
    for index, item in enumerate(queryset_bjh):
        data["total"] += index
        row_id += 1

        content = {
            "id": row_id,
            "platform": "百家号",
            "nickname": item.nickname,
            "avatar": item.avatar,
            "auth_time": item.auth_time,
            "expires_time": item.expires_time,
            "status": item.expires_time > datetime.now(),
            "app_id": item.app_id,
        }

        data["rows"].append(content)

    return JsonResponse(data)


def account_delete(request):
    """删除授权账号"""

    delete_id = request.GET.get("delete_id")

    dy_query = Q(open_id=delete_id)
    zh_query = Q(zh_uid=delete_id)
    bjh_query = Q(app_id=delete_id)
    bz_query = Q(openid=delete_id)

    # 利用 Q 对象，可以在一个查询中检查多个条件
    exists_dy = models.PlatFormDouYin.objects.filter(dy_query).exists()
    exists_zh = models.PlatFormZhiHu.objects.filter(zh_query).exists()
    exists_bjh = models.PlatFormBaiJiaHao.objects.filter(bjh_query).exists()
    exists_bz = models.PlatFormBilibili.objects.filter(bz_query).exists()

    if exists_dy:
        models.PlatFormDouYin.objects.filter(dy_query).delete()
        return JsonResponse({"status": True})
    elif exists_zh:
        models.PlatFormZhiHu.objects.filter(zh_query).delete()
        return JsonResponse({"status": True})
    elif exists_bjh:
        models.PlatFormBaiJiaHao.objects.filter(bjh_query).delete()
        return JsonResponse({"status": True})
    elif exists_bz:
        models.PlatFormBilibili.objects.filter(bz_query).delete()
        return JsonResponse({"status": True})

    return JsonResponse({"status": False})


def account_data_list(request):
    """数据展示"""

    # 前端选中标签
    active_account_data = ""
    header_label = ""
    if request.path == "/account/data/list/":
        active_account_data = "active"
        header_label = "数据展示"

    context = {"active_account_data": active_account_data, "header_label": header_label}
    return render(request, "account_data_list.html", context)


def account_data_get(request):
    """获取授权账号数据表格数据"""

    # 获取当前登陆的用户uid
    uid = request.session.get("info").get("uid")

    row_id = 0
    data = {"total": 0, "rows": []}

    # 抖音数据发送到前端
    queryset = models.PlatFormData.objects.filter(uid=uid)
    for index, item in enumerate(queryset):
        row_id += 1
        data["total"] += index
        content = {
            "id": row_id,
            "platform": item.platform,
            "nickname": item.nickname,
            "type": item.type,
            "create_time": item.create_time,
            "title": item.title,
            "update_time": item.update_time,
            "like_count": item.like_count,
            "comment_count": item.comment_count,
            "play_count": item.play_count,
            "download_rec_count": item.download_rec_count,
            "share_vote_count": item.share_vote_count,
            "forward_collect_count": item.forward_collect_count,
            "share_url": item.share_url,
        }
        data["rows"].append(content)

    return JsonResponse(data)


def account_data_update(request):
    """更新数据到数据库"""

    # 获取当前用户ID
    uid = request.session.get("info").get("uid")

    gd = GetData()

    dy_param = []
    dy_queryset = models.PlatFormDouYin.objects.filter(uid=uid)
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
    bz_queryset = models.PlatFormBilibili.objects.filter(uid=uid)
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
    zh_queryset = models.PlatFormZhiHu.objects.filter(uid=uid)
    for item in zh_queryset:
        z_c0 = item.z_c0
        zh_uid = item.zh_uid
        nickname = item.nickname
        uid = item.uid
        zh_param.append(
            {"nickname": nickname, "z_c0": z_c0, "zh_uid": zh_uid, "uid": uid}
        )

    bjh_param = []
    bjh_queryset = models.PlatFormBaiJiaHao.objects.filter(uid=uid)
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

    for param in dy_param:
        gd.get_douyin_data(
            param["nickname"], param["open_id"], param["access_token"], param["uid"]
        )
    for param in bz_param:
        gd.get_bilibili_data(
            param["nickname"], param["access_token"], param["openid"], param["uid"]
        )
    for param in zh_param:
        gd.get_zhihu_data(
            param["nickname"], param["z_c0"], param["zh_uid"], param["uid"]
        )
    for param in bjh_param:
        gd.get_baijiahao_data(
            param["nickname"],
            param["bjhstoken"],
            param["bduss"],
            param["token"],
            param["app_id"],
            param["uid"],
        )

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

    return JsonResponse({"status": True})


def account_auth_refresh(request):
    """刷新refresh_token"""

    refresh_id = request.GET.get("refresh_id")

    exists_zh = models.PlatFormZhiHu.objects.filter(zh_uid=refresh_id).exists()
    if exists_zh:
        data = {
            "status": False,
            "data": {"stats": "刷新失败", "tips": "知乎账号刷新无效，如已过期，请删除后重新授权"},
        }
        return JsonResponse(data)

    exists_bjh = models.PlatFormBaiJiaHao.objects.filter(app_id=refresh_id).exists()
    if exists_bjh:
        data = {
            "status": False,
            "data": {"stats": "刷新失败", "tips": "百家号账号刷新无效，如已过期，请删除后重新授权"},
        }
        return JsonResponse(data)

    exists_dy = models.PlatFormDouYin.objects.filter(open_id=refresh_id).exists()
    if exists_dy:
        row_object = models.PlatFormDouYin.objects.filter(open_id=refresh_id).first()
        rft_data = {
            "refresh_token": row_object.refresh_token,
            "client_key": "awpswfd65m22r59e",
        }
        rft_response = requests.post(
            "https://open.douyin.com/oauth/renew_refresh_token/", data=rft_data
        )
        rft_response_data = rft_response.json().get("data", "")
        rft_response_message = rft_response.json().get("message", "")

        if rft_response_message == "success":
            models.PlatFormDouYin.objects.filter(open_id=refresh_id).update(
                refresh_token=rft_response_data.get("refresh_token")
            )
            act_data = {
                "client_key": "awpswfd65m22r59e",
                "grant_type": "refresh_token",
                "refresh_token": rft_response_data.get("refresh_token"),
            }
            act_response = requests.post(
                "https://open.douyin.com/oauth/refresh_token/", data=act_data
            )
            act_response_data = act_response.json().get("data", "")
            act_response_message = act_response.json().get("message")

            if act_response_message:
                access_token = act_response_data["access_token"]
                expires_in = act_response_data["expires_in"]
                expires_time = datetime.now() + timedelta(seconds=expires_in)
                expires_time = datetime.strftime(expires_time, "%Y-%m-%d %H:%M:%S")

                models.PlatFormDouYin.objects.filter(open_id=refresh_id).update(
                    access_token=access_token, expires_in=expires_time
                )
                nickname = (
                    models.PlatFormDouYin.objects.filter(open_id=refresh_id)
                    .first()
                    .nickname
                )
                data = {
                    "status": True,
                    "data": {"stats": "刷新成功", "tips": f"{nickname}将在{expires_time}后过期"},
                }
                return JsonResponse(data)

        data = {
            "status": False,
            "data": {"stats": "刷新失败", "tips": "refresh_token过期，请删除授权账号重新授权"},
        }
        return JsonResponse(data)

    exists_bz = models.PlatFormBilibili.objects.filter(openid=refresh_id).exists()
    if exists_bz:
        row_object = models.PlatFormBilibili.objects.filter(openid=refresh_id).first()
        rft_data = {
            "refresh_token": row_object.refresh_token,
            "client_id": "302763bae0404eee",
            "client_secret": "aef73864a09a42bcbe1bbec8130ee5ed",
            "grant_type": "refresh_token",
        }
        rft_response = requests.post(
            "https://api.bilibili.com/x/account-oauth2/v1/refresh_token", data=rft_data
        )
        rft_response_data = rft_response.json().get("data", "")
        rft_response_code = rft_response.json().get("code", "")

        if rft_response_code == 0:
            models.PlatFormBilibili.objects.filter(openid=refresh_id).update(
                refresh_token=rft_response_data.get("refresh_token"),
                access_token=rft_response_data.get("access_token"),
                expires_in=datetime.utcfromtimestamp(
                    rft_response_data.get("expires_in")
                ).strftime("%Y-%m-%d %H:%M:%S"),
            )
            nickname = (
                models.PlatFormBilibili.objects.filter(openid=refresh_id)
                .first()
                .nickname
            )
            expires_time = (
                models.PlatFormBilibili.objects.filter(openid=refresh_id)
                .first()
                .expires_in
            )
            data = {
                "status": True,
                "data": {"stats": "刷新成功", "tips": f"{nickname}将在{expires_time}后过期"},
            }
            return JsonResponse(data)

    data = {
        "status": False,
        "data": {"stats": "刷新失败", "tips": "refresh_token过期，请删除授权账号重新授权"},
    }
    return JsonResponse(data)


def account_auth_detail(request):
    """授权账号详情"""

    # 前端选中标签与头部标签
    active_account_auth = "active" if request.path == "/account/auth/detail/" else ""

    # 获取当前用户ID与当前平台账号 ID
    uid = request.session.get("info").get("uid")
    platform_uid = request.GET.get("platformid", "")
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
            .filter(platform_uid=platform_uid)
            .aggregate(Sum(field))
        )
        data_dict.update(queryset)

    # 修改头部平台名称+账号昵称
    platform_info = models.PlatFormData.objects.filter(
        platform_uid=platform_uid
    ).first()
    nickname = platform_info.nickname
    platform = platform_info.platform
    platform_mapping = {
        1: "抖音",
        2: "知乎",
        3: "百家号",
        4: "哔哩哔哩",
    }
    platform_name = platform_mapping.get(platform, "")
    header_label = f"{platform_name}-{nickname}"

    context = {
        "platform_uid": platform_uid,
        "active_account_auth": active_account_auth,
        "header_label": header_label,
        "data": data_dict,
    }

    return render(request, "account_auth_detail.html", context)


def account_auth_detail_echarts(request):
    """账号详情图表"""
    # 获取当前用户ID与当前平台账号 ID
    uid = request.session.get("info", {}).get("uid")
    platform_uid = request.GET.get("platform_uid", "")

    # 获取指定平台的历史数据
    queryset = models.HistoryDate.objects.filter(uid=uid, platform_uid=platform_uid)

    # 提取日期和指标列表
    date = queryset.values_list("date", flat=True)
    metrics = [
        "like_sum",
        "comment_sum",
        "play_sum",
        "download_rec_sum",
        "share_vote_sum",
        "forward_collect_sum",
    ]

    # 初始化空的 series_dict
    series_dict = {
        metric: list(queryset.values_list(metric, flat=True)) for metric in metrics
    }

    backend_data = {
        "categories": [i.strftime("%Y-%m-%d") for i in date],
        "seriesData": series_dict,
    }

    return JsonResponse({"status": True, "backendData": backend_data})
