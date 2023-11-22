import json

import requests
from datetime import datetime


def get_douyin_data(open_id: str, access_token: str) -> dict:
	"""
	（抖音开放平台）获取抖音视频数据字典
	:param open_id: PlatFormDouYin.open_id
	:param access_token: PlatFormDouYin.access_token
	:return: {
			"VideoList":[{str:str},{str:str},{str:str}],
			"avatar": str,
			"nickname":str
			}
	"""

	# 获取用户视频数据
	video_list = []
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
		video_list.append(result["data"]["list"])
		cursor = result["data"]["cursor"]
		has_more = result["data"]["has_more"]

	data = {"VideoList": [i for k in video_list for i in k]}

	return data
