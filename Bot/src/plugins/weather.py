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
    faceid = str(random.randint(0,118))
    msg = "[CQ:at,qq="+uid+"][CQ:face,id="+faceid+"]sb"
    await bot.send_group_msg(group_id=gid, message=msg,auto_escape=False)



music = on_command("来首歌",priority=5)
@music.handle()
async def music_share(bot: Bot, event: Event, state:T_State):
    gid = event.group_id
    msg = "[CQ:music,type=163,id=36392027]"
    await bot.send_group_msg(group_id=gid, message=msg,auto_escape=False)




se = on_command("色图",aliases={"涩图","色","涩"},priority=3)
@se.handle()
async def setu(bot: Bot, event: Event, state:T_State):
    gid = event.group_id
    uid = event.get_user_id()
    iid = str(random.randint(0,19))
    at = "[CQ:at,qq="+uid+"]"
    msg = "[CQ:image,file=file:///D:\KSBot\KSbot\image\setu\\"+iid+".png]"
#    await bot.send_group_msg(group_id=gid, message=at,auto_escape=False)
    await bot.send_group_msg(group_id=gid, message=msg,auto_escape=False)