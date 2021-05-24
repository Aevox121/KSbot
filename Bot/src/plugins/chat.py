from nonebot import on_command,on_message,on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message
import random

weather = on_command("天气",rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    uid = event.get_user_id()
    gid = event.group_id
#    bot.send_group_message(gid,uid,"很热")
#    await weather.send(message="很热",at_sender=True)
    await bot.send_msg(message_type='group',message="fuck",group_id=gid)


mao = on_keyword(keywords=['毛哥','毛毛'],priority=3)
@mao.handle()
async def fuck_mao(bot: Bot, event: Event, state:T_State):
    gid = event.group_id
    uid = "2733405958"
    faceid = str(random.randint(0,200))
    msg = "[CQ:at,qq=%s][CQ:face,id=%s]sb"%(uid,faceid)
    await bot.send_group_msg(group_id=gid, message=msg,auto_escape=False)



music = on_command("来首歌",priority=5)
@music.handle()
async def music_share(bot: Bot, event: Event, state:T_State):
    gid = event.group_id
    msg = "[CQ:music,type=qq,id=231594573]"
    await bot.send_group_msg(group_id=gid, message=msg,auto_escape=False)




se = on_command("色图",aliases={"涩图","色","涩"},priority=3)
@se.handle()
async def setu(bot: Bot, event: Event, state:T_State):
    gid = event.group_id
    uid = event.get_user_id()
    iid = str(random.randint(0,30))
    at = "[CQ:at,qq=%s]"%uid
    msg = "[CQ:image,file=file:///D:\KSBot\KSbot\image\setu\%s.png]"%iid
#    await bot.send_group_msg(group_id=gid, message=at,auto_escape=False)
    await bot.send_group_msg(group_id=gid, message=msg,auto_escape=False)


fun = on_command("功能",priority=1)
@fun.handle()
async def fun_list(bot:Bot,event:Event,state:T_State):
    gid = event.group_id
    funl = {
        "骂毛哥":"毛哥,毛毛",
        "发色图":"色图,涩图",
        "发电影":"电影,看个片"
    }
    items = funl.items()
    msg = "功能如下:\n-功能列表---触发口令-\n"
    for item in items:
        msg += "-%s----%s\n"%(item[0],item[1])
    await bot.send_group_msg(group_id = gid,message = msg)

bot_name = on_keyword(["机器人","章鱼","bot"],priority=1)
@bot_name.handle()
async def botnc(bot:Bot,event:Event,state:T_State):
    gid = event.group_id
    uid = event.user_id
    msgs = ["叫我干嘛???","别叫","你有病吧","干嘛!!!???"]
    r = random.randint(0,3)
    msg = "[CQ:at,qq=%s]%s"%(uid,msgs[r])
    await bot.send_group_msg(group_id = gid,message = msg)