# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync
import tg_code

def tg_qd(tg_bot,tg_command):
    client.send_message(tg_bot, tg_command)	#第一项是机器人ID，第二项是发送的文字
    time.sleep(5)	#延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
    messages = client.get_messages(tg_bot)
    messages[0].download_media(file="1.jpg")
    the_code=tg_code.truecaptcha()
    client.send_message(tg_bot, the_code)
    time.sleep(5)
    #client.send_read_acknowledge("@charontv_bot")	#将机器人回应设为已读
    messages = client.get_messages(tg_bot)
    return messages[0].message



api_id = [0123456, 6543210]	#输入api_id，一个账号一项
api_hash = ['0123456789abcdef0123456789abcdef', 'abcdef0123456789abcdef0123456789']	#输入api_hash，一个账号一项
session_name = api_id[:]
bots_commands=["@blueseamusic_bot","/checkin","成功"]
for num in range(len(api_id)):
	session_name[num] = "id_" + str(session_name[num])
	client = TelegramClient(session_name[num], api_id[num], api_hash[num])
	client.start()
	the_result=tg_qd(bots_commands[0],bots_commands[1])
	i=0
	while bots_commands[2] not in the_result:
	    i+=1
	    the_result=tg_qd(bots_commands[0],bots_commands[1])
	    if i > 5:
	        break
	    
	    
	
os._exit(0)
