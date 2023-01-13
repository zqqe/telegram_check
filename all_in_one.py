# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync
import tg_code


class bot_check():
    def bot_pic(bot_id,messages):
        # client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        # time.sleep(2)  # 延时2秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        # messages = client.get_messages(bot_id)
        time.sleep(2)
        messages[0].download_media(file="1.jpg")
        the_code = tg_code.truecaptcha()
        client.send_message(bot_id, the_code)
        time.sleep(5)
        messages = client.get_messages(bot_id)
        return messages[0].message

    def bot_pic2(bot_id,bot_command):
        client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        messages = client.get_messages(bot_id)
        time.sleep(2)
        messages[0].download_media(file="1.jpg")
        the_code = tg_code.truecaptcha()
        client.send_message(bot_id, the_code)
        time.sleep(5)
        messages = client.get_messages(bot_id)
        return messages[0].message

    def bot_inline(bot_id,messages):
        # client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        # time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        # messages = client.get_messages(bot_id)
        time.sleep(2)
        messages[0].download_media(file="1.jpg")
        time.sleep(2)
        the_code = tg_code.truecaptcha()

        res = messages[0].click(text=the_code)
        time.sleep(1)
        if res == "None":
            messages[0].click(0)
        time.sleep(5)
        messages = client.get_messages(bot_id)
        return messages[0].message

    def bot_inline2(bot_id,bot_command):
        client.send_message(bot_id, bot_command)  # 第一项是机器人ID，第二项是发送的文字
        time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        messages = client.get_messages(bot_id)
        time.sleep(2)
        messages[0].download_media(file="1.jpg")
        time.sleep(2)
        the_code = tg_code.truecaptcha()

        res = messages[0].click(text=the_code)
        time.sleep(1)
        if res == "None":
            messages[0].click(0)
        time.sleep(5)
        messages = client.get_messages(bot_id)
        return messages[0].message


api_id = [0123456, 6543210]	#输入api_id，一个账号一项
api_hash = ['0123456789abcdef0123456789abcdef', 'abcdef0123456789abcdef0123456789']	#输入api_hash，一个账号一项
bots_connands = {"@charontv_bot": ["/checkin", "获得"],"@JMSIPTV_bot": ["/checkin", "成功"],"@blueseamusic_bot": ["/checkin", "成功"],"@svipxddosbot": ["签到领积分", "成功"]}
session_name = api_id[:]
for num in range(len(api_id)):
    session_name[num] = "id_" + str(session_name[num])
    client = TelegramClient(session_name[num], api_id[num], api_hash[num])
    client.start()
    for key, value in bots_connands.items():
        client.send_message(key, value[0])  # 第一项是机器人ID，第二项是发送的文字
        time.sleep(2)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        messages = client.get_messages(key)
        if value[1] not in messages[0].message:
            if messages[0].buttons != None:
                i = 0
                the_result = bot_check.bot_inline(key,messages)
                while value[1] not in the_result:
                    time.sleep(10)
                    i += 1
                    the_result = bot_check.bot_inline2(key,value[0])
                    if i >= 5:
                        break
            else:
                i = 0
                the_result = bot_check.bot_pic(key,messages)
                while value[1] not in the_result:
                    time.sleep(10)
                    i += 1
                    the_result = bot_check.bot_pic2(key,value[0])
                    if i >= 5:
                        break

os._exit(0)
