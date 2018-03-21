#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here


global BUFFER_SIZE
global TCP_IP
global SOCKET


TCP_IP = "127.0.0.1"
SOCKET = 3063

BUFFER_SIZE = 4096

