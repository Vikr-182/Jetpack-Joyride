import os
import random
import numpy as np
from colorama import init,Fore,Back,Style
from gameObjects import *
from character import *
from scenery import *

class board():
    def __init__(self,x,y,xb,yb):
        self.__ylim = y
        self.__xlim = xb
        self.__board = [[" " for j in range(0,x)] for i in range(0,y)]
        self.__border = yb
        up = yb
        for i in range(y):
            for j in range(x):
                if i in range(up,self.__ylim-up) : # play screen
                    self.__board[i][j] = Style.RESET_ALL+' '
                elif i in range(0,up+1):  # top border
                    self.__board[i][j] = Back.RED + '|'+Style.RESET_ALL
                else:   
                    self.__board[i][j] = Back.GREEN + '_'+Style.RESET_ALL
        self.__board[2][52] = "\u23e9"  
        self.__board[3][53] = "\u23e9"  
        self.__board[4][54] = "U"  
        self.__board[5][55] = "X"  

        # Prepare the boss at the last 75 characters 
        
    def __display(self,x1,x2):
        for i in range(self.__ylim):
            for j in range(x1,x2+1):
                print("\033["+str(i)+";"+str(j-x1)+"H"+self.__board[i-1][j])
            print()

    def __change_at(self,x,y,char):
        self.__board[x][y] = char
        print("\033["+str(y)+";"+str(x)+"H"+char)
    
    def __render_board(self,x,xx,ismag):       # Randomly renders the next 100 characters in the board
######################### COINS ###############################################################
        # Place piece of coins in the board
        a = random.randint(0,1)
        # Choose coordinates for coin placage
        yco1 = random.randint(self.__border+1,self.__ylim-self.__border-5)
        xco1 = random.randint(x,xx-6)
        yco2 = random.randint(self.__border+1,self.__ylim-self.__border-5)
        xco2 = random.randint(x,xx-6)

        # Render at these coordinates
        coins_array_circ().display(self.__board,xco1,xco1+4,yco1,yco1+4)
        coins_array_rect().display(self.__board,xco2,xco2+4,yco2,yco2+4)
###############################################################################################

######################### OBSTACLES ###########################################################
        for i in range(7):
            yco1 = random.randint(self.__border+1,self.__ylim-self.__border-5)
            xco1 = random.randint(x,xx-5)
            flag = random.randint(0,3)
            a = beams(flag)
            a.display(self.__board,xco1,xco1+3,yco1,yco1+3)
###############################################################################################

######################### MAGNETS #############################################################
        d = random.randint(0,5)
        if d is 2 or d is 4:
            # put a magnet
            j = 0    
            yco1 = random.randint(self.__border+1,self.__ylim-self.__border-5)
            xco1 = random.randint(x,xx-5)
            # Place at these coordinates
            self.__board[yco1][xco1] = "U"
            ismag = True
        else:
            ismag = False
###############################################################################################

######################### FASTFOR #############################################################
        d = random.randint(0,2)
        if d is 1:
            # put a fast forward
            yco1 = random.randint(self.__border+1,self.__ylim-self.__border-5)
            xco1 = random.randint(x,xx-5)
            # Place at these coordinates
            self.__board[yco1][xco1] = "\u23e9"
###############################################################################################
