#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,random,logging,socket,threading
from param import *
import pygame, time

root = Tk()
ini = 0
fim = 0
noow = ""

def clear_repository():
    global c
    path = "arquivos/"
    dir = os.listdir(path)
    for file in dir:
        os.remove("arquivos/"+file)

    ini = time.time()
    date_time = time.asctime( time.localtime(time.time()) )
    logging.debug("[S] Repository clean "+ str(date_time) )
    c = ["beep-01a.mp3"]
    played = []

def music():
    global c
    pygame.init()
    
    try:
        pygame.mixer.pre_init(48000, -16, 2) # 44.1kHz, 16-bit signed, stereo
        pygame.mixer.init(48000, -16, 1, 4096)
    except pygame.error, exc:
        print >>sys.stderr, "Could not initialize sound system: %s" % exc
        return 1
    pygame.mixer.music.load(c[0])
    pygame.mixer.music.play(0)
    
    queu()

def queu():
    global  c, played, noow
    pos = pygame.mixer.music.get_pos()
    
    try:
      if int(pos) == -1:
        j = 0
        while True:
            if j == len(c):
                played = []
            x = random.randint(0,len(c))
            if (x not in played or x != 0):
                played.append(x)
                break
            j += 1

        if x != 0:
            print(x, c[x])
            noow = c[x]
            logging.info("[M] "+str(x)+ " played "+ str(c[x]))
            pygame.mixer.music.load(c[x])
            pygame.mixer.music.play(0)
    except:
      pass
    root.after(1000, server)



def response(client_socket,data):
    client_socket.send(data)  
    client_socket.close()
    

def music_transfer(client_socket,addr):
    size = client_socket.recv(16)
    name = client_socket.recv(int(size))
    
    client_socket.send("101")
    filesize = client_socket.recv(32)
    filesize = int(filesize, 2)
    
    file = open("arquivos/"+name, 'w')
    chunksize = BUFFER_SIZE
    
    while filesize > 0:
        if filesize < chunksize:
            chunksize = filesize
    
        data = client_socket.recv(BUFFER_SIZE)  
        filesize -= len(data)            
        file.write(data)
        
    file.close()

    c.append("arquivos/"+name)
    logging.debug("[M] "+name+ " Send to "+ str(addr))

def remote_control(client_socket):
    global c
    type = client_socket.recv(4)
    print type
    if type == "list":
        playlist = ""
        for x in range(0,len(c)):
            playlist = playlist + str(x) + " - " + c[x] + "\n"
        client_socket.send(playlist)
    elif (type == "stop"):
        pygame.mixer.music.pause()
        client_socket.send("Stop Music")
    elif (type == "play"):
        pygame.mixer.music.unpause()
        client_socket.send("Play Music")
    elif (type == "next"):
        x = random.randint(1,len(c))
        pygame.mixer.music.load(c[x])
        pygame.mixer.music.play(0)
        client_socket.send("Next Music")
    elif (type == "rewi"):
        pygame.mixer.music.rewind(c[x])
    elif(type == "noow"):
        client_socket.send(noow)

def control(client_socket,addr):
    type = client_socket.recv(3)
    if type == "001":
        music_transfer(client_socket,addr)
    elif type == "002":
        remote_control(client_socket)
        
    
    
    
def execute_music():
    root.mainloop()   
   

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.bind((TCP_IP, SOCKET))
    s.listen(5)
    s.settimeout(1.0)
    ini = time.time()
    date_time = time.asctime(time.localtime(time.time()) )
    logging.debug("[S]ystem init "+ str(date_time) )
    while True:
        queu()
        try:
            (conn, addr) = s.accept()
            print 'Connection address:', addr
            logging.debug("[C] "+ str(addr) )
            t = threading.Thread(target=control, args=(conn, addr),)   
            t.run()
        except socket.timeout:
            fim = time.time()
            if ((fim - ini) > 3600):
                clear_repository()      
            
def main():
    music()
    execute_music()



if __name__ == '__main__':
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    
    played = []
    c = ["beep-01a.mp3"]
    main()