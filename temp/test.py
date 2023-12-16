params_string = """
video_id=v0200fg10000clu1gnjc77u4eiia7htg
&video_width=1080
&video_height=1920
&video_cover_uri=tos-cn-p-0015%2FooEA8fydgB5xASzsINInBCAghiGK7vEvjVwAeg
&permission_sync_decouple=1
&new_sdk=1
&mixed_type=0
&duet_ignore_visibility=true
&download_ignore_visibility=true
&share_ignore_visibility=true
&is_diy_prop=0
&remove_background=0
&is_text_reading=0
&video_cnt=1
&pic_cnt=0
&is_multi_content=0
&music_edited_from=
&original=1
&tab_name=fast_shoot
&creation_id=add1e52a-e969-48df-a32e-c963f9ee914b
&location_permission=false
&entry_type=0
&speed=3
&activity_extra_json=%7B%22e_activity_user%22%3Afalse%7D
&camera=0
&prettify=2
&is_upload_audio_track=false
&is_multi_video_upload=false
&use_camera_type=1
&h264_high_profile=1
&tanning=0
&import_video_info=%5B%7B%22h%22%3A1280%2C%22w%22%3A720%2C%22b%22%3A0%2C%22e%22%3A-1%7D%5D
&music_begin_time=0
&music_end_time=6363
&image_album_music_info=%7B%22begin_time%22%3A0%2C%22end_time%22%3A0%2C%22volume%22%3A100%7D
&music_selected_from=original
&is_draft=0
&initial_privacy_status=public
&download_type=0
&item_duet=0
&comment_permission_status=0
&item_share=0
&is_text_mode=0
&groot_model_result=%7B%22allow_groot_research%22%3Atrue%2C%22detect_type%22%3A0%2C%22first_model_result%22%3Afalse%7D
&sticker_extra_info=%5B%5D
&category_da=0
&upload_info=%5B%5D
&cover_tsp=0.0
&misc_info=%7B%22green_screen%22%3A0%2C%22is_teen_video%22%3A0%2C%22koi_fish%22%3A0%2C%22video_tag%22%3A0%2C%22music_begin_time%22%3A%220%22%2C%22mv_type%22%3A0%2C%22original_gid_distance%22%3A1%2C%22original_group_id%22%3A%227275981014877424959%22%2C%22vpa_info%22%3A%7B%22show_info_bar_type%22%3A0%2C%22show_opt_out_button%22%3Afalse%7D%7D
&countdown_list=%5B0%5D
&is_music_looped=0
&text_fonts=
...
&create_scale_type=%5B%22f_h%22%5D
"""

# 解析参数值
decoded_data = {key: value for key, value in [param.split('=') for param in params_string.strip().split('&')]}

# 输出解析结果
print(decoded_data)
