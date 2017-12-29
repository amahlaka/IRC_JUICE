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
WHOIS_B = None

stalker = irc.connect(C1_HOST, C1_PORT, use_ssl=False)
stalker.register(C1_NICK, C1_NICK, C1_NICK)


class User:
    Name = ""
    Nick = ""
    Channels = ""

@stalker.on("irc-001")
def autojoin_channelsB(message):
    stalker.join(["##JUISSICMD"])


@bot.on("irc-001")
def autojoin_channels(message):
    bot.join(["##JUISSICMD", "#BOTTERI"])


@stalker.on("irc-311")
def whois(message):
    global WHOIS_B
    if(WHOIS_B is None):
        WHOIS_B = "\n" + str(message)
    else:
        WHOIS_B = WHOIS_B + "\n" + str(message)

    print(message)


@stalker.on("irc-312")
def whois2(message):
    global WHOIS_B


    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-313")
def whois3(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-314")
def whois4(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-315")
def whois5(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-316")
def whois5(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-317")
def whois5(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-319")
def whois5(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)

@stalker.on("irc-318")
def whois5(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)
    SendResult(WHOIS_B)


def SendResult(result):
    print(result)
    result = result.replace('"', '')
    result = result.replace('RFC1459Message:', '')
    result = result.replace(':', '')
    resultS = result.split('\n')
    for line in resultS:
        temps = line.split(' ')
        temps = list(filter(None, temps))
        print(temps)
        if(len(temps) => 3):
            if(temps[1] == '311'):



@bot.on("message")
def incoming_message(parsed, user, target, text):
    # parsed is an RFC1459Message object
    # user is a User object with nick, user, and host attributes
    # target is a string representing nick/channel the message was sent to
    # text is the text of the message
    bot.say(target, "{}: you said {}".format(user.nick, text))
    cmd = text.split(' ', 1)
    print(cmd)
    print(cmd[0])
    if('!whois' in cmd[0]):
        print("WHOIS")
        stalker.say("##JUISSICMD", "TESTING")
        stalker.writeln("PRIVMSG ##JUISSICMD DEBUG")
        stalker.writeln("WHOIS {}".format(cmd[1]))


asyncio.get_event_loop().run_forever()
