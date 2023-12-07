import requests

headers = {
	# 'authority': 'www.douyin.com',
	# 'accept': 'application/json, text/plain, */*',
	# 'accept-language': 'zh-CN,zh;q=0.9',
	# 'cookie': 'ttwid=1%7CTWNmzCkWgT51QroS1rogq6cYUl7ln1xFfW1KP__U1mg%7C1699948003%7C095cd79a7cbd39d03e2a725380344fffcc6abb58ecb11e8e67223e87ed5d08e7; passport_csrf_token=d0c1258ea1307a586b0f66af4c731e5a; passport_csrf_token_default=d0c1258ea1307a586b0f66af4c731e5a; s_v_web_id=verify_loy15iyc_UcspcgJJ_xVaR_4I1z_A2n8_mQLxOxokDs9a; odin_tt=023ed788ea68c1dd53cfade0173c0de894ae3511430ec053e852a9f220e844cc2a4650eb08e4198f4558056f6993f7d4aac75b3c0df252904075d8c2df0de43d; dy_swidth=1920; dy_sheight=1080; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; bd_ticket_guard_client_web_domain=2; csrf_session_id=9111f38251342f7561a22d60a79e2008; strategyABtestKey=%221701760363.419%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; __ac_nonce=0656ed4cf005eb638dd9f; __ac_signature=_02B4Z6wo00f01IBU5TwAAIDDFIK-M0pKY0CAdOGAAEWABMGpVXtz.hSHKHgMsF30boCdKvb1ym9WHQe1SvZflwWTzC85wXYoYr5DrC4YNFmz5.RFUaaka8FMJFKeMuwbqJUZ5TDQ.vZMvOH935; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A300%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQWFrb1NxNzg1dDNhcndyNStEQUM1UEc3elM3VkppRTNYcGpRMkwyU2ppTDlGTk9rb1hJWC9LcjcvbTFCM3Rsc2wrYSt3WVNsUGNLUVlSSmhkY3dlMnM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; SEARCH_RESULT_LIST_TYPE=%22single%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; msToken=5qtTwo3IbAvBO6XCQ38IIIZ3OUsIZsiO5_AgYB1IF1mR8_NQBKcsA7br8qmoR7G9soJyTenJH19OtNovlslk3lECB74VefqmGLzYntMZ_WOdVx21tkWMGBF-KeM=; tt_scid=Qlkh9rzSzxgOT-nHrPpkoXAJ4-BOML7RNhV81Lxc5Ddu8a3h9MpA.c4f64u3-pMZ9704; download_guide=%221%2F20231205%2F0%22; msToken=JYzePcoJn9d5CSs13xaI4qYVDVL3gayMF_8kJQuMT8plZSbU6KL_Iol1dnBZXlwXPfcAsgfUZxQtorpegYoWzrRSiXz_x_H7C-MDmHidyMsjzR3KXII86uVea9Y=',
	'referer': 'https://www.douyin.com/search/',
	# 'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	# 'sec-ch-ua-mobile': '?0',
	# 'sec-ch-ua-platform': '"macOS"',
	# 'sec-fetch-dest': 'empty',
	# 'sec-fetch-mode': 'cors',
	# 'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

response = requests.get(
	'https://www.douyin.com/aweme/v1/web/general/search/single/?aid=6383&keyword=%E4%BB%A3%E7%90%86ip&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=10&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=104.0.0.0&browser_online=true&engine_name=Blink&engine_version=104.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=250&webid=7301221014381348352&msToken=JYzePcoJn9d5CSs13xaI4qYVDVL3gayMF_8kJQuMT8plZSbU6KL_Iol1dnBZXlwXPfcAsgfUZxQtorpegYoWzrRSiXz_x_H7C-MDmHidyMsjzR3KXII86uVea9Y=',
	headers=headers,
)
result = response.json()
print(result)

