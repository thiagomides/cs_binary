#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from param import *
from os.path import isfile, join, isdir, exists, abspath
from optparse import OptionParser
import os
import ntpath
import glob

ntpath.basename("a/b/c")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def parseArg():
	parser = OptionParser()

	parser.add_option("-p", "--port", dest="port", help="Port Number to Listen Up", metavar="PORT_NUM",type="int")
	parser.add_option("-f", "--file", dest="file", help="File to share");
	parser.add_option("-d", "--directory", dest="dir", help="Directory to share")
	parser.add_option("-c", "--command", dest="command", help="Command")

	(options, args) = parser.parse_args()

	if options.file != None or options.dir != None:
		pass
		#if not(exists(options.file)):
		#	raise RuntimeError("File doenst exist")	
		#elif not(isdir(options.dir)):
		#	raise RuntimeError("Dir doenst exist")	
			
	return (options, args)


def remote_control(command):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, SOCKET))
	s.send("002")
	if (command == "list"):
		s.send("list")
		data = s.recv(BUFFER_SIZE)
		print data		
	elif (command == "stop"):
		s.send("stop")
		data = s.recv(BUFFER_SIZE)
	elif (command == "play"):
		s.send("play")
		data = s.recv(BUFFER_SIZE)
	elif (command == "rewind"):
		s.send("rewi")
		data = s.recv(BUFFER_SIZE)
	elif (command == "next"):
		s.send("next")
		data = s.recv(BUFFER_SIZE)
	elif (command == "noow"):
		s.send("noow")
		data = s.recv(BUFFER_SIZE)
		print data

	s.close()

def file_transfer(files):

	file_extension = ".mp3"
	for music in files:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, SOCKET))
		
		s.send("001")
		filename_complete, file_extension = os.path.splitext(music)
		filename = path_leaf(filename_complete)+file_extension
		
		size = len(filename)
		size = bin(size)[2:].zfill(16) 
		
		s.send(size)
		s.send(filename)

		data = s.recv(3)
		print data
		if (data == "101"):
			filename = os.path.join(filename_complete+file_extension)
			filesize = os.path.getsize(filename)
			filesize = bin(filesize)[2:].zfill(32) 
			s.send(filesize)

			f = open(music,"r")
			l = f.read(BUFFER_SIZE)
	        
			while l:
				s.send(l)
				l = f.read(BUFFER_SIZE)
			f.close()
			s.close()

def main():
	files = []
	if options.dir != None:
		for filename in glob.glob(options.dir+"/*.mp3"):
			files.append(filename)		
		file_transfer(files)
	elif options.file != None:  
		filename, file_extension = os.path.splitext(options.file)
		files.append(filename+file_extension)
		file_transfer(files)
	elif options.command != None:
		remote_control(options.command)
	


if __name__ == '__main__':
	(options, args) = parseArg()
	main()

