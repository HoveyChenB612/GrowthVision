import json
from datetime import datetime
from typing import Optional, Union, Any

import requests


def searchDyRank(keyword: str) -> Optional[list[dict[str, Union[str, Any]]]]:
	"""
	根据关键词搜索抖音排行榜
	:param keyword: 关键词
	:return: 抖音排行榜列表
	"""
	url = f"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=0&publish_time=0&keyword={keyword}&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=30&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=98.0.4758.102&browser_online=true&engine_name=Blink&engine_version=98.0.4758.102&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7202027632111961656&msToken=HPG5Ui3bDa8yGs4cq5SLHr2jIcCZuQgskdjK5EhB09vmv_o8T6ARV4ib6Xbb69go-qU8GN6lRg0yzvJGyX3ec1rqAQhP-8NpXGJqms-di-B7aC3ccppR&X-Bogus=DFSzswVOZr0ANVGvSglHAN7Tlqt6"

	headers = {
		"cookie": "passport_csrf_token=050ea514c5f012d19870c80d54a503d9; passport_csrf_token_default=050ea514c5f012d19870c80d54a503d9; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jc3IiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLVxyXG5NSUlCRFRDQnRRSUJBREFuTVFzd0NRWURWUVFHRXdKRFRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxXHJcbllYSmtNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEQVFjRFFnQUVzVEp3TjI3d0tkdEVDVG0rSjFJSnNOT0VcclxuNlMzRERYdGM3SHJ0Y0tieTRmT0U2d3FFSmgzTEwvODJDdkJ3VVYxenJlTDFNYmFadWRNYzBNT0VJQnNDZGFBc1xyXG5NQ29HQ1NxR1NJYjNEUUVKRGpFZE1Cc3dHUVlEVlIwUkJCSXdFSUlPZDNkM0xtUnZkWGxwYmk1amIyMHdDZ1lJXHJcbktvWkl6ajBFQXdJRFJ3QXdSQUlnUHdCNkFZRkt3QjQzcDNZV3lSaHl4TUliSEZTeGlVS0lBQTloMWRUdk81Y0NcclxuSUc2R2t1ZnVNMkM5RS9VWS9ZMjFZb0tXbitWOTd6ZWVFVDQwKzBXYkdXb1NcclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; ttcid=aa03ff42d2e7448fbecad2e5adb5b7bf28; strategyABtestKey=%221676852758.978%22; s_v_web_id=verify_lec2u5ph_9zh8RuQj_tVLI_4QNa_AzrC_e4dDyJH9l3OU; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230220%22; douyin.com; csrf_session_id=972d0cfacb7f0cb7a05505c0de2cf94d; passport_assist_user=CkHtbpi5yDihhyHTWEzuHhitFSeIl7LtFMSIGHi6EwrHK5hw2qjVsMZLHf9BCexMqxOpB4PDwIhwcy8R5cUummy9hxpICjyjb_1PZ3qBxiDX_Nz3J-eGfu-sg0oyQsWe0MJoxHUuWlivl49824Y1cBo_sKeLDZR47OohhAlkCTpfRIsQouSpDRiJr9ZUIgEDpO_ucw%3D%3D; n_mh=FRGUtHUdWPZkFKTvg9qLFd45tV5O6njrOBEozt_g1Xo; sso_uid_tt=8683797c2a2aa6c284f673ce11587302; sso_uid_tt_ss=8683797c2a2aa6c284f673ce11587302; toutiao_sso_user=0a95f3175b1d83432b80161a7581081c; toutiao_sso_user_ss=0a95f3175b1d83432b80161a7581081c; sid_ucp_sso_v1=1.0.0-KDVjNjdlZTFhZmRhZDlhNTYyYTI3OTliMzE1YzE5YTg4NGYxNTcyYWYKHwi-x4C78IykBhDnmsyfBhjaFiAMMNj6wYMGOAZA9AcaAmxmIiAwYTk1ZjMxNzViMWQ4MzQzMmI4MDE2MWE3NTgxMDgxYw; ssid_ucp_sso_v1=1.0.0-KDVjNjdlZTFhZmRhZDlhNTYyYTI3OTliMzE1YzE5YTg4NGYxNTcyYWYKHwi-x4C78IykBhDnmsyfBhjaFiAMMNj6wYMGOAZA9AcaAmxmIiAwYTk1ZjMxNzViMWQ4MzQzMmI4MDE2MWE3NTgxMDgxYw; passport_auth_status=34ed5cf59334c7127b9a2148ae7edd54%2C; passport_auth_status_ss=34ed5cf59334c7127b9a2148ae7edd54%2C; uid_tt=66fd48b656b782288a8c1c1025fcabb0; uid_tt_ss=66fd48b656b782288a8c1c1025fcabb0; sid_tt=908535a7447915b39529742e5186c907; sessionid=908535a7447915b39529742e5186c907; sessionid_ss=908535a7447915b39529742e5186c907; store-region=cn-sd; store-region-src=uid; ttwid=1%7C46V897AmTkxw2INMnUSmfyoUzIjsPsyKn86kdGjiuc8%7C1676880361%7C7d5a93b85561b36c2a2bf9480836c7e6d704acacc4af2ba428786513bca47995; __ac_nonce=063f32cf900228a89a03e; __ac_signature=_02B4Z6wo00f01wS1YkgAAIDAkGM5Rqoda3MElWbAAKLoeONiP2H52enjUPK3Os7f4BCwFMBZJaHIDbPzJNJBnUNXxsxYixfinPuSgX.EhkC71iP7wc9hGgtsNVezBydonjsyMlwEX6cBDpwu41; odin_tt=5afbbb0452c8a3633c06997e77c9554b65adc0c3d010a1fcd2f952da36e1b0d9f5aefd541bc7345ceb349dd0ca06a990; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1677486975294%2C%22type%22%3A1%7D; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA-Pce_jRb-JZdmsgPZos3YJA8bbRAc2hY4TLK8GnHJPOOFqMMHEY_lCz1Vc1RfMUR%2F1676908800000%2F0%2F1676882180929%2F0%22; LOGIN_STATUS=1; sid_guard=908535a7447915b39529742e5186c907%7C1676882184%7C5174879%7CFri%2C+21-Apr-2023+06%3A04%3A23+GMT; sid_ucp_v1=1.0.0-KDcyZjZjYjA4N2EyNzk2NDZlOWI3OTQ1Nzg1OWUyZWEyYmVlMjgwOTYKGQi-x4C78IykBhCI4syfBhjaFiAMOAZA9AcaAmxxIiA5MDg1MzVhNzQ0NzkxNWIzOTUyOTc0MmU1MTg2YzkwNw; ssid_ucp_v1=1.0.0-KDcyZjZjYjA4N2EyNzk2NDZlOWI3OTQ1Nzg1OWUyZWEyYmVlMjgwOTYKGQi-x4C78IykBhCI4syfBhjaFiAMOAZA9AcaAmxxIiA5MDg1MzVhNzQ0NzkxNWIzOTUyOTc0MmU1MTg2YzkwNw; tt_scid=JU5kfMfpRd0tm7iHR-xa5xywvLxKp3gaENiqUaNIN6pHpdgcp6LYttU363FLJWap76f1; msToken=XpCu3OTNnb1fjptLdJi_eIaCV8HCmrqGVhLh5IgZRO_IKx1a0wMtL3LChSohft-BrA9gZurWzeLKa7VULSgrkBs0L3gmJz03jc7CTN0DBT1FejGbJjwt; msToken=HPG5Ui3bDa8yGs4cq5SLHr2jIcCZuQgskdjK5EhB09vmv_o8T6ARV4ib6Xbb69go-qU8GN6lRg0yzvJGyX3ec1rqAQhP-8NpXGJqms-di-B7aC3ccppR; passport_fe_beating_status=false; home_can_add_dy_2_desktop=%220%22",
		"pragma": "no-cache",
		"referer": "https://www.douyin.com/search/%E4%BB%A3%E7%90%86ip?source=normal_search&aid=f67c8cbf-f5ed-437b-8688-a42fcc7b8173&enter_from=recommend&focus_method=",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": '"macOS"',
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
	}
	res = requests.get(url=url, headers=headers)
	res_data = res.json().get("data")

	if not res_data:
		return None
	with open("temp.json", "w", encoding="utf-8") as f:
		f.write(json.dumps(res_data, ensure_ascii=False))

	rank_list = []
	for index, item in enumerate(res_data):
		avatar = item.get("aweme_info", {}).get("author", {}).get("avatar_medium", {}).get("url_list", [])
		avatar = avatar[0] if avatar else ""
		nickname = item.get("aweme_info", {}).get("author", {}).get("nickname", "")
		title = item.get("aweme_info", {}).get("desc", "")
		share_url = item.get("aweme_info", {}).get("share_info", {}).get("share_url", "")
		digg_count = item.get("aweme_info", {}).get("statistics", {}).get("digg_count", 0)
		comment_count = item.get("aweme_info", {}).get("statistics", {}).get("comment_count", 0)
		share_count = item.get("aweme_info", {}).get("statistics", {}).get("share_count", 0)
		collect_count = item.get("aweme_info", {}).get("statistics", {}).get("collect_count", 0)
		download_count = item.get("aweme_info", {}).get("statistics", {}).get("download_count", 0)
		create_time_timestamp = item.get("aweme_info", {}).get("create_time", 0)
		create_time_datetime = datetime.fromtimestamp(create_time_timestamp)
		create_time = create_time_datetime.strftime("%Y-%m-%d %H:%M:%S")
		data_dict = {
			"rank": index + 1,
			"avatar": avatar,
			"nickname": nickname,
			"title": title,
			"share_url": share_url,
			"digg_count": digg_count,
			"comment_count": comment_count,
			"share_count": share_count,
			"collect_count": collect_count,
			"download_count": download_count,
			"create_time": create_time, }
		rank_list.append(data_dict)
	return rank_list


if __name__ == '__main__':
	data = searchDyRank("代理IP")
	for i in data:
		print(i)
