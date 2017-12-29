# IRC_JUICE

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
  - Modify the configuration in the IRC_JUICE.py
  - Run with `python IRC_JUICE.py`
  - On C&C Channel, send message `!whois <target>`
  
Tested with Python 3.5.2
Date: 29.12.2017
Version: 0.1b

Popular IRC servers:
 - Freenode: `chat.freenode.net:6667` 
 - Choopa:  `irc.choopa.net:6667` 
 - Rizon: `irc.rizon.rocks:6667` 



IRC_JUICE is licensed under MIT
For more details, please see the LICENSE.md file

Uses asyncirc library from https://github.com/watchtower/asyncirc
