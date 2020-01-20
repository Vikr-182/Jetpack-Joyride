import os,signal,time
from playsound import playsound
from colorama import init,Fore
from board import *
from character import *
from gameObjects import *
import numpy as np
import take_input as ti
init()

print("\033\143")
key = True
a = 0

initSettings = gameSettings(5,10)
initSettings._gameSettings__displaySettings()

#   Dimensions 
totalxdim = 2000
totalydim = 20
xdim = 80
ydim = 2
xpos = 0

sample = board(totalxdim,totalydim,xdim,ydim)
sample._board__display(xpos,xpos+xdim)
start = time.time()
while key is True:
#    playsound('lol.mp3')
    if initSettings._gameSettings__life is 0:
        key = False
        print("Thank you for playing! Do download our app on PlayStore")
    print('Hi')
    while key is True:
        if (time.time()-start==0.1):
            # Move screen
            start = time.time()
            xpos = xpos + 1
            sample._board__display(xpos,xpos+xdim)
