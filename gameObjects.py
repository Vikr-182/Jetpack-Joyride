import os
import random
import numpy as np
from colorama import init,Fore,Back,Style

class gameSettings:
    def __init__(self,lives,coins):
        self.__life = lives
        self.__paisa = coins
        self.__shield = False

    def displaySettings(self,life,coins,debug,debug2,sh,BOSS):
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
    
    def get_figure(self):
        return self.__figure
    def set_figure(self,value):
        self.__figure = value

    def get_ch(self):
        return self.__ch
    def set_ch(self,value):
        self.__ch = value

    def get_xdim(self):
        return self.__xdim
    def set_xdim(self,value):
        self.__xdim = value
    
    def get_ydim(self):
        return self.__ydim
    def set_ydim(self,value):
        self.__ydim = value

    def display(self,board,x1,x2,y1,y2):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if len(board[j])>i and len(self.__figure[j-y1])>i-x1:
                    board[j][i] = self.__figure[j-y1][i-x1]   

class coins_array_rect(figures):
    def __init__(self):
        self.__array = [[" " for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                self.__array[i][j]= "O"
        figures.__init__(self,self.__array,"O",5,3)
    
    def get_array(self,array):
        return self.__array
    def set_array(self,value):
        self.__array = value


class coins_array_circ(figures):
    def __init__(self):
        self.__array = [[" " for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                if i*i+j*j<=16:
                    self.__array[i][j]= "O"
        figures.__init__(self,self.__array,"O",5,5)
    def get_array(self,array):
        return self.__array
    def set_array(self,value):
        self.__array = value


class beams(figures):
    def __init__(self,flag):
        self.__beam = "X"
        self.__array = [[" " for i in range(4)] for j in range(4)]
        for i in range(4):
            for j in range(4):
                if i is j and flag is 0:            # 45 deg left
                    self.__array[i][j] = self.__beam
                elif i is 4-j and flag is 1:        # 45 deg right
                    self.__array[i][j] = self.__beam
                elif i is 0 and flag is 2:          # vertical
                    self.__array[i][j] = self.__beam
                elif j is 0 and flag is 3:          # horizontal
                    self.__array[i][j] = self.__beam
        figures.__init__(self,self.__array,self.__beam,4,4)

    def get_beam(self):
        return self.__beam
    def set_beam(self,value):
        self.__beam = value
    
    def get_array(self,array):
        return self.__array
    def set_array(self,value):
        self.__array = value

class magnet(figures):
    def __init__(self):
        self.__pop = "U"
        self.__array = []
        self.__array[0] = pop
        figures.__init__(self,array,pop,1,1)
    
    def get_pop(self):
        return pop
    def set_pop(self,value):
        self.__pop = value
    
    def get_array(self):
        return self.__array
    def set_array(self,value):
        self.__array = value