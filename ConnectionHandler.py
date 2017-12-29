import sys
import time
import asyncio
from asyncirc import irc
CC_HOST = "127.0.0.1"
CC_PORT = 6667
CC_NICK = "Botteri1"
bot = irc.connect(CC_HOST, CC_PORT, use_ssl=False)
bot.register(CC_NICK, CC_NICK, CC_NICK)


@bot.on("irc-001")
def autojoin_channels(message):
    bot.join(["##JUISSICMD", "#BOTTERI"])


@bot.on("message")
def incoming_message(parsed, user, target, text):
    # parsed is an RFC1459Message object
    # user is a User object with nick, user, and host attributes
    # target is a string representing nick/channel the message was sent to
    # text is the text of the message
    bot.say(target, "{}: you said {}".format(user.nick, text))



asyncio.get_event_loop().run_forever()
