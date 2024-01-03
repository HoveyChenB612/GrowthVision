import typing
from time import sleep
import random
import json

from playwright.sync_api import Playwright, sync_playwright, TimeoutError
from playwright._impl._api_structures import Cookie
import requests


# def get_cookies(playwright: Playwright) -> typing.List[Cookie]:
#     headers = {
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#     }
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     context.set_extra_http_headers(headers=headers)
#     page = context.new_page()
#     page.goto("https://creator.douyin.com/")
#     page.get_by_text("登录").click()
#     # 使用 locator 定位到包含二维码图片的 div 元素
#     qrcode_div = page.locator(".qrcode-image")
#     # 使用 locator 定位到 div 元素下的 img 元素（这里使用 CSS 选择器）
#     img_element = qrcode_div.locator("img").first
#     # 获取 img 元素的 "src" 属性值
#     src_value = img_element.get_attribute("src")

#     # 等待页面重定向
#     page.wait_for_selector(".title--K_hSx", timeout=60000)
#     cookies = context.cookies()

#     context.close()
#     browser.close()

#     return cookies


def get_user_info(cookies: str):
	cookies_str = cookies
	cookies_json = json.loads(cookies_str)
	cookies_list = []
	for item in cookies_json:
		if "sameSite" in item.keys():
			del item["sameSite"]
			cookies_list.append(item)

	cookies = {cookie["name"]: cookie["value"] for cookie in cookies_json}

	headers = {
		"Host": "creator.douyin.com",
		"Sec-Fetch-Site": "same-origin",
		"Accept-Language": "zh-CN,zh-Hans;q=0.9",
		# 'x-secsdk-csrf-token': '000100000001287394e04f2a9db67b101ee221bd38ec2108c8aac8f7e28526914e40a7202e5217a34f8c27b42f04',
		"Sec-Fetch-Mode": "cors",
		"Accept": "application/json, text/plain, */*",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
		"Connection": "keep-alive",
		"Referer": "https://creator.douyin.com/creator-micro/home",
		"Sec-Fetch-Dest": "empty",
		# "Cookies": "_tea_utm_cache_2906=undefined; bd_ticket_guard_client_web_domain=2; ttcid=f97b8b486f604e1eb43fcb9bc699fc1f40; passport_csrf_token=a13778409b241b2393f1e06e500ee791; passport_csrf_token_default=a13778409b241b2393f1e06e500ee791; oc_login_type=LOGIN_PERSON; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; passport_assist_user=CkHmy08_ASrTWVtylwfpoXiA5iwaQU93LourUmQv-ia2W8TyG6j_Gu1pDNY-xfuGnbO16HHTJ9oOP_FcATwCpDds8hpKCjzxgZz0QbQXGTiaXXA8mX4FH4b1qFGkI8VHcvAUy2fdMSOA4W281l55XVHqgzE436rl9bvOLvenww82GvgQucnEDRiJr9ZUIAEiAQPRbC5z; n_mh=HTDyx66G3EEQCr_1y6y6Mc81KMqKD2aiLaOsNPRwclg; sso_uid_tt=2a5dd1bec5aac60951805a15d0e08c05; sso_uid_tt_ss=2a5dd1bec5aac60951805a15d0e08c05; toutiao_sso_user=55b97679632dcc871086ba171d0e2cd8; toutiao_sso_user_ss=55b97679632dcc871086ba171d0e2cd8; sid_ucp_sso_v1=1.0.0-KGY5MGQzYzYyYTRjMjljYjJkNDllZmYxZWJiOWViMDgyMTU2YmIwYzgKHwizy-Cm183gAxCBvpOsBhjaFiAMMMya3aYGOAZA9AcaAmxxIiA1NWI5NzY3OTYzMmRjYzg3MTA4NmJhMTcxZDBlMmNkOA; ssid_ucp_sso_v1=1.0.0-KGY5MGQzYzYyYTRjMjljYjJkNDllZmYxZWJiOWViMDgyMTU2YmIwYzgKHwizy-Cm183gAxCBvpOsBhjaFiAMMMya3aYGOAZA9AcaAmxxIiA1NWI5NzY3OTYzMmRjYzg3MTA4NmJhMTcxZDBlMmNkOA; odin_tt=1b3377d4761953c04bef4c7a44302a0b176a4b11c5d75ff6fcadafe0a0a5f1f0b8cc56342f54142c43d5c0b62447c5f092b3be0a2bb8961783e986c6daaa6c94; passport_auth_status=96007407d187436dc814344cf38b0c54%2Ce23c93ed5453d0a5a7b51fc988de5150; passport_auth_status_ss=96007407d187436dc814344cf38b0c54%2Ce23c93ed5453d0a5a7b51fc988de5150; uid_tt=79cf183a83e18e9fec59851f9549ce25; uid_tt_ss=79cf183a83e18e9fec59851f9549ce25; sid_tt=14b05fc14f202785747df36d9306eb34; sessionid=14b05fc14f202785747df36d9306eb34; sessionid_ss=14b05fc14f202785747df36d9306eb34; _bd_ticket_crypt_cookie=3aa169908163964dc11aaf6f706edb74; sid_guard=14b05fc14f202785747df36d9306eb34%7C1703206661%7C5183999%7CTue%2C+20-Feb-2024+00%3A57%3A40+GMT; sid_ucp_v1=1.0.0-KDYyMTY4YzFhNTg2ZGFmZTgyMThkM2YzNWM4NGMxMzM3OTA5NGZhZGUKGwizy-Cm183gAxCFvpOsBhjaFiAMOAZA9AdIBBoCaGwiIDE0YjA1ZmMxNGYyMDI3ODU3NDdkZjM2ZDkzMDZlYjM0; ssid_ucp_v1=1.0.0-KDYyMTY4YzFhNTg2ZGFmZTgyMThkM2YzNWM4NGMxMzM3OTA5NGZhZGUKGwizy-Cm183gAxCFvpOsBhjaFiAMOAZA9AdIBBoCaGwiIDE0YjA1ZmMxNGYyMDI3ODU3NDdkZjM2ZDkzMDZlYjM0; csrf_session_id=9111f38251342f7561a22d60a79e2008; s_v_web_id=lqhcun21_K36vInLQ_q48z_48Yd_BRvX_BecLFWJGjm5E; tt_scid=GZDYFTfC8dzEecgJwfBAmHBWopmXUyMKWwVGAzR9.wAOLkfsS.KUjcc.EDd6opOUc4c2; ttwid=1%7CyDxgaAuuWntIBsqopMN6q2XrCy8dOAWsDmEH9y9Ot1g%7C1703294223%7C4b8887e3c6bb1b0f79daae4f321567f0c408317942a2bbe480b7589602a668c2; passport_fe_beating_status=true; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSHdRYVpneE5wWmQ0Nk5UVUNSMXkzOUFPeWsxTDBSSklWRlV5ZkdoRTFpQ2NhVDliVDFZR2lIYmZIWk5HY3hyMy92YVNtb2pOelpsK0VXU1J3b2RHV2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=sCK-YcB_AjkOe9tlpNnXLX6QsmXUcPAtWg9HHlWPBtPAStawfhbTAvu0oZ00aJFH2x_4VWABMxdHu2cP6cfGCtJnT5odBE4AhYslrTv5Ai1RVtjurA==; msToken=GyhHMj9pY0l3gX3FBvH9W273Jw1HWRvQHRSROYC2YWEH8k_spR9Y8XY3Jvd_9biTyOiBB-C_I0NPtbbrei6RyQWW8kgrephBOBtytBhio1zCBLoYug==",
	}
	data = {"status": False, "code": 0, "mes": "", "data": {}}
	response = requests.get(
		"https://creator.douyin.com/aweme/v1/creator/user/info/",
		headers=headers,
		verify=False,
		cookies=cookies,
	)
	result = response.json()

	if result["status_code"] == 8:  # 'status_msg': '用户未登录'
		data["code"] = 0
		data["mes"] = "用户信息获取失败，cookies过期"
		return data

	nick_name = result.get("douyin_user_verify_info").get("nick_name")
	avatar_url = result.get("douyin_user_verify_info").get("avatar_url")
	douyin_unique_id = result.get("douyin_user_verify_info").get("douyin_unique_id")

	if nick_name or avatar_url or douyin_unique_id:
		user_info = {
			"nickname": nick_name,
			"avatar": avatar_url,
			"douyinid": douyin_unique_id,
			"cookies": cookies_json,
		}
		data["status"] = True
		data["code"] = 1
		data["mes"] = "用户信息获取成功"
		data["info"] = user_info
		return data

	data["mes"] = "用户信息获取失败，cookies过期"
	return data


def run(
		playwright: Playwright,
		cookies: typing.List[Cookie],
		file: str,
		title: str,
		target: list[str],
		content: str,
):
	headers = {
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
	}

	browser = playwright.chromium.launch(headless=False)
	context = browser.new_context()
	context.set_extra_http_headers(headers=headers)
	context.add_cookies(cookies)
	page = context.new_page()
	# try:
	page.goto("https://creator.douyin.com/creator-micro/content/upload")

	# 上传文件
	input_ele = page.locator("input[type=file]")
	input_ele.set_input_files(files=file)

	# 等待页面加载完成
	page.wait_for_selector("#root", timeout=30000, state="visible")

	# 填写内容
	# 1.标题
	page.get_by_placeholder("好的作品标题可获得更多浏览").click()
	page.get_by_placeholder("好的作品标题可获得更多浏览").type(title)
	sleep(random.uniform(1, 2))

	# 2. 作品简介
	page.locator(".zone-container").click()
	type_text = "\n ".join([f"#{item}" for item in target]) + "\n "
	page.locator(".zone-container").type(type_text + content)
	sleep(random.uniform(1, 2))
	# 等待视频上传完成
	page.wait_for_selector(".text--7Ii7o", timeout=60000, state="visible")

	# 发布
	page.get_by_role("button", name="发布", exact=True).click()
	sleep(random.uniform(1, 2))
	# 验证视频是否发布成功
	page.wait_for_selector(".search", timeout=60000, state="visible")

	for _ in range(3):
		text = page.locator(
			"xpath=//*[@id='root']/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div"
		).inner_text(timeout=3000)

		if title in text:
			return {"status": True, "mes": "发布成功", "code": 1}
		else:
			page.reload()
			sleep(random.uniform(1, 2))

	# except Exception as e:
	# 	print(e)
	# 	return {"status": False, "mes": "cookies 已过期，请重新授权", "code": 0}

	# finally:
	context.close()
	browser.close()

	return {"status": False, "mes": "发布失败", "code": 0}


def publish(cookies: typing.List[Cookie], file: str, title: str, target: list[str], content: str, ):
	with sync_playwright() as playwright:
		result = run(playwright, cookies, file, title, target, content)
		return result

# if "__main__" == __name__:
#     cookies_str = """
#     [{"domain":".creator.douyin.com","expirationDate":1703903297,"hostOnly":false,"httpOnly":false,"name":"_tea_utm_cache_2906","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"undefined"},{"domain":".douyin.com","expirationDate":1708482513.821999,"hostOnly":false,"httpOnly":false,"name":"bd_ticket_guard_client_web_domain","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"2"},{"domain":".douyin.com","expirationDate":1708482499.024206,"hostOnly":false,"httpOnly":false,"name":"passport_csrf_token","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"4540b3186feee1636539143f9076d032"},{"domain":".douyin.com","expirationDate":1708482499.024253,"hostOnly":false,"httpOnly":false,"name":"passport_csrf_token_default","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"4540b3186feee1636539143f9076d032"},{"domain":".douyin.com","expirationDate":1737858510.556954,"hostOnly":false,"httpOnly":false,"name":"passport_assist_user","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"CjzW6vsYs837wi6AffieSoqt0kqXBUCSa_17AUpBpsbh8GMUNydy-etiVDiXATlk6j0Wa1ULo4pmxdK6_cUaSgo85BllO8VReeJgMgvYcOuQyTajIl9h--Qz6K4jjeBYUk89LYlXDo5DNNOmn0QNmMHRdSr37OnS_HnNQMUXELzVxA0Yia_WVCABIgEDHC_M7w%3D%3D"},{"domain":".douyin.com","expirationDate":1713666510.557013,"hostOnly":false,"httpOnly":true,"name":"n_mh","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"baGxkkyow3sTab6X9aabmz60AaC7fG4cqc8O3UHkZcQ"},{"domain":".douyin.com","expirationDate":1708482510.557061,"hostOnly":false,"httpOnly":true,"name":"sso_uid_tt","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"4e42f8189630b123a4eef122569146ed"},{"domain":".douyin.com","expirationDate":1708482510.557108,"hostOnly":false,"httpOnly":true,"name":"sso_uid_tt_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"4e42f8189630b123a4eef122569146ed"},{"domain":".douyin.com","expirationDate":1708482510.557156,"hostOnly":false,"httpOnly":true,"name":"toutiao_sso_user","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"0f8e221f00e8fbb3a929bb44ef2fde47"},{"domain":".douyin.com","expirationDate":1708482510.557201,"hostOnly":false,"httpOnly":true,"name":"toutiao_sso_user_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"0f8e221f00e8fbb3a929bb44ef2fde47"},{"domain":".douyin.com","expirationDate":1708482510.557246,"hostOnly":false,"httpOnly":true,"name":"sid_ucp_sso_v1","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"1.0.0-KDc1NjQwZGEwNGRlNmJiM2ZiYjFkOGJmMzcyMThjMTdmM2RkNGMxMGIKHQjf1reChAIQzouZrAYY2hYgDDCBt4nOBTgGQPQHGgJscSIgMGY4ZTIyMWYwMGU4ZmJiM2E5MjliYjQ0ZWYyZmRlNDc"},{"domain":".douyin.com","expirationDate":1708482510.557294,"hostOnly":false,"httpOnly":true,"name":"ssid_ucp_sso_v1","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"1.0.0-KDc1NjQwZGEwNGRlNmJiM2ZiYjFkOGJmMzcyMThjMTdmM2RkNGMxMGIKHQjf1reChAIQzouZrAYY2hYgDDCBt4nOBTgGQPQHGgJscSIgMGY4ZTIyMWYwMGU4ZmJiM2E5MjliYjQ0ZWYyZmRlNDc"},{"domain":".douyin.com","expirationDate":1734834512.180337,"hostOnly":false,"httpOnly":true,"name":"odin_tt","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"00c5d7c387be1590f19b78673a38bb2c2f2af4c4e60e8da0902648f8b7e0feeaf5b50fc87ae086d565b42101e0b1c649"},{"domain":".douyin.com","expirationDate":1705890512.180493,"hostOnly":false,"httpOnly":true,"name":"passport_auth_status","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"feefc7c77cc4c6821254685174cf35db%2C"},{"domain":".douyin.com","expirationDate":1705890512.180522,"hostOnly":false,"httpOnly":true,"name":"passport_auth_status_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"feefc7c77cc4c6821254685174cf35db%2C"},{"domain":".douyin.com","expirationDate":1708482513.164464,"hostOnly":false,"httpOnly":true,"name":"uid_tt","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"bb78fa762462d337c903afe0c27b6bc4"},{"domain":".douyin.com","expirationDate":1708482513.164485,"hostOnly":false,"httpOnly":true,"name":"uid_tt_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"bb78fa762462d337c903afe0c27b6bc4"},{"domain":".douyin.com","expirationDate":1708482513.164504,"hostOnly":false,"httpOnly":true,"name":"sid_tt","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"515736b48793ac76475ee84ac4b35ebd"},{"domain":".douyin.com","expirationDate":1708482513.16454,"hostOnly":false,"httpOnly":true,"name":"sessionid","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"515736b48793ac76475ee84ac4b35ebd"},{"domain":".douyin.com","expirationDate":1708482513.164557,"hostOnly":false,"httpOnly":true,"name":"sessionid_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"515736b48793ac76475ee84ac4b35ebd"},{"domain":"creator.douyin.com","expirationDate":1737858512.86839,"hostOnly":true,"httpOnly":true,"name":"oc_login_type","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"LOGIN_PERSON"},{"domain":".douyin.com","expirationDate":1734834512.985185,"hostOnly":false,"httpOnly":true,"name":"ttwid","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"1%7CyDxgaAuuWntIBsqopMN6q2XrCy8dOAWsDmEH9y9Ot1g%7C1703298513%7C93edeaeff7928400e1070e5f219452661d306ef8b446f54a40ff5a2fb6eef07e"},{"domain":".douyin.com","expirationDate":1708482513.736045,"hostOnly":false,"httpOnly":false,"name":"_bd_ticket_crypt_doamin","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"2"},{"domain":".douyin.com","expirationDate":1708482513.778778,"hostOnly":false,"httpOnly":false,"name":"_bd_ticket_crypt_cookie","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"692804008524a2f10828df5adf16b070"},{"domain":".douyin.com","expirationDate":1708482513.788837,"hostOnly":false,"httpOnly":false,"name":"__security_server_data_status","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1"},{"domain":".douyin.com","expirationDate":1708482513.821869,"hostOnly":false,"httpOnly":false,"name":"bd_ticket_guard_client_data","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSHdRYVpneE5wWmQ0Nk5UVUNSMXkzOUFPeWsxTDBSSklWRlV5ZkdoRTFpQ2NhVDliVDFZR2lIYmZIWk5HY3hyMy92YVNtb2pOelpsK0VXU1J3b2RHV2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D"},{"domain":".douyin.com","expirationDate":1734402515.164422,"hostOnly":false,"httpOnly":true,"name":"sid_guard","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"515736b48793ac76475ee84ac4b35ebd%7C1703298515%7C5183998%7CWed%2C+21-Feb-2024+02%3A28%3A33+GMT"},{"domain":".douyin.com","expirationDate":1708482513.164574,"hostOnly":false,"httpOnly":true,"name":"sid_ucp_v1","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"1.0.0-KGMyZTk3MGI3ZDk2M2I2MTU2N2M0MWM2MGNlODg0ZTllOTdjYWQwMDcKGQjf1reChAIQ04uZrAYY2hYgDDgGQPQHSAQaAmhsIiA1MTU3MzZiNDg3OTNhYzc2NDc1ZWU4NGFjNGIzNWViZA"},{"domain":".douyin.com","expirationDate":1708482513.164618,"hostOnly":false,"httpOnly":true,"name":"ssid_ucp_v1","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"1.0.0-KGMyZTk3MGI3ZDk2M2I2MTU2N2M0MWM2MGNlODg0ZTllOTdjYWQwMDcKGQjf1reChAIQ04uZrAYY2hYgDDgGQPQHSAQaAmhsIiA1MTU3MzZiNDg3OTNhYzc2NDc1ZWU4NGFjNGIzNWViZA"},{"domain":"creator.douyin.com","expirationDate":1734834523,"hostOnly":true,"httpOnly":false,"name":"tt_scid","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"3gl5RrX.qJ8LyK35gUQDqJOBcwWPOcIo.dH5IdMQaPZQ52hEaW.TmBVkFhf2M1fy2fb3"},{"domain":"creator.douyin.com","expirationDate":1734837512,"hostOnly":true,"httpOnly":false,"name":"msToken","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"vqTJYQTwO0LExhY5a7nv3M4g3gNQ0mtwNJhM_QQMIoZccDqaO3PaXZSy5oBdJhfiEVgux2UL4DJCMTi0I6mOSidHAfRlHxusjh1Sgek19ctmZ8q3aw=="},{"domain":".creator.douyin.com","hostOnly":false,"httpOnly":false,"name":"passport_fe_beating_status","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"true"},{"domain":".douyin.com","expirationDate":1703907226.690655,"hostOnly":false,"httpOnly":false,"name":"msToken","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"65X1SIwlY97Y0RrHifGLl_bAu9dJQ0JtI3cw5fu6XedEKKV_7Fq0cKRJCzVKOt-phjjWrKtzQCvbPS8S2zJkkcxp7NpzdhabzltUj7NGzIW_61JdEQ=="}]
#     """
#     data = get_user_info(cookies_str)
#     cookies = data["data"]["cookies"]
#
#     with sync_playwright() as playwright:
#         # cookies = get_cookies(playwright)
#         file = "/Users/chen/PycharmProjects/GrowthVision/media/202311164511/IMG_0876.MOV"
#         title = "今天下雪了"
#         target = ["雪景", "超级大雪", "下雪啦"]
#         content = "好久没有见过这么大的雪了，真好"
#         result = publish(playwright, cookies, file, title, target, content)
#         print(result)
