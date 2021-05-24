#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pachong.py
@Time    :   2021/05/22 21:36:09
@Author  :   Aevox 
@Version :   1.0
@Contact :   aevox_y@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import xlrd
import random
import re
from nonebot import on_command,on_message,on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message

movie = on_command("电影",aliases={"来个电影","电影","推荐点电影","看个片"},priority=3)

@movie.handle()
async def gmovie(bot:Bot,event:Event,state:T_State):
    gid = event.group_id
    movie_url,movie_image,movie_name,movie_inf = get_movie_inf(get_movie())
    msg1 = "来看这个吧:\n%s"%movie_inf
    msg2 = "[CQ:image,file=%s]"%movie_image
    msg3 = "[CQ:share,url=%s,title=%s]"%(movie_url,movie_name)
    await bot.send_group_msg(group_id = gid,message = msg1)
    await bot.send_group_msg(group_id = gid,message = msg2)
    await bot.send_group_msg(group_id = gid,message = msg3)






def get_movie():
    try:
        workbook = xlrd.open_workbook("src\plugins\pachong\豆瓣电影Top250.xls")         # 打开数据文件
    except Exception as e:
        print('发生错误',e)
    rm = random.randint(0,250)                                 # 随机选择一个电影

    sheet = workbook.sheet_by_index(0)                         # 获取表单

    movie = sheet.row(rm)
    return movie

def get_movie_inf(movie):
    movie_url = movie[0].value
    movie_image = movie[1].value
    movie_name = movie[2].value
    movie_rating = movie[4].value
    movie_inq = movie[6].value

    inf ="《" +movie_name+ "》-----"+ movie_inq + "\n" + "评分:"+ movie_rating

    return movie_url,movie_image,movie_name,inf

# if __name__ == "__main__":
#     movie_url,movie_image,movie_name,movie_inf = get_movie_inf(get_movie())
#     print(movie_inf)


    

