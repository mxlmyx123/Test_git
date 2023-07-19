"""
    非阻塞IO(套接字模块)
"""
from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1',8888))
