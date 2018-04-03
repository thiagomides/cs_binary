#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here


global BUFFER_SIZE
global SET_LIST
global TCP_IP
global SOCKET
global PORT
global POS
global ETF      # End Transfer File
global MTF      # Music Transfer File(s)
global RCC 		# Remote Control Command
global FTF 		# Finish Transfer File(s)
global RTM 		# Return Transfer Music
global DIR		# Directory path
global NOW		# Music ID NOW

MTF = "001"
RCC = "002"
RTM = "101"
ETF = "111"
FTF = "200"

SET_LIST, PLAYED = ["beep-01a.mp3"],[]
TCP_IP = "127.0.0.1"
PORT,BUFFER_SIZE = 3030,4096
NOW,DIR = "",""
INI,FIM,POS = 0,0,0
ROOT = Tk()
ROOT.title('Server')

def tk_settings():
    image = PIL.Image.open("wallpapper1.png")
    photo = ImageTk.PhotoImage(image)

    label = Label(image = photo)
    label.image = photo 

    label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    label.pack()

