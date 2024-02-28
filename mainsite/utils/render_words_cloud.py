import os
import pandas as pd


def process_word_cloud(user_path):
    df = pd.read_csv(user_path)
    df.drop("index", inplace=True, axis=1)
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    word_list = df['words'].tolist()
    word_df = pd.DataFrame(columns=["word", "play_count"])
    for index, word in enumerate(word_list):
        play_count = df.loc[index, "play_count"]
        words = word.split(",")
        for item in words:
            word_count = [[item, play_count]]
            new_word_df = pd.DataFrame(word_count, columns=["word", "play_count"])
            word_df = pd.concat([word_df, new_word_df], axis=0)
    result = word_df.groupby("word").sum().sort_values("play_count", ascending=False).iloc[0:200, :]
    return result


def render_words_cloud(role, user_list, uid, words_cloud_dir):
    data = []

    if role:
        for user in user_list:
            user_path = os.path.join(words_cloud_dir, str(user) + ".csv")
            result = process_word_cloud(user_path)
            # 遍历 DataFrame 中的每一行
            for index, row in result.iterrows():
                data.append({"name": index, "value": row.play_count})
    else:
        user_path = os.path.join(words_cloud_dir, str(uid) + ".csv")
        if not os.path.exists(user_path):
            return {"status": True, "data": data, "mes": "数据未更新"}
        result = process_word_cloud(user_path)
        # 遍历 DataFrame 中的每一行
        for index, row in result.iterrows():
            data.append({"name": index, "value": row.play_count})

    return {"status": True, "data": data, "mes": "数据获取成功"}
