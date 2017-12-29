"""
Dual Server IRC BOT (IRC_JUICE) Created by Arttu Mahlakaarto.

(https://github.com/amahlaka/IRC_JUICE)

This bot connects to 2 different IRC servers and runs WHOIS on Target server,
when instructed to by Command server

Requirements:
  - Python version 3.5.2
  - You also need to have pip installed matching the python version!
    (at least pip 8.1.1)
  - Asyncirc (https://github.com/watchtower/asyncirc)
    (Install with "pip3 install asyncio-irc" or "pip install asyncio-irc")

Usage:
  - Make sure that all Requirements are met
  - Clone repository
  - Modify the configuration below
  - Run with `python IRC_JUICE.py`
Tested with Python 3.5.2
Date: 29.12.2017
Version: 0.1b

Popular IRC servers:
NAME: HOSTNAME:PORT
Freenode: chat.freenode.net:6667
Choopa:  irc.choopa.net:6667
Rizon: irc.rizon.rocks:6667

IRC_JUICE is licensed under MIT
For more details, please see the LICENSE.md file

Uses asyncirc library from https://github.com/watchtower/asyncirc
"""

import asyncio
from asyncirc import irc

# **** C&C Configuration ****
CC_HOST = ""  # IP or HOSTNAME of C&C Server.
CC_PORT = 6667  # Port of C&C Server.
CC_NICK = ""  # Nickname for the bot, shown on C&C.
CC_CHANNEL = ""  # C&C Channel name (With the # Prefix).
CC_OWNER = ""  # Accept commands only from this User.
# ////////END OF C&C CONFIG ////////

# **** Target Configuration ****
TRGT_HOST = ""  # IP or HOSTNAME of Target Server.
TRGT_PORT = 6667  # Target server port. ( Usually between 6665-6669)
TRGT_CHAN = []  # List of Channels to join on target server.
TRGT_NICK = ""  # Nickname of bot in Target server.
# ////////END OF TARGET CONFIG ////////


# DO NOT MODIFY BELOW THIS!
bot = irc.connect(CC_HOST, CC_PORT, use_ssl=False)
bot.register(CC_NICK, CC_NICK, CC_NICK)
WHOIS_B = None

stalker = irc.connect(TRGT_HOST, TRGT_PORT, use_ssl=False)
stalker.register(TRGT_NICK, TRGT_NICK, TRGT_NICK)

print("C&C SERVER: "+CC_HOST+":"+str(CC_PORT))
print("C&C CHANNEL: "+CC_CHANNEL)
print("ACCEPTING COMMNDS FROM: "+CC_OWNER)


class User:
    """Class for storing results of WHOIS."""

    def __init__(self):
        """Class Variables."""
        self.Name = ""
        self.Nick = ""
        self.Chan = ""
        self.Host = ""


UserS = User()


@stalker.on("irc-001")
def autojoin_channelsB(message):
    """Handle channel joining for target server."""
    stalker.join(TRGT_CHAN)


@bot.on("irc-001")
def autojoin_channels(message):
    """Handle channel joining for C&C server."""
    bot.join([CC_CHANNEL])


@stalker.on("irc-311")
def whois(message):
    """Handle IRC code 311."""
    global WHOIS_B
    if(WHOIS_B is None):
        WHOIS_B = "\n" + str(message)
    else:
        WHOIS_B = WHOIS_B + "\n" + str(message)

    print(message)


@stalker.on("irc-312")
def whois2(message):
    """Handle IRC code 312."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-313")
def whois3(message):
    """Handle IRC code 313."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-314")
def whois4(message):
    """Handle IRC code 314."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-315")
def whois5(message):
    """Handle IRC code 315."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-316")
def whois6(message):
    """Handle IRC code 316."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-317")
def whois7(message):
    """Handle IRC code 317."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-319")
def whois8(message):
    """Handle IRC code 319."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)


@stalker.on("irc-318")
def whois9(message):
    """Handle IRC code 318, End of WHOIS."""
    global WHOIS_B
    WHOIS_B = WHOIS_B + "\n" + str(message)
    ParseResult(WHOIS_B)


def ParseResult(result):
    """Parse WHOIS results."""
    print(result)
    global UserS
    result = result.replace('"', '')
    result = result.replace('RFTRGT459Message:', '')  # Remove the prefix
    result = result.replace(':', '')
    resultS = result.split('\n')
    for line in resultS:
        temps = line.split(' ')
        temps = list(filter(None, temps))
        if(len(temps) >= 3):
            if(temps[1] in "311"):
                UserS.Nick = temps[4]
                UserS.Name = temps[7]
                UserS.Host = temps[5]
            if(temps[1] in "319"):
                y = [x for (i, x) in enumerate(temps) if i not in (0, 1, 2, 3)]
                UserS.Chan = str(y)
            if(temps[1] in "318"):
                SendWhois(UserS)


def SendWhois(res):
    """Send Whois results to C&C."""
    msg = "Whois report: "+res.Nick+"'s Real name is: "+res.Name+"  "
    msg = msg + "Channels:" + res.Chan + " HOST:" + res.Host + " on "+TRGT_HOST
    bot.say(CC_CHANNEL, "Results for WHOIS: {}".format(msg))


@bot.on("message")
def incoming_message(parsed, user, target, text):
    """Handle incoming messages."""
    if(target in CC_CHANNEL and user is CC_OWNER):
        cmd = text.split(' ', 1)
        if('!whois' in cmd[0]):
            stalker.writeln("WHOIS {}".format(cmd[1]))


asyncio.get_event_loop().run_forever()
