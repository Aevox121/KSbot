from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

weather = on_command("天气", rule= to_me(), priority=5)



@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await weather.send("很热")