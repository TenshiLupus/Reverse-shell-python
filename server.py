from mmap import PROT_WRITE
import socket
import sys

# create socket allows to computers to connect

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# bind socket to port and wait connection from a client

def socket_bind():
     try:
        global host
        global port
        global s
        print("binding socket to port " + str(port))