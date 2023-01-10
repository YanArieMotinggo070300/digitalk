# plugins/clock.py
import cs_bot
from cs_bot import MessageSession
from datetime import datetime


@cs_bot.on_keyword(["time"])
def time_teller(sess: MessageSession):
    clock: str = datetime.now().strftime("%H:%M:%s")
    sess.reply(f"Now it is {clock}")
    cs_bot.send(sess.sender.email, f"Now it is {clock}")