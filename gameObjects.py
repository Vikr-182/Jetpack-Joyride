import os
import random
import numpy as np
from colorama import init,Fore,Back,Style

class gameSettings:
    def __init__(self,lives,coins):
        self.__life = lives
        self.__paisa = coins
        self.__shield = False

    def __displaySettings(self,life,coins,debug,debug2,sh,BOSS):
        print("Number of Lives left: ",end="")
        print(str(life),end="")
        # for i in range(life):
        #     print("\u2665",end="")
        print("\t",end="")
        print("Number of Coins Earned: ",end="")
        print(coins,end="")
        print("\t",end="")
        print("BOSS:\t",end="")
        print(str(BOSS._person__life)+str("||"),end="")
        print("Shield Activated:",end="")
        print(sh)
        print("\t" + str(debug))
        print("\t"+str(debug2))

class figures:
    def __init__(self,initarray,character,xdim,ydim):
        self.__figure = initarray
        self.__ch = character
        self.__xdim = xdim
        self.__ydim = ydim

    def display(self,board,x1,x2,y1,y2):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                board[j][i] = self.__figure[j-y1][i-x1]   

class coins_array_rect(figures):
    def __init__(self):
        array = [[" " for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                array[i][j]= "O"
        figures.__init__(self,array,"O",5,3)

class coins_array_circ(figures):
    def __init__(self):
        array = [[" " for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                if i*i+j*j<=16:
                    array[i][j]= "O"
        figures.__init__(self,array,"O",5,5)

class beams(figures):
    def __init__(self,flag):
        beam = "X"
        array = [[" " for i in range(4)] for j in range(4)]
        for i in range(4):
            for j in range(4):
                if i is j and flag is 0:            # 45 deg left
                    array[i][j] = beam
                elif i is 4-j and flag is 1:        # 45 deg right
                    array[i][j] = beam
                elif i is 0 and flag is 2:          # vertical
                    array[i][j] = beam
                elif j is 0 and flag is 3:          # horizontal
                    array[i][j] = beam
        figures.__init__(self,array,beam,4,4)

class magnet(figures):
    def __init__(self):
        pop = "U"
        array = []
        array[0] = pop
        figures.__init__(self,array,pop,1,1)