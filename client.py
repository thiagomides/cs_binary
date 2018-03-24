#!/usr/bin/env python
# -*- coding: utf-8 -*-
from param import *
from os.path import isfile, join, isdir, exists, abspath
from optparse import OptionParser
import os,socket,ntpath,glob


def parseArg():
	parser = OptionParser()

	parser.add_option("-p", "--port", dest="port", help="port number to listen up (default: 3030)", metavar="PORT",type="int");
	parser.add_option("-a", "--address", dest="addr", help="address number to listen up (default: 127.0.0.1)",metavar="IP");
	parser.add_option('--no-keep-alive',dest="no_keep_alive", action='store_true',help='connections are  considered persistent unless a --no-keep-alive header is included')
	parser.add_option("-f", "--file", dest="file", help="path to binary file(s) or binary file",metavar="DOF");
	parser.add_option("-c", "--command", dest="command", help="customize chapter command (see README)",metavar="CMD")

	(options, args) = parser.parse_args()

	if options.port == None:
		options.port = 3030
	if options.file == None and options.command == None: 
		raise RuntimeError("Parameter -f or -c problem")
	if options.addr == None: 
		options.addr = "127.0.0.1"
	if options.file != None and not(exists(options.file)):
		exit("Directory or File doenst exist")
	
	return (options, args)

def path_leaf(path):
	ntpath.basename("a/b/c")
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)


def response(s,resp):
	s.send(resp)


def binary_encode(string,bits):
	return bin(int(len(string)))[2:].zfill(int(bits))

def remote_control(command,options):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((options.addr, options.port))
	response(s,"002")
	if (command == "list"):
		s.send("list")
	elif (command == "stop"):
		s.send("stop")
	elif (command == "play"):
		s.send("play")
	elif (command == "rewind"):
		s.send("rewi")
	elif (command == "next"):
		s.send("next")
	elif (command == "noow"):
		s.send("noow")
	elif (command == "play_music"):
		s.send("pmus")
	else:
		print "Invalid command"
		s.close()
		return

	chunksize = 4096

	size = 	int(s.recv(16), 2)
	while size > 0:

		if size < chunksize:
			chunksize = size

		data = s.recv(BUFFER_SIZE)  
		print data
		size -= len(data)            
	
	if (command == "play_music"):
		x = raw_input("Entre com o identificador da musica: ")
		while not (x.isdigit()):
			print "Somente identificadores numericos sao aceitos"	
			x = raw_input("Entre com o identificador da musica: ")
			
		s.send(x)
		print s.recv(30)

	s.close()


def file_transfer(files,options):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((options.addr, int(options.port)))
	response(s,MTF)
	i = 0
	for binary in files:

		if i != 0 and options.no_keep_alive == True:
			s.close()
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((options.addr, int(options.port)))
			response(s,MTF)


		response(s,MTF)

		filename_complete, file_extension = os.path.splitext(binary)
		filename = path_leaf(filename_complete)+file_extension
		
		s.send(binary_encode(filename,16))
		s.send(filename)

		if (s.recv(3) == RTM):

			filesize = os.path.getsize(os.path.join(filename_complete+file_extension))
			filesize = bin(filesize)[2:].zfill(32)
			
			response(s,filesize)

			f = open(binary,"r")
			l = f.read(BUFFER_SIZE)
	        
			while l:
				response(s,l)
				l = f.read(BUFFER_SIZE)

			f.close()

		
			if (int(s.recv(3)) == FTF):
				i += 1
				if options.no_keep_alive == True:
					response(s,ETF)
				continue


	response(s,ETF)
	s.close()

def main(options):
	files = []
	if options.file != None:
		if (isdir(options.file)):
			for filename in glob.glob(options.file+"/*"):
				files.append(filename)		
			file_transfer(files,options)
		else:  
			filename, file_extension = os.path.splitext(options.file)
			files.append(filename+file_extension)
			file_transfer(files,options)
	elif options.command != None:
		remote_control(options.command,options)
	


if __name__ == '__main__':
	(options, args) = parseArg()
	main(options)

