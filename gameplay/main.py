import os,signal,time
from playsound  import playsound
from colorama import init,Fore
from board import *
from character import *
from gameObjects import *
import numpy as np
from take_input import inputtake as KBHit
from alarmexception import AlarmException
from dragon import *
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
BOSS = Boss(totalxdim-100,2)
BOSS.define_boss(sample.get_board())
###############################################################################################

######################### INIT SETTINGS #######################################################
ismag = 0
move = 1
shieldcnt = 0
canhe = 1
karde = [0]
powerup = 0
speed = 0.001
meradragon = 0
initspeed = speed
initSettings = gameSettings(5,10)
initSettings.displaySettings(10,0,xpos,1,0,BOSS)
start = time.time()
Golu = Drag(1,14)
###############################################################################################

######################### INIT CHARACTERS #####################################################
vel = [0,0]
din = Mandalorian(1,totalydim-ydim-4)
din.define_mandalorian(sample.get_board(),1,totalydim-ydim-4)
sample.display(xpos,xpos+xdim)
###############################################################################################

os.system('aplay -qN ./sound/starwars.wav &')
while key is True:
    # playsound.playsound('ok.mp3')
    ok = True
    if cnt is 200:
        cnt = 0
        speed = initspeed
    if din.get_life() <= 0:
        key = False
        os.system('reset')
        print("You Lost!! \nThank you for playing! Do download our app on PlayStore")
        quit()
    e = give_me_character()
    if e is 'q':
        os.system('reset')
        print("Thank you for playing! Do download our app on PlayStore")
        quit()
    if e is ' ':
        din.set_shield(din.get_shield()^1)
    if e is 'x':
        # Shoot bullets
        if din.get_xco()+3 < xpos + xdim-2: # Append only if not at last
            din.get_bullets().append([din.get_xco()+3,din.get_yco()])
    if e is 'l':
        # Activate dragon
        meradragon = meradragon + 1
        if meradragon is 1:
            din.set_dragon(1)
            Golu.set_xco(xpos)
            Golu.set_yco(totalydim-6-2)
            Golu.define_dragon(din,sample.get_board(),xpos)
        else:
            din.set_dragon(0)
    if din.get_dragon() is 0:
        din.set_shield(canhe & din.get_shield() )
        interact_magnet(sample.get_board(),xpos,xdim,din)
        din.move_me(sample.get_board(),e,xpos,din.get_xco(),din.get_yco(),xdim,ok,ismag,karde,din.get_shield(),move)
    else:
        Golu.move_me(din,sample.get_board(),xpos,karde,e,move)
    # move = 0
    if (time.time()-start>=speed or za is 0):
        # Shield remove 
        print("|||"+str(karde[0])+"|||")
        if din.get_shield() is 1:
            shieldcnt = shieldcnt + 1
        else:
            powerup = powerup + 1
        # Shieldcnt increased by speed seconds
        if shieldcnt > 10/speed:
            shieldcnt = 0
            din.set_shield(0)
            canhe = 0
        if powerup > 60/speed:
            canhe = 1  

        if xpos >= totalxdim-200:
            move = 0

        print("self sheild"+str(din.get_shield()))
        if move is 0:
            BOSS.interact(sample.get_board(),din.get_xco(),din.get_yco(),din)

        if speed < initspeed:
            cnt = cnt + 1
            # Move screen
        start = time.time()       
        if za%(xdim//2) is 0:
            sample.render_board(xpos+xdim,xpos+xdim+xdim//2,ismag)
        za = za + 1
        if e is 'q':
            os.system('reset')
            print("Thank you for playing! Do download our app on PlayStore")
            quit()            
        if BOSS.get_life() <= 0:
            os.system('reset')
            print("You won!!Thank you for playing! Do download our app on PlayStore")
            quit()
        ok = False

        if din.get_dragon() is 0 and meradragon is 1:
            Golu.remove_dragon(din,sample.get_board(),xpos)
            meradragon = meradragon + 1
            din.set_dragon(0)

        if din.get_dragon() is 0:
            din.set_shield(canhe & din.get_shield() )
            interact_magnet(sample.get_board(),xpos,xdim,din)
            din.move_me(sample.get_board(),e,xpos,din.get_xco(),din.get_yco(),xdim,ok,ismag,karde,din.get_shield(),move)
        else:
            Golu.set_counter((Golu.get_counter()+1)%4)

        din.move_bullets(sample.get_board(),xpos,xdim,din.get_shield(),karde)
        BOSS.move_bullets(sample.get_board(),din)
        xpos = xpos + 1*move+karde[0]*move
        sample.display(xpos,xpos+xdim)
        initSettings.displaySettings(din.get_life(),din.get_coins(),xpos,din.get_xco(),din.get_shield(),BOSS)
        din.set_vel(din.get_vel() + 1)  # Velocity increasing downward everytime


############################################################################## SHIELD ##################################################################################
        # Shield activity
        if din.get_shield() is 1:
            # Print the shield around Din
            for i in range(6):
                if din.get_yco()-1+i > 2 and din.get_yco()-1+i < totalydim-ydim and din.get_xco()+4 < xpos + xdim - 3:
                    sample._board__board[din.get_yco()-1+i][din.get_xco()+4] = "L"
            for i in range(6):
                if din.get_yco()-1+i > 2 and din.get_yco()-1+i < totalydim-ydim and din.get_xco()-1 > 1:
                    sample._board__board[din.get_yco()-1+i][din.get_xco()-2] = "L"
            for j in range(5):
                if din.get_yco()-1 > 2 and din.get_xco()-1+j < xpos + xdim - 3 and din.get_xco()-1+j > 1:
                    sample._board__board[din.get_yco()-1][din.get_xco()-1+j] = "L"
            for j in range(5):
                if din.get_yco()+4 < totalydim-ydim and din.get_xco()-1+j < xpos + xdim - 3 and din.get_xco()-1+j > 1:
                    sample._board__board[din.get_yco()+4][din.get_xco()-1+j] = "L"    
