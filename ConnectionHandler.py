import sys
import socket
import string
import time

CC_HOST = "127.0.0.1"
CC_PORT = 6667
CC_NAME = "BotteriB"
CC_OWNR = "amahlaka"
CC_SOCK = socket.socket()
CC_CHAN = "##JUISSICMD"


C1_HOST = "irc.choopa.net"
C1_PORT = 6667
C1_NAME = "Botteri"
C1_CHAN = "##BOTTERI"
C1_SOCK = socket.socket()

CC_BUFFER = ""
C1_BUFFER = ""
CC_CONNECTED = False
C1_CONNECTED = False
C1_LISTEN = True


def ConnectToCC():
    """Handle Connection to C&C Server."""
    global CC_CONNECTED
    global CC_SOCK


print("**** Connecting to: " + CC_HOST + ":" + str(CC_PORT) + " ****")
CC_SOCK.connect((CC_HOST, CC_PORT))
CC_SOCK.setblocking(False)
CC_SOCK.send("USER %s %s bla :%s\r\n" % (CC_NAME, CC_NAME, botteri))
#tmps = "USER " + CC_NAME + " " + CC_NAME + " " + CC_NAME + " :bro\n"
#CC_SOCK.send(tmps)
time.sleep(10)
CC_SOCK.send("NICK " + CC_NAME + "\n")
time.sleep(10)
CC_SOCK.send("JOIN " + CC_CHAN + "\n")
time.sleep(4)
CC_SOCK.send("PRIVMSG " + CC_OWNR + " " + CC_NAME + " ALIVE\n")
CC_SOCK.send("PRIVMSG " + CC_CHAN + " " + CC_NAME + " ALIVE\n")
print("DONE\n")
CC_CONNECTED = True


def ConnectToC1():
    """Handle Connection to Target Server."""
    print("**** Connecting to: " + C1_HOST+":"+str(C1_PORT) + " ****")
    C1_SOCK.connect((C1_HOST, C1_PORT))
    time.sleep(10)
    C1_SOCK.setblocking(False)
    tmps = "USER " + C1_NAME + " " + C1_NAME + " " + C1_NAME + " :bro\r\n"
    print(tmps)
    C1_SOCK.send(tmps)
    time.sleep(5)
    C1_SOCK.send("NICK " + C1_NAME + "\r\n")
    time.sleep(5)
    C1_SOCK.send("JOIN " + C1_CHAN + "\r\n")
    time.sleep(3)
    CC_SOCK.send("PRIVMSG " + C1_CHAN + " " + C1_NAME + " ALIVE\n")
    C1_CONNECTED = True
    print("DONE\n")


def CMD_WHOIS(USER):
    print("\n REQUESTING WHOIS FOR USER: " + USER + " \n")
    if(C1_CONNECTED):
        C1_SOCK.send("WHOIS " + USER)
        print("WHOIS command sent")
    else:
        print("Not Connected to target server")


ConnectToCC()
#if(C1_CONNECTED is False):
#    ConnectToC1()

while True:
    time.sleep(3)
    print(".")
    if(CC_CONNECTED is True):

        CC_BUFFER = CC_SOCK.recv(1024)
        print(CC_BUFFER)
        temp = string.split(CC_BUFFER, "\n")
        tmpb = temp.pop()
        print(tmpb)
        if("451" in tmpb):
            CC_SOCK.send("USER %s %s bla :%s\r\n" % (CC_NAME, CC_NAME, CC_NAME))
    #C1_BUFFER = C1_SOCK.recv(1024)
    #print(C1_BUFFER)
