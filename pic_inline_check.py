# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync
import tg_code

def tg_qd(tg_bot,tg_command):
    client.send_message(tg_bot, tg_command)  # 第一项是机器人ID，第二项是发送的文字
    time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
    messages = client.get_messages(tg_bot)
    time.sleep(2)
    messages[0].download_media(file="1.jpg")#下载验证码图片
    time.sleep(2)
    the_code = tg_code.truecaptcha()

    res = messages[0].click(text=the_code)#点击返回验证码
    time.sleep(1)
    if res == "None":#如果不存在这个验证码，就点第一个
        messages[0].click(0)
    time.sleep(5)
    messages = client.get_messages(tg_bot)
    return messages[0].message


api_id = [7047794]	#输入api_id，一个账号一项
api_hash = ['4648c6c14b86a7a90aa9e7b82f73e245']	#输入api_hash，一个账号一项
session_name = api_id[:]
bots_commands=["@JMSIPTV_bot","/checkin","成功"]
for num in range(len(api_id)):
	session_name[num] = "id_" + str(session_name[num])
	client = TelegramClient(session_name[num], api_id[num], api_hash[num])
	client.start()
	the_result=tg_qd(bots_commands[0],bots_commands[1])
	i=0
	while bots_commands[2] not in the_result:
	    i+=1
	    the_result=tg_qd(bots_commands[0],bots_commands[1])
	    if i > 5:#最多循环次数
	        break
	    
	    
	
os._exit(0)
