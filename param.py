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
global ETF      # End Transfer File(s)
global MTF      # Music Transfer File(s)
global RCC 		# Remote Control Command
global FTF 		# Finish Transfer File(s)
global RTM 		# Return Transfer Music


MTF = "001"
RCC = "002"
RTM = "101"
ETF = "111"
FTF = "200"

TCP_IP = "127.0.0.1"
SOCKET = 3105
BUFFER_SIZE = 4096

