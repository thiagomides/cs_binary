#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,random,logging,socket,threading,time,pygame 
from param import *
from PIL import Image, ImageTk
from os.path import exists

root = Tk()
ini = 0
fim = 0
noow = ""

played = []
c = ["beep-01a.mp3"]


def clear_repository():
    global c,played

    path = "arquivos/"
    
    for file in os.listdir(path):
        os.remove("arquivos/"+file)

    ini = time.time()
    logging.debug("[S] Repository clean "+ str(time.asctime( time.localtime(time.time()) )) )
    c = ["beep-01a.mp3"]
    played = []
    played.append(0)

def music_play(x):
    global c, noow
    noow = c[x]
    pygame.mixer.music.load(c[x])
    pygame.mixer.music.play(0)
    logging.info("[M] "+str(x)+ " played "+ str(c[x]))
    played.append(x)
    print(x, c[x])



def music():
    pygame.init()
    try:
        pygame.mixer.pre_init(44100, -16, 2)
        pygame.mixer.init(44100, -16, 1, 4096)
    
    except pygame.error, exc:
     
        print >>sys.stderr, "Could not initialize sound system: %s" % exc
        exit()

    music_play(0)
    queu()

def queu():
    global  c, played, noow
    pos = pygame.mixer.music.get_pos()
    
    try:
      if int(pos) == -1:
        j = 0
        x = random.randint(1,len(c))
        while x in played:
            if j == len(c):
                played = []
                j = 0
            j += 1
            x = random.randint(1,len(c))            
        
        music_play(x)

    except:
      pass
    root.after(1000, server)



def response(client_socket,data):
    client_socket.send(data)  
    client_socket.close()
    
def get_playlist():
    global c
    playlist = ""
    for x in range(0,len(c)):
        playlist = playlist + str(x) + " - " + c[x] + "\n"
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

        
        client_socket.send(FTF)

    client_socket.close()

def remote_control(client_socket):
    global c,x
    type = client_socket.recv(4)
    
    if type == "list":
        response(client_socket,get_playlist())

    elif (type == "stop"):
        pygame.mixer.music.pause()
        response(client_socket,"Stop Music")

    elif (type == "play"):
        pygame.mixer.music.unpause()
        response(client_socket,"Play Music")

    elif(type == "noow"):
        response(client_socket,noow)
    
    else:
        if (type == "next"):
            msg = "No Music List"
            if len(c) > 1:
                music_play(random.randint(1,len(c)))
                msg = "Next Music"    
            response(client_socket,msg)
           
        elif (type == "rewi"):
            
            pygame.mixer.music.rewind()
            client_socket.send("Repeat Music")
            logging.info("[Music] "+str(x)+ " played "+ str(c[x]))

def control(client_socket,addr):
    type = client_socket.recv(3)
    if type == MTF:
        music_transfer(client_socket,addr)
    elif type == RCC:
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

    logging.basicConfig(filename = 'example.log',level = logging.DEBUG)
    
    if not(exists("arquivos/")):
        os.mkdir("arquivos/")
    
    

    image = Image.open("wallpapper1.png")
    photo = ImageTk.PhotoImage(image)

    label = Label(image = photo)
    label.image = photo 
    label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    label.pack()

    clear_repository()
    music()
    execute_music()



if __name__ == '__main__':
    main()