import requests
from datetime import datetime
from mainsite import models
from django.utils import timezone


class GetData:
	works_list = []

	def get_douyin_data(self, nickname: str, open_id: str, access_token: str, uid: int):
		"""（抖音开放平台）获取抖音视频数据"""

		# 获取用户视频数据
		has_more = True
		cursor = 0
		while has_more:
			headers = {
				'access-token': access_token,
			}
			params = {
				'open_id': open_id,
				'cursor': cursor,
				'count': '10',
			}
			response = requests.get('https://open.douyin.com/api/douyin/v1/video/video_list/', params=params,
			                        headers=headers)
			result = response.json()
			error_code = result["data"]["error_code"]

			if error_code != 0:
				models.PlatFormDouYin.objects.filter(open_id=open_id).update(expires_in=timezone.now())
				return

			cursor = result["data"]["cursor"]
			has_more = result["data"]["has_more"]
			for item in result["data"]["list"]:
				media_type = item.get("media_type", "")
				if not media_type:
					continue
				itme_type = "视频" if media_type == 4 else "文图"
				works_dict = {
					"platform": 1,
					"uid": uid,
					"nickname": nickname,
					"platform_uid": open_id,
					"item_id": item["item_id"],
					"title": item["title"],
					"type": itme_type,
					"create_time": datetime.fromtimestamp(item["create_time"]).strftime("%Y-%m-%d %H:%M:%S"),
					"update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
					"share_url": item["share_url"],
					"like_count": item["statistics"]["digg_count"],
					"comment_count": item["statistics"]["comment_count"],
					"play_count": item["statistics"]["play_count"],
					"download_rec_count": item["statistics"]["download_count"],
					"share_vote_count": item["statistics"]["share_count"],
					"forward_collect_count": item["statistics"]["forward_count"],
				}
				self.works_list.append(works_dict)

	def get_zhihu_data(self, nickname: str, z_c0: str, zh_uid: str, uid: int):
		"""获取知乎授权账号的作品数据"""

		cookies = {"z_c0": z_c0}
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}

		url = "https://www.zhihu.com/api/v4/creators/creations/v2/all?end=0&limit=20&need_co_creation=1&offset=0&sort_type=created&start=0"
		is_end = False

		while not is_end:
			response = requests.get(url, cookies=cookies, headers=headers)
			result = response.json()
			url = result["paging"]["next"]
			is_end = result["paging"]["is_end"]
			for item in result["data"]:
				if item["type"] == "pin":
					continue
				if item["type"] == "article":
					works_dict = {
						"platform": 2,
						'uid': uid,
						"platform_uid": zh_uid,
						"nickname": nickname,
						"item_id": item["data"]["id"],
						"title": item["data"]["title"],
						"type": "文章",
						"create_time": datetime.fromtimestamp(item["data"]["created_time"]).strftime(
							"%Y-%m-%d %H:%M:%S"),
						"update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
						"share_url": f"https://zhuanlan.zhihu.com/p/{item['data']['id']}",
						"like_count": item["reaction"]["like_count"],
						"comment_count": item["reaction"]["comment_count"],
						"play_count": item["reaction"]["read_count"],
						"download_rec_count": item["reaction"]["reviewing_comment_count"],
						"share_vote_count": item["reaction"]["vote_up_count"],
						"forward_collect_count": item["reaction"]["collect_count"],
					}
					self.works_list.append(works_dict)
				if item["type"] == "zvideo":
					works_dict = {
						"platform": 2,
						'uid': uid,
						"platform_uid": zh_uid,
						"nickname": nickname,
						"item_id": item["data"]["id"],
						"title": item["data"]["title"],
						"type": "视频",
						"create_time": datetime.fromtimestamp(item["data"]["created_time"]).strftime(
							"%Y-%m-%d %H:%M:%S"),
						"update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
						"share_url": f"https://zhuanlan.zhihu.com/p/{item['data']['id']}",
						"like_count": item["reaction"]["like_count"],
						"comment_count": item["reaction"]["comment_count"],
						"play_count": item["reaction"]["play_count"],
						"download_rec_count": item["reaction"]["reviewing_comment_count"],
						"share_vote_count": item["reaction"]["vote_up_count"],
						"forward_collect_count": item["reaction"]["collect_count"],
					}
					self.works_list.append(works_dict)

	def get_baijiahao_data(self, nickname: str, bjhstoken: str, bduss: str, token: str, app_id: str, uid: int):
		"""获取百家号授权账号的作品数据"""
		cookies = {'bjhStoken': bjhstoken, 'BDUSS': bduss}
		headers = {
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
			"token": token,
			"Referer": "https://baijiahao.baidu.com/builder/rc/content?currentPage=1&search=&pageSize=10&type=&collection=",
			"Accept": "application/json, text/plain, */*"
		}

		params = {
			'currentPage': '1',
			'pageSize': '10',
			'search': '',
			'type': '',
			'collection': '',
			'app_id': app_id,
		}

		response = requests.get('https://baijiahao.baidu.com/pcui/article/lists', params=params, cookies=cookies,
		                        headers=headers)
		result = response.json()
		totalPage = result["data"]["page"]["totalPage"]
		for i in range(totalPage):
			params = {
				'currentPage': i + 1,
				'pageSize': '10',
				'search': '',
				'type': '',
				'collection': '',
				'app_id': app_id,
			}
			# if params["currentPage"] > 10:
			# 	break
			result = requests.get('https://baijiahao.baidu.com/pcui/article/lists', params=params, cookies=cookies,
			                      headers=headers).json()
			data_list = result["data"]["list"]
			# print(data_list)
			for item in data_list:
				if item["type"] == "image_text":
					continue
				works_dict = {
					"platform": 3,
					'uid': uid,
					"nickname": nickname,
					"platform_uid": app_id,
					"item_id": item["id"],
					"title": item["title"],
					"type": item["type"],
					"create_time": item.get("publish_time", "2022-12-14 14:08:58"),
					"update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
					"share_url": item.get("share_url", ""),
					"like_count": item.get("like_amount", 0),
					"comment_count": item.get("comment_amount", 0),
					"play_count": item.get("read_amount", 0),
					"download_rec_count": item.get("rec_amount", 0),
					"share_vote_count": item.get("share_amount", 0),
					"forward_collect_count": item.get("collection_amount", 0),
				}

				self.works_list.append(works_dict)

	def get_bilibili_data(self, nickname: str, access_token: str, openid: str, uid: int):
		"""获取哔哩哔哩视频数据"""

		has_next = True
		pn = 1  # 当前页
		ps = 10  # 单页数量
		while has_next:
			video_list_url = "https://member.bilibili.com/arcopen/fn/archive/viewlist"
			video_list_param = {
				"client_id": "302763bae0404eee",
				"access_token": access_token,
				"pn": pn,
				"ps": ps,
			}
			video_list_response = requests.get(url=video_list_url, params=video_list_param)
			video_list_result = video_list_response.json()
			code = video_list_result.get("code")
			if code != 0:
				break

			video_list = video_list_result["data"]["list"]
			for item in video_list:
				resource_id = item["resource_id"]
				title = item["title"]
				share_url = item["video_info"]["share_url"]

				video_detail_url = "https://member.bilibili.com/arcopen/fn/data/arc/stat"
				video_detail_param = {
					"client_id": "302763bae0404eee",
					"access_token": access_token,
					"resource_id": resource_id
				}
				video_detail_response = requests.get(url=video_detail_url, params=video_detail_param)
				video_detail_result = video_detail_response.json()
				create_time = datetime.utcfromtimestamp(video_detail_result["data"]["ptime"]).strftime(
					"%Y-%m-%d %H:%M:%S")
				works_dict = {
					"platform": 4,
					'uid': uid,
					"item_id": resource_id,
					"title": title,
					"type": "视频",
					"create_time": create_time,
					"update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
					"platform_uid": openid,
					"nickname": nickname,
					"like_count": video_detail_result["data"]["like"],
					"comment_count": video_detail_result["data"]["reply"],
					"play_count": video_detail_result["data"]["view"],
					"download_rec_count": video_detail_result["data"]["danmaku"],
					"share_vote_count": video_detail_result["data"]["coin"],
					"forward_collect_count": video_detail_result["data"]["favorite"],
					"share_url": share_url
				}

				self.works_list.append(works_dict)

			total = video_list_result["data"]["page"]["total"]
			pn = video_list_result["data"]["page"]["pn"]
			ps = video_list_result["data"]["page"]["ps"]
			has_next = total > (pn * ps)
			pn += 1


if __name__ == '__main__':
	gd = GetData()
	# open_id = "_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn"
	# access_token = "act.3.XA3TRzjQyBGa2nn8ntS0hu32E630_Pcj0t5ltUOdOYLRxSYGaZQjMdgBQH6wsSnXTIvurbqwcWptsPAqbbrUmkiSuFk-dOJCFqEurbEL7o_a2zvXXfS8ZX18CT4eJ8uWLxfyGTGDZVhj0IaYp7hKO8qQjRd9UAu0PinGVIk-mvLOvczcKHs-Lpzp0zM="
	# gd.get_douyin_data("123", open_id, access_token)
	# print("抖音完成")
	# z_c0 = "2|1:0|10:1700625594|4:z_c0|92:Mi4xZV9oV1NnQUFBQUFCd05HUjhqaTRGeVlBQUFCZ0FsVk51TXBLWmdCWmdDZ0loX3FjSF9raVk1V3l6MnliWlA3VGFB|5a7fa50c76250f3ad96ea2d53ebc71ae5303a2137331e799dd53cca0b2f4a177"
	# zh_uid = "1fdef83551b8a7f4190a7fc9c5f9aa6e"
	# gd.get_zhihu_data("123", z_c0, zh_uid)
	# print("知乎完成")
	# bjhStoken = "28cf132b30584c155a19150166fe3236872e822c081dac367603da878126a2b5"
	# bduss = "HkyOVdvZm5RajVUZkg2N2lHcjNKZzJyblgxOXZMWUdSU0xHUlFOeEp2ZjJ2b3RsRUFBQUFBJCQAAAAAAQAAAAEAAADCNR4PyMu1xMP8yve1xNOwOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPYxZGX2MWRlO"
	# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iYWlqaWFoYW8uYmFpZHUuY29tIiwiYXVkIjoiaHR0cDpcL1wvYmFpamlhaGFvLmJhaWR1LmNvbSIsImlhdCI6MTcwMTA3NTUwNCwibmJmIjoxNzAxMDMyMzA5LCJleHAiOjE3MDExMTg3MDl9.Ip9Kt8jf-x16wi6Xeb8gXgOrlZRMJtqBl1y6CiVVlo4'
	# app_id = "1734231139480701"
	# gd.get_baijiahao_data("123", bjhStoken, bduss, token, app_id)
	# print("百家号完成")
	# with open("../../temp/integration.json", "w", encoding="utf-8") as f:
	# 	import json
	#
	# 	f.write(json.dumps(gd.works_list, ensure_ascii=False))

	# gd.get_bilibili_data("四叶天ip代理", "4a001d049fae724300e3278281aa5dc1", "9aa6e1e9fc0f47f6b2999d0e333e9291")
	# print(gd.works_list)

	gd.get_baijiahao_data("静态IP中屹",
	                      "b29b3898333835610e3b8b8cceff255799980547a41698a3c01703dd86df6cdd",
	                      "WpsRHBDTmJVejdTQWVMMGJ6cmRjaHM5aUlOUmJjejFXSG1qMm9ITnNrd0gtZFpsRUFBQUFBJCQAAAAAAQAAAAEAAAB0QoYEwsDQobGmc2VvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdsr2UHbK9le",
	                      "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iYWlqaWFoYW8uYmFpZHUuY29tIiwiYXVkIjoiaHR0cDpcL1wvYmFpamlhaGFvLmJhaWR1LmNvbSIsImlhdCI6MTcwNTk5NTMwMywibmJmIjoxNzA1OTUyMTA4LCJleHAiOjE3MDYwMzg1MDh9.APO_ZNmp4gyPKHqGloNAL-xM-QqJ6KnZFFW1kWbyI7w",
	                      "1724990340332265",
	                      202312097807)

	print(gd.works_list)
