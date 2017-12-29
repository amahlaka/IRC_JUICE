import sys
import time
import asyncio
from asyncirc import irc
CC_HOST = "127.0.0.1"
CC_PORT = 6667
CC_NICK = "Botteri1"

C1_HOST = "chat.freenode.net"
C1_PORT = 6667
C1_CHAN = "##BOTTERI"
C1_NICK = "Botteri1"
bot = irc.connect(CC_HOST, CC_PORT, use_ssl=False)
bot.register(CC_NICK, CC_NICK, CC_NICK)


stalker = irc.connect(C1_HOST, C1_PORT, use_ssl=False)
stalker.register(C1_NICK, C1_NICK, C1_NICK)


@stalker.on("irc-001")
def autojoin_channelsB(message):
    stalker.join(["##JUISSICMD"])


@bot.on("irc-001")
def autojoin_channels(message):
    bot.join(["##JUISSICMD", "#BOTTERI"])


@bot.on("irc-311")
def whois(message):
    print(message)


@bot.on("message")
def incoming_message(parsed, user, target, text):
    # parsed is an RFC1459Message object
    # user is a User object with nick, user, and host attributes
    # target is a string representing nick/channel the message was sent to
    # text is the text of the message
    bot.say(target, "{}: you said {}".format(user.nick, text))
    stalker.say(target, "{}: you said {}".format(user.nick, text))
    cmd = text.split(' ', 1)
    print(cmd)
    print(cmd[0])
    if('!whois' in cmd[0]):
        print("WHOIS")
        stalker.say("##JUISSICMD", "TESTING")
        stalker.writeln("WHOIS {}".format(cmd[1]))


asyncio.get_event_loop().run_forever()
