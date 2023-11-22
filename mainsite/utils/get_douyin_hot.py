import requests
import json


def get_douyin_hot(open_id: str, access_token: str, keywords: str) -> dict:
	"""
	（抖音开放平台）获取抖音热搜
	:param keywords: request.POST.get("keywords")
	:param open_id: PlatFormDouYin.open_id
	:param access_token: PlatFormDouYin.access_token
	:return: {}
	"""

	# 获取热搜数据
	hot_list = []
	has_more = True
	cursor = 0
	count = 0
	while has_more and count < 5:
		headers = {
			"Content-Type": "application/json",
			"access-token": access_token
		}
		params = {
			'open_id': open_id,
			'cursor': cursor,
			'count': '10',
			'keyword': keywords,
		}
		response = requests.get('https://open.douyin.com/video/search/', params=params, headers=headers)
		result = response.json()
		print(result)
		hot_list.append(result["data"]["list"])
		cursor = result["data"]["cursor"]
		has_more = result["data"]["has_more"]
		count += 1

	data = {"list": [i for k in hot_list for i in k]}
	print(data)

	return data


if __name__ == '__main__':
	open_id = "_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn"
	access_token = "act.3.gGVD-9gEG9_QaBNWw9BR6EfHmSyMYd_DF15u_GNL5JYBOK4xWfbmWqIQyeqekwOxXjrqCA4IQCrhq3642aI5rL7I9qfmfNvD0yxN9e6dPb4eIbWE6oP5JJXXOwXmOylGbh5rHHSUAVPX9evKz0WEfvKPS506y3nV4hXUv-b04elzkoEnRxvuT99U_T8="
	keywords = "代理IP"
	data = get_douyin_hot(open_id, access_token, keywords)

	with open("/Users/chen/PycharmProjects/GrowthVision/temp_data.json", "w", encoding="utf8") as f:
		f.write(json.dumps(data, ensure_ascii=False))

# TODO
