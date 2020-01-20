import os,signal,time
from playsound  import playsound
from colorama import init,Fore
from board import *
from character import *
from gameObjects import *
import numpy as np
from take_input import inputtake as KBHit
from alarmexception import AlarmException
init()

print("\033\143")
key = True
a = 0

KB = KBHit()

#   Dimensions 
totalxdim = 2000
totalydim = 20
xdim = 150
ydim = 2
xpos = 0
za = 80

######################### INIT BOARD ##########################################################
sample = board(totalxdim,totalydim,xdim,ydim)
###############################################################################################

######################### INIT SETTINGS #######################################################
initSettings = gameSettings(5,10)
initSettings._gameSettings__displaySettings(10,0,xpos,1)
start = time.time()
###############################################################################################

######################### INIT CHARACTERS #####################################################
vel = [0,0]
din = Mandalorian(1,totalydim-ydim-4)
din.define_mandalorian(sample._board__board,1,totalydim-ydim-4)
sample._board__display(xpos,xpos+xdim)
###############################################################################################

while key is True:
    # playsound.playsound('ok.mp3')
    ok = True
    if din._person__life is 0:
        key = False
        print("Thank you for playing! Do download our app on PlayStore")
        quit()
    e = give_me_character()
    if e is 'q':
            print("Thank you for playing! Do download our app on PlayStore")
            quit()
    din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok)
    if (time.time()-start>=0.001):
            # Move screen
        start = time.time()       
        if za%(xdim//2) is 0:
            sample._board__render_board(xpos+xdim,xpos+xdim+xdim//2)
        za = za + 1
        if e is 'q':
            print("Thank you for playing! Do download our app on PlayStore")
            quit()
        ok = False
        din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok)
        xpos = xpos + 1
        sample._board__display(xpos,xpos+xdim)
        initSettings._gameSettings__displaySettings(din._person__life,din._person__coins,xpos,din._person__xco)
