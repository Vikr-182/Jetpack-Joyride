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
move = 0
speed = 0.001
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
        din._person__shield = din._person__shield^1
    if e is 'x':
        # Shoot bullets
        if din._person__xco+3 < xpos + xdim -2: # Append only if not at last
            din._person__bullets.append([din._person__xco+3,din._person__yco])
    din.move_bullets(sample._board__board,xpos,xdim,din._person__shield)

    din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok,ismag,speed,din._person__shield,move)
    # print(str(time.time())+"||"+str(start))
    if (time.time()-start>=speed or za is 0):
        if speed < initspeed:
            cnt = cnt + 1
            # Move screen
        start = time.time()       
        if za%(xdim//2) is 0:
            sample._board__render_board(xpos+xdim,xpos+xdim+xdim//2,ismag)
        za = za + 1
        if e is 'q':
            os.system('reset')
            print("Thank you for playing! Do download our app on PlayStore")
            quit()
        ok = False
        din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok,ismag,speed,din._person__shield,move)
        xpos = xpos + 1
        sample._board__display(xpos,xpos+xdim)
        initSettings._gameSettings__displaySettings(din._person__life,din._person__coins,xpos,din._person__xco,din._person__shield)
        print("\t||PP"+str(din._person__shield))
        din._person__vel = din._person__vel + 1 # Velocity increasing downward everytime
        
        # Shield activity
        if din._person__shield is 1:
            # Print the shield around Din
            for i in range(6):
                if din._person__yco-1+i > 2 and din._person__yco-1+i < totalydim-ydim and din._person__xco+4 < xpos + xdim - 3:
                    sample._board__board[din._person__yco-1+i][din._person__xco+4] = "L"
            for i in range(6):
                if din._person__yco-1+i > 2 and din._person__yco-1+i < totalydim-ydim and din._person__xco-1 > 1:
                    sample._board__board[din._person__yco-1+i][din._person__xco-2] = "L"
            for j in range(5):
                if din._person__yco-1 > 2 and din._person__xco-1+j < xpos + xdim - 3 and din._person__xco-1+j > 1:
                    sample._board__board[din._person__yco-1][din._person__xco-1+j] = "L"
            for j in range(5):
                if din._person__yco+4 < totalydim-ydim and din._person__xco-1+j < xpos + xdim - 3 and din._person__xco-1+j > 1:
                    sample._board__board[din._person__yco+4][din._person__xco-1+j] = "L"    