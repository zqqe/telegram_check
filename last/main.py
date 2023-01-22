# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync
import tg_code2


#签到结束删除验证码图片
def remove_pic():
    images_files = os.listdir(os.getcwd())
    for file in images_files:
        if file.endswith('.jpg'):
            os.remove(os.path.join(os.getcwd(), file))


class bot_check():
    def bot_easy(client,bot_id, bot_command):
        client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        time.sleep(5)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        messages = client.get_messages(bot_id)
        time.sleep(3)	#延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
	client.send_read_acknowledge(bot_id)	#将机器人回应设为已读
        return messages[0].message

    def bot_pic(client,bot_id,bot_command):
        client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        messages = client.get_messages(bot_id)
        time.sleep(2)
        pic_name=messages[0].download_media()
        the_code = tg_code2.truecaptcha(pic_name)
        client.send_message(bot_id, the_code)
        time.sleep(5)
        messages = client.get_messages(bot_id)
        time.sleep(3)	#延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
	client.send_read_acknowledge(bot_id)	#将机器人回应设为已读
        return messages[0].message

    def bot_inline(client,bot_id,bot_command):
        client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        messages = client.get_messages(bot_id)
        time.sleep(2)
        pic_name=messages[0].download_media()
        time.sleep(2)
        the_code = tg_code2.truecaptcha(pic_name)

        res = messages[0].click(text=the_code)#根据打码平台的返回结果点击内联键盘，若无法对应返回None
        if str(res) == "None":
            messages[0].click(0)#打码不匹配就点击第一个
        time.sleep(5)
        messages = client.get_messages(bot_id)
        time.sleep(3)	#延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
	client.send_read_acknowledge(bot_id)	#将机器人回应设为已读
        return messages[0].message


def mess(client,chose,bot_id,bot_command,bot_key):
    i=0
    if str(chose) == "0":
        the_result = bot_check.bot_easy(client,bot_id,bot_command)
        
    elif str(chose) == "1":
        the_result = bot_check.bot_pic(client,bot_id,bot_command)
        while bot_key not in the_result:
            i += 1
            the_result = bot_check.bot_pic(client,bot_id,bot_command)
            if i >= 4:#不成功循环次数
                break
    elif str(chose) == "2":
        the_result = bot_check.bot_inline(client,bot_id,bot_command)
        while bot_key not in the_result:
            i += 1
            the_result = bot_check.bot_inline(client,bot_id,bot_command)
            if i >= 4:#不成功循环次数
                break
    
api_id = [0123456, 6543210]  # 输入api_id，一个账号一项
api_hash = ['0123456789abcdef0123456789abcdef', 'abcdef0123456789abcdef0123456789']  # 输入api_hash，一个账号一项
bots_connands = [["@charontv_bot","/checkin", "获得","1"],["@JMSIPTV_bot","/checkin", "成功","2"],["@blueseamusic_bot","/checkin", "成功","1"],["@svipxddosbot","签到领积分", "成功","0"]]#格式：["机器人id", "签到命令", "签到成功关键词", "验证类别:0最普通签到；1回复验证码；2点击验证内联键盘"]
session_name = api_id[:]
for num in range(len(api_id)):
    session_name[num] = "id_" + str(session_name[num])
    client = TelegramClient(session_name[num], api_id[num], api_hash[num])
    client.start()
    for i_ in range(len(bots_connands)):
        bot_id=bots_connands[i_][0]
        bot_command=bots_connands[i_][1]
        bot_key=bots_connands[i_][2]
        bot_type=bots_connands[i_][3]
        try:
            mess(client,bot_type,bot_id,bot_command,bot_key)
        except:
            continue
os._exit(0)
remove_pic()
