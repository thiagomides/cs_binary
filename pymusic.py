import pygame, time
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

root = Tk()
c = ["08 Srta. Sexo & Afins.mp3", "08 Srta. Sexo & Afins.mp3",  "13 Cartel Bolado (Muito Bolado).mp3", "music3.mp3","music4.mp3","music5.mp3", ""] 
#you can add more
x = 0

def music():
   pygame.init()
   pygame.mixer.init()
   pygame.mixer.music.load(c[x])
   pygame.mixer.music.play(0)
   que()

def que():
   global x, c
   pos = pygame.mixer.music.get_pos()
   try:
      if int(pos) == -1:
         x += 1
         print(x, c[x])
         pygame.mixer.music.load(c[x])
         pygame.mixer.music.play(0)
   except:
      pass
   root.after(1000, que)



music()


root.mainloop()

