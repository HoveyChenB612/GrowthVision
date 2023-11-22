import requests

cookies = {
	# "SUBMIT_0": "c23dab54-3273-4de8-a8cc-006aee325ae1",
	# 四叶天 "z_c0": "2|1:0|10:1700552777|4:z_c0|92:Mi4xZV9oV1NnQUFBQUFBVUpWSHFVbThGeVlBQUFCZ0FsVk5SNjVKWmdDMFhjc3djVVUzWG5vSllMQXlxUTJObUNodFln|d60243997d0da8ed6607781a8aadf0ff94bac98eafe2014b043ecae52f5366c9",
	"z_c0": "2|1:0|10:1700558819|4:z_c0|92:Mi4xTk9qZUFRQUFBQUFBb0JTVE9FeThGeVlBQUFCZ0FsVk40OFZKWmdDTVFFVEFVUHlCWVk1UTlfQ2p2NEtfUW1rdkl3|da8e4e19dfbbd9c23ad91eb724b36e0c67b68f81422ae7ac7bb4bc5cf7cc8c6a"
	# "__snaker__id": "elqF9lECqkr6eFdb",
	# "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1700020515,1700096531,1700458027,1700526500",
	# "_zap": "4879fa0b-408e-4ecc-89d6-e4116ae29b78",
	# "d_c0": "AFCVR6lJvBePTkPjOudW8arp3ASahZ674wU=|1700552767",
}

headers = {
	# 'Accept': '*/*',
	# 'Sec-Fetch-Site': 'same-origin',
	# 'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
	# # 'Accept-Encoding': 'gzip, deflate, br',
	# 'Sec-Fetch-Mode': 'cors',
	# 'Host': 'www.zhihu.com',
	# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
	# 'Referer': 'https://www.zhihu.com/creator/manage/creation/all',
	# 'Connection': 'keep-alive',
	# 'Cookie': 'KLBRSID=c450def82e5863a200934bb67541d696|1700551830|1700543243; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1700551820; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1700020515,1700096531,1700458027,1700526500; z_c0=2|1:0|10:1700551819|4:z_c0|92:Mi4xZV9oV1NnQUFBQUFBb05RRngwcVpGeVlBQUFCZ0FsVk5pcXBKWmdEc050R05lSDJNOVI0bnNBZVo1emhXMmx1c2xB|5dd803276d7d57d685373b8b3aa594e21449eac26a8b509abe579ea94a932dd7; captcha_session_v2=2|1:0|10:1700551803|18:captcha_session_v2|88:OXFCb1dQZHVtNnphUlJDU0RIUzAzV3pJNWphb2pXQzZocnE2SGpQVGJMdGN4Ym9uRzhybFdwTzdwbTN2dEVVVA==|6f6de83923c070feed7e0769488a6391f97c5e4cbd94e9dcf53954ba9e9653c4; JOID=VF0UAEqtflvrFWKdbKjKzZXcLQB8nU8cv1c24BTEGWykWRLpMUgjB4sRZZtsaBDARho1Z3FW355s6vKZYpowEhs=; SESSIONID=35EVEWyznd3MNwwY1OdsXGzBEwYjgRg61lBEG4TaCvY; osd=V1oSAEqueV3rFWGaaqjKzpLaLQB_mkkcv1Qx5hTEGmuiWRLqNk4jB4gWY5tsaxfGRho2YHdW351r7PKZYZ02Ehs=; SUBMIT_0=24249ddf-a408-4bf4-befa-d0880c1d2601; tst=r; gdxidpyhxdE=uTyRftSh%2FfN8BZt8QfmcqhKirmym39wLK1CeDYeQQsM4TUpujMV6V4rVQK%2BxIVDb4JDhDxtISuW9c7g0ZbOtEUzcWm9ZMlJat%2BrZS2ysOqj14nI6%2BGWSb3tiq5cBV%2FlZouVnEUI5cwpRD0GZc%2FaVeE4Mlh1Klo1MmD9hZ%2ByWCRjDeHpn%3A1700552214710; _ga=GA1.2.408011547.1700531823; _gid=GA1.2.188246395.1700531823; captcha_ticket_v2=2|1:0|10:1700529965|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfNm9GbWVCdlRud2tldVJvMTJzS2dBZlhzWXVRNTVXYVZXVENVajB2U29kWXhoTzhpcXBYR2RpbldrUS5BMDVONklISHNKa3VvR1lTY3JXb0QxVGZKUWZpM3BzSGtMU1ZXaFBROWVBRW5yOTRLSjRYNldJYng0NHR0UWtQZVkyaUY4TEZLa0pyYnJJX3JhKkthZ2VVdDZnY3J5V19iSUFtekN4MkRYQ3hHS1pDREpmdzFVUERGbUxYdUhyUjl1bmNfZDRrSnI4RUFERWpVNSpwRHNONWRfRHVoYjBwUVpxMWdSX0MqRE9zdU9IbGJsZzF0RXN5STNFcmpMQ19QNXBIRFZLRFVERml0Ul9xV251RlpUWVdXcW9WLnNReDN4RWFWVVBpd1BkZXF0SVNuaUQzTUpoTTBsZng2OFhxQmM2RXVoOUFua3REcjNzYmpic2JwLlhKb09seGtyOFFtOUZzZkpkakZCVFh4dXFaTipaak5BWnV4TENQY0c1ZUhjSGFGMVozSW8yLjZKVENfRWZxbFJ5NkVyLlVZUlYza0k0Lk1Zb2JFdUZwcmtTaC5kZ2VodzYqWV9fc1J6UV9jKkp0YnAqa2V4SHloYWxVX09jcUZoMTZZeEM2elljb2hqTEwqYypoTUtFUDBRWlFYZ1RiOEcyZmUqZ004ejhaKnBDb1RjUUkqTFg3N192X2lfMSJ9|db83ea00f1202d23f8a82a398428483133bfbf74d65737c9ae9a1dd63c45b0de; YD00517437729195%3AWM_TID=N8pdXvYr%2BWpEAVVFVROFzotWe%2FvpKG3T; YD00517437729195%3AWM_NI=EXr50%2F3NSlRl%2FxAVh8Mp2fN0LP%2FrfM5VfxxHtBAa8dOQzhUr50zQaD%2BQT0hLkpPN684wk%2BX3ZI5HoEad1eYI9yH3mp7xYUCYT9AU8admPVt1Uny%2B6Fh8QQUsVsvz4%2F5ANkY%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb6cf53b3ed98d0e64fb48e8eb3c45f968f9ab0c466edeee184db40a7a6adaae52af0fea7c3b92a8788bed6b325f1929d8dd168eda88fb7eb348fb0fe87cd3c9090e193e547f78aaa99fb44b89e8f82bb708d8fb689d87af7f0b6b2e450e98f9cd1eb48a9b0a0afb534f8a9a5ccdb399a97fba9ee4fa3bcff86dc43fba788d4f07cf5a897b6c25398e78fb6bb6ba8b3a0b7f73b97b2b7ccb54eace89fb2d87996adba9bb725f79f828cdc37e2a3; _xsrf=d2d1676f-859a-4e4f-9ddf-f165a7bc69bb; __snaker__id=9uBjcn3Wt7x2M7sA; q_c1=479c5351e7cd472da3ba53ade8aa158b|1698713098000|1698713098000; _zap=7a598e1e-35f7-4ace-88a9-b206f67167ea; d_c0=AKDUBcdKmRePTg6bXIlg1KHUzKlEq17ejSc=|1698204249',
	# 'Sec-Fetch-Dest': 'empty',
	# 'x-zse-96': '2.0_C6MnV2djAWSjhfnZ+OIFekbygOIH5uF5Z=XjTvJ6bw80TwWX0j6yWX/dj=qZVJF=',
	# 'x-requested-with': 'fetch',
	# 'x-zse-93': '101_3_3.0',
}

params = {
	'start': '0',
	'end': '0',
	'limit': '10',
	'offset': '0',
	'need_co_creation': '1',
	'sort_type': 'created',
}

# works_response = requests.get('https://www.zhihu.com/api/v4/creators/creations/v2/all', params=params, cookies=cookies,
                              # headers=headers)
me_response = requests.get("https://www.zhihu.com/api/v4/me", cookies=cookies)
result = me_response.json()
print(result)
