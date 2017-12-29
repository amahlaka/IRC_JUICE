import sys
import time
import asyncio
from asyncirc import irc
CC_HOST = "127.0.0.1"
CC_PORT = 6667
CC_NICK = "Botteri1"
CC_CHANNEL = "##JUISSICMD"
C1_HOST = "chat.freenode.net"
C1_PORT = 6667
C1_CHAN = "##BOTTERI"
C1_NICK = "Botteri1"
CC_OWNER = "amahlaka"


victimList = ["##TEST1", "#BOTTERI"]

bot = irc.connect(CC_HOST, CC_PORT, use_ssl=False)
bot.register(CC_NICK, CC_NICK, CC_NICK)
WHOIS_B = None

stalker = irc.connect(C1_HOST, C1_PORT, use_ssl=False)
stalker.register(C1_NICK, C1_NICK, C1_NICK)

print("C&C SERVER: "+CC_HOST+":"+str(CC_PORT))
print("C&C CHANNEL: "+CC_CHANNEL)
print("ACCEPTING COMMNDS FROM: "+CC_OWNER)

class User:
    def __init__(self):
        self.Name = ""
        self.Nick = ""
        self.Chan = ""
        self.Host = ""


UserS = User()


@stalker.on("irc-001")
def autojoin_channelsB(message):
    stalker.join(victimList)
    print("Connected to: " + victimList)


@bot.on("irc-001")
def autojoin_channels(message):
    bot.join([CC_CHANNEL])


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
def whois6(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-317")
def whois7(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-319")
def whois8(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-318")
def whois9(message):
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)
    SendResult(WHOIS_B)


def SendResult(result):
    print(result)
    global UserS
    result = result.replace('"', '')
    result = result.replace('RFC1459Message:', '')
    result = result.replace(':', '')
    resultS = result.split('\n')
    for line in resultS:
        temps = line.split(' ')
        temps = list(filter(None, temps))
        if(len(temps) >= 3):
            if(temps[1] in '311'):
                UserS.Nick = temps[4]
                UserS.Name = temps[7]
                UserS.Host = temps[5]
            if(temps[1] in "319"):
                y = [x for (i, x) in enumerate(temps) if i not in (0, 1, 2, 3)]
                UserS.Chan = str(y)
            if(temps[1] in "318"):
                SendWhois(UserS)


def SendWhois(res):
    msg = "Whois report: "+res.Nick+"'s Real name is: "+res.Name+"  "
    msg = msg + "Channels:" + res.Chan + " HOST:" + res.Host + " on " + C1_HOST
    bot.say(CC_CHANNEL, "Results for WHOIS: {}".format(msg))


@bot.on("message")
def incoming_message(parsed, user, target, text):
    if(target in CC_CHANNEL and user is CC_OWNER):
        cmd = text.split(' ', 1)
        if('!whois' in cmd[0]):
            stalker.writeln("WHOIS {}".format(cmd[1]))


asyncio.get_event_loop().run_forever()
