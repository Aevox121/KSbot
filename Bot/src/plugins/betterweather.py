#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   betterweather.py
@Time    :   2021/05/27 08:24:05
@Author  :   Aevox 
@Version :   1.0
@Contact :   aevox_y@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import os
import re
from nonebot import on_command,on_message,on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message

weather = on_command("天气", priority=1)
path = 're\msyh.ttc'
file = open('re\citycid.txt','r',encoding='utf-8')
cityids = file.readlines()
cityids = str(cityids)
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    gid = event.group_id
    city = state["city"]
    city_weather = await weathercn(await findcityid(city))
    msg = '[CQ:image,file=file:///C:\\Users\德兰李维奇\.cache\weatherCN\weather.png]'
    await bot.send_group_msg(group_id=gid,message=msg)






async def findcityid(cityname):
    cityid = re.findall("(\d{9})=%s" % cityname, cityids)[0]
    return cityid

async def weathercn(cityid):
    str = 'python -m weathercn %s D:\KSBot\weather\pic\msyh.ttc'%cityid
    os.system(str)
    print("打印成功!")

