import pandas as pd
from sklearn.preprocessing import MinMaxScaler
pd.options.mode.chained_assignment = None  # default='warn'

def process_data(df, is_play_data, is_platform_data, platform_name):
	"""处理数据"""
	df["platform"] = df["platform"].replace(platform_name)
	if is_play_data:
		group_by_cols = ["platform"] if is_platform_data else ["nickname", "platform"]
		data_df = df[["play_count"] + group_by_cols].groupby(group_by_cols).sum().reset_index()
		if not is_platform_data:
			data_df["nickname"] = data_df["platform"].astype(str) + "-" + data_df["nickname"].astype(str)
	else:
		group_by_cols = ["platform"] if is_platform_data else ["nickname", "platform"]
		numeric_columns = ["like_count", "comment_count", "download_rec_count", "share_vote_count",
		                   "forward_collect_count"]
		data_df = df[group_by_cols + numeric_columns]
		scaler = MinMaxScaler()
		data_df[numeric_columns] = scaler.fit_transform(data_df[numeric_columns])
		data_df = data_df.groupby(group_by_cols).sum().reset_index()
		data_df['interaction'] = data_df[numeric_columns].sum(axis=1)

	return data_df


def statistics(queryset, is_play_data, is_platform_data, platform_name):
	"""统计数据"""
	df = pd.DataFrame(queryset)
	processed_df = process_data(df, is_play_data, is_platform_data, platform_name)

	categories = processed_df["platform" if is_platform_data else "nickname"]
	values = processed_df["play_count" if is_play_data else "interaction"]

	data = [[category, round(value, 2)] for category, value in zip(categories, values)]

	return data
