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
os.system('reset')

#   Dimensions 
totalxdim = 1000
totalydim = 20
xdim = 150
ydim = 2
xpos = 0
za = 80
cnt = 0
######################### INIT BOARD ##########################################################
sample = board(totalxdim,totalydim,xdim,ydim)
###############################################################################################

######################### INIT SETTINGS #######################################################
ismag = 0
speed = 0.01
initspeed = speed
initSettings = gameSettings(5,10)
initSettings._gameSettings__displaySettings(10,0,xpos,1,0)
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
    if cnt is 200:
        cnt = 0
        speed = initspeed
    if din._person__life <= 0:
        key = False
        os.system('reset')
        print("Thank you for playing! Do download our app on PlayStore")
        quit()
    e = give_me_character()
    if e is 'q':
            os.system('reset')
            print("Thank you for playing! Do download our app on PlayStore")
            quit()
    if e is 'b':
            prit
            din._person__shield = din._person__shield^1
    din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok,ismag,speed)
    if (time.time()-start>=speed):
        if speed < initspeed:
            cnt = cnt + 1
            # Move screen
        start = time.time()       
        if za%(xdim//2) is 0:
            sample._board__render_board(xpos+xdim,xpos+xdim+xdim//2)
        za = za + 1
        if e is 'q':
            os.system('reset')
            print("Thank you for playing! Do download our app on PlayStore")
            quit()
        if e is 'b':
            din._person__shield = din._person__shield^1
        ok = False
        din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok,ismag,speed)
        xpos = xpos + 1
        sample._board__display(xpos,xpos+xdim)
        initSettings._gameSettings__displaySettings(din._person__life,din._person__coins,xpos,din._person__xco,din._person__shield)
        print("\t||"+str(din._person__yco))
        din._person__vel = din._person__vel + 1 # Velocity increasing downward everytime
        if speed < initspeed:
            print("SPEED:"+str(speed)+"$")