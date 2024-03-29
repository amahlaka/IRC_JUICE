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
  - Modify the configuration in config.ini
  - Run with `python IRC_JUICE.py`
Tested with Python 3.5.2
Date: 29.12.2017
Version: 0.1b

Popular IRC servers:
NAME: HOSTNAME:PORT
Freenode: chat.freenode.net:6667
Choopa:  irc.choopa.net:6667 NOTE: MAY NOT WORK HERE
Rizon: irc.rizon.rocks:6667

IRC_JUICE is licensed under MIT
For more details, please see the LICENSE.md file

Uses asyncirc library from https://github.com/watchtower/asyncirc
"""

import configparser
import asyncio
from asyncirc import irc

config = configparser.ConfigParser()
config.read('config.ini')

# **** C&C Configuration ****
CC_HOST = config['CONTROL']['Host']  # IP or HOSTNAME of C&C Server.
CC_PORT = int(config['CONTROL']['Port'])  # Port of C&C Server.
CC_NICK = config['CONTROL']['Nick']  # Nickname for the bot, shown on C&C.
CC_CHANNEL = config['CONTROL']['Channel']  # C&C Channel name.
CC_OWNER = config['CONTROL']['Owner']  # Accept commands only from this User.
# ////////END OF C&C CONFIG ////////

# **** Target Configuration ****
TRGT_HOST = config['TARGET']['Host']  # IP or HOSTNAME of Target Server.
TRGT_PORT = int(config['TARGET']['Port'])  # Target server port.
TRGT_CHAN = config['TARGET']['Channel']  # List of Channels to join on target.
TRGT_NICK = config['TARGET']['Nick']  # Nickname of bot in Target server.
# ////////END OF TARGET CONFIG ////////


# DO NOT MODIFY BELOW THIS!


WHOIS_B = None
IsRealUser = False
bot = irc.connect(CC_HOST, CC_PORT, use_ssl=False)
bot.register(CC_NICK, CC_NICK, CC_NICK)


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
    stalker.join([TRGT_CHAN])
    print("Joining Target Channel")


@bot.on("irc-001")
def autojoin_channels(message):
    """Handle channel joining for C&C server."""
    bot.join([CC_CHANNEL])
    print("Joining CC Channel")


@stalker.on("irc-311")
def whois(message):
    """Handle IRC code 311."""
    global WHOIS_B
    global IsRealUser
    if(WHOIS_B is None):
        WHOIS_B = "\n" + str(message)
    else:
        WHOIS_B = WHOIS_B + "\n" + str(message)
    IsRealUser = True


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
    global IsRealUser
    if(IsRealUser is False):
        WHOIS_B = ''
        ReplyError()
    else:
        WHOIS_B = WHOIS_B + "\n" + str(message)
        ParseResult(WHOIS_B)


def ReplyError():
    """Handle user not existing."""
    bot.say(CC_CHANNEL, "User not found!")


def ParseResult(result):
    """Parse WHOIS results."""
    global UserS
    result = result.replace('"', '')
    result = result.replace('RFC1459Message:', '')  # Remove the prefix
    result = result.replace(':', '')
    resultS = result.split('\n')
    for line in resultS:
        temps = line.split(' ')
        temps = list(filter(None, temps))
        if(len(temps) >= 3):
            print(temps)
            if(temps[1] in '311'):
                UserS.Nick = temps[4]
                UserS.Name = temps[7]
                UserS.Host = temps[5]
            if(temps[1] in '319'):
                y = [x for (i, x) in enumerate(temps) if i not in (0, 1, 2, 3)]
                UserS.Chan = str(y)
            if(temps[1] in '318'):
                SendWhois()


def SendWhois():
    """Send Whois results to C&C."""
    bot.say(CC_CHANNEL, "Results for WHOIS on: " + TRGT_HOST)
    msg = "NICKNAME: "+UserS.Nick+". NAME: "+UserS.Name
    print(msg)
    bot.say(CC_CHANNEL, msg)
    msg = "CHANNELS: " + UserS.Chan
    print(msg)
    bot.say(CC_CHANNEL, msg)
    msg = "HOST: " + UserS.Host
    print(msg)
    bot.say(CC_CHANNEL, msg)
    global userS
    userS = User()
    global WHOIS_B
    global IsRealUser
    WHOIS_B = ""
    IsRealUser = False


@bot.on("message")
def incoming_message(parsed, user, target, text):
    """Handle incoming messages."""
    if(CC_CHANNEL in target and CC_OWNER in user.nick):
        cmd = text.split(' ', 1)
        if('!whois' in cmd[0]):
            stalker.writeln("WHOIS {}".format(cmd[1]))


asyncio.get_event_loop().run_forever()
