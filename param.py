#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here


global TCP_IP
global BUFFER_SIZE
global SOCKET
global FIRST
global FREQ
global BITSIZE
global CHANNELS
global BUFFER
global FRAMERATE



FIRST = True
TCP_IP = "127.0.0.1"
SOCKET = 3094
BUFFER_SIZE = 4096

# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished
