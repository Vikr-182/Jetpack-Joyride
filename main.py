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
za = 0
cnt = 0
######################### INIT BOARD ##########################################################
sample = board(totalxdim,totalydim,xdim,ydim)
BOSS = Boss(totalxdim-80,2)
BOSS.define_boss(sample._board__board)
###############################################################################################

######################### INIT SETTINGS #######################################################
ismag = 0
move = 1
shieldcnt = 0
canhe = 1
powerup = 0
speed = 0.001
initspeed = speed
initSettings = gameSettings(5,10)
initSettings._gameSettings__displaySettings(10,0,xpos,1,0,BOSS)
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
    din._person__shield = canhe & din._person__shield 

    din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok,ismag,speed,din._person__shield,move)
    # print(str(time.time())+"||"+str(start))
    if (time.time()-start>=speed or za is 0):
        # Shield remove 
        if din._person__shield is 1:
            shieldcnt = shieldcnt + 1
        else:
            powerup = powerup + 1
        # Shieldcnt increased by speed seconds
        if shieldcnt > 10/speed:
            shieldcnt = 0
            din._person__shield = 0
            canhe = 0
        if powerup > 60/speed:
            canhe = 1  

        # if za is 2:
        #     print("HAHAHAHHA")
        #     move = 0

        if move is 0:
            BOSS.interact(sample._board__board,din._person__xco,din._person__yco,din)

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
        if BOSS._person__life <= 0:
            os.system('reset')
            print("Thank you for playing! Do download our app on PlayStore")
            quit()
        ok = False
        din.move_me(sample._board__board,e,xpos,din._person__xco,din._person__yco,xdim,ok,ismag,speed,din._person__shield,move)
        BOSS.move_bullets(sample._board__board,din)
        xpos = xpos + 1*move
        sample._board__display(xpos,xpos+xdim)
        initSettings._gameSettings__displaySettings(din._person__life,din._person__coins,xpos,din._person__xco,din._person__shield,BOSS)
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