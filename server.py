#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,random,logging,socket,threading,time,pygame,param
from param import *
from os.path import exists
from optparse import OptionParser


def parseArg():
    
    parser = OptionParser()

    parser.add_option("-p", "--port", dest="port", help="port number to listen up (default: 3030)", metavar="PORT",type="int");
    parser.add_option("-d", "--directory", dest="dir", help="binary(s) storage folder (default: ../arquivos/)",metavar="dir");

    
    (options, args) = parser.parse_args()

    if options.port == None:
        options.port = 3030

    if options.dir == None: 
        options.dir = "../arquivos/"
    
    if not(exists(options.dir)):
        os.mkdir(options.dir)


    return (options, args)

def clear_repository():
    
    for file in os.listdir(param.DIR):
        os.remove("../arquivos/"+file)

    param.SET_LIST = ["beep-01a.mp3"]
    param.PLAYED = []
    
    param.INI = time.time()
    logging.info("[SERVER] Repository clean "+ str(time.asctime(time.localtime(time.time()))))
    

def music_play(x):

    if (x < len(param.SET_LIST)):


        pygame.mixer.music.load(param.SET_LIST[x])
        pygame.mixer.music.play(0)
    
        param.NOW = x
        param.PLAYED.append(x)
    
        logging.info("[MUSIC] "+str(x)+ " played "+ str(param.SET_LIST[x]) + " " + str(time.asctime(time.localtime(param.INI))))
        print(x, param.SET_LIST[x])

        return True

    return False



def music():
    pygame.init()

    try:

        pygame.mixer.pre_init(44100, -16, 2)
        pygame.mixer.init(44100, -16, 1, 4096)
    
    except pygame.error, exc:
     
        print >>sys.stderr, "Could not initialize sound system: %s" % exc
        exit()

    music_play(0)
    queue()

def queue():
    pos = pygame.mixer.music.get_pos()
    
    if int(pos) == -1:

        j = 0
        x = random.randint(1,len(param.SET_LIST))
        if len(param.SET_LIST) > 1:
            while x in param.PLAYED:
                if j == len(param.SET_LIST):
                    param.PLAYED = []
                    j = 0
                j += 1
                x = random.randint(1,len(param.SET_LIST)  - 1) 

            music_play(x)


    param.ROOT.after(1000, server)


def binary_encode(string,bits):
    return bin(int(len(string)))[2:].zfill(int(bits))


def response(client_socket,data):
    client_socket.send(binary_encode(data,16))
    client_socket.send(data)  
    client_socket.close()
    
def get_playlist():
    playlist = ""
    for x in range(0,len(param.SET_LIST)):
        playlist = playlist + str(x) + " - " + param.SET_LIST[x] + "\n"
    return playlist


def music_transfer(client_socket,addr):
    while True:

        type = client_socket.recv(3)
        if type == ETF:
            break


        size = client_socket.recv(16)
        name = client_socket.recv(int(size))
        
        client_socket.send(RTM)
        
        filesize = client_socket.recv(32)
        filesize = int(filesize, 2)
        
        file = open(param.DIR+name, 'w')
        chunksize = BUFFER_SIZE
        
        while filesize > 0:
            if filesize < chunksize:
                chunksize = filesize
        
            data = client_socket.recv(BUFFER_SIZE)  
            filesize -= len(data)            
            file.write(data)
            
        file.close()

        param.SET_LIST.append(param.DIR+name)
        logging.info("[MUSIC] "+name+ " Send to "+ str(addr) + " " + str(time.asctime(time.localtime(param.INI))))

        
        client_socket.send(FTF)

    client_socket.close()

def remote_control(client_socket,addr):
    type = client_socket.recv(4)
    log = ""
    if type == "list":
        response(client_socket,get_playlist())
        log = "GET LIST"


    elif (type == "stop"):
        pygame.mixer.music.pause()
        response(client_socket,"Stop Music")
        log = "STOP MUSIC"

    elif (type == "play"):
        pygame.mixer.music.unpause()
        response(client_socket,"Play Music")
        log = "PLAY MUSIC"

    elif(type == "noow"):
        response(client_socket,param.SET_LIST[param.NOW])
        log = "MUSIC NOW"

    elif(type == "pmus"):

        client_socket.send(binary_encode(get_playlist(),16))
        client_socket.send(get_playlist())  

        resp = music_play(int(client_socket.recv(3)))
        if resp == False:
            client_socket.send("Música não existente")
        else:
            log = "MUSIC "+param.SET_LIST[param.NOW]+" PLAY"
            client_socket.close()
    
    else:
        msg = "No Music List"
        if len(param.SET_LIST) == 1:
            response(client_socket,msg)

        elif (type == "next"):
            music_play(random.randint(1,len(param.SET_LIST)  - 1 ))
            msg = "Next Music"  
            log = "NEXT MUSIC"
  
           
        elif (type == "rewi"):
            msg = "Repeat Music"
            music_play(param.NOW)
            log = "REPEAT MUSIC"
        response(client_socket,msg)

    logging.info("[CMD] "+log+ " to "+ str(addr) + " " + str(time.asctime(time.localtime(param.INI))))



def control(client_socket,addr):
    type = client_socket.recv(3)

    if type == MTF:
        music_transfer(client_socket,addr)

    elif type == RCC:
        remote_control(client_socket,addr)
        
    
    
def execute_music():
    param.ROOT.mainloop()   
   

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.bind((TCP_IP, param.PORT))
    s.listen(5)
    s.settimeout(1.0)
    param.INI = time.time()
    logging.info("[SERVER] Init "+ str(time.asctime(time.localtime(param.INI))))
    while True:
        queue()
        try:
            (conn, addr) = s.accept()
            print 'Connection address:', addr
            logging.info("[CONNECT] "+ str(addr) + " " + str(time.asctime(time.localtime(param.INI))))
            t = threading.Thread(target=control, args=(conn, addr),)   
            t.run()
        except socket.timeout:
            param.FIM = time.time()
            if ((param.FIM - param.INI) > 3600):
                clear_repository()      
            



def main(options):
 
    logging.basicConfig(filename = 'example.log',level = logging.INFO)
    
    param.PORT = options.port
    param.DIR = options.dir

    tk_settings()
    clear_repository()

    music()
    execute_music()



if __name__ == '__main__':
    (options, args) = parseArg()
    main(options)