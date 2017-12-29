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
CC_AUTH = False


def SendMessage(sock, message):
    """Send message to the socket."""
    print("Sending message " + message)
    sock.send(message.encode())


def ConnectCC():
    """Connect to C&C server."""
    print("***CONNECTING TO C&C SERVER***")
    global CC_SOCK
    global CC_CONNECTED
    CC_STAT = CC_SOCK.connect_ex((CC_HOST, CC_PORT))
    if(CC_STAT is 0):
        print("CONNECTED")
        CC_CONNECTED = True
    else:
        print("ERROR: " + CC_STAT)
        exit()
    print("DONE")


def MainLoop():
    """Main Loop."""
    global CC_SOCK
    global CC_CONNECTED
    global CC_AUTH
    while True:
        if (CC_CONNECTED is True):
            if(CC_AUTH is False):
                messageB = "USER " + CC_SOCK + " 0 * :Botteri\r\n"
                message = "NICK " + CC_NAME + "\r\n" + messageB
                SendMessage(CC_SOCK, message)
                CC_AUTH = True
            CC_MESSAGE = CC_SOCK.recv(1024)
            print(CC_MESSAGE)


ConnectCC()
MainLoop()
