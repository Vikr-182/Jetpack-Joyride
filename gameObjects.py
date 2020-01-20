import os
import random
import numpy as np
from colorama import init,Fore,Back,Style

class gameSettings:
    def __init__(self,lives,coins):
        self.__life = lives
        self.__paisa = coins
        self.__shield = False

    def __displaySettings(self):
        print("Number of Lives left:",end="")
        for i in range(self.__life):
            print("\u2665",end="")
        print("\t",end="")
        print("Number of Coins Earned:",end="")
        print(self.__paisa,end="")
        print("$\t",end="")
        print("Shield Activated:",end="")
        print(self.__shield)

class figures:
    def __init__(self,initarray,character,xdim,ydim):
        self.__figure = initarray
        self.__ch = character
        self.__xdim = xdim
        self.__ydim = ydim

    def display(board,x1,x2,y1,y2):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                board[j][i] = self.__figure[j-y1][i-x1]   

class coins_array_rect(figures):
    def __init__(self):
        array = [["\U0001F315" for i in range(5)],
                ["\U0001F315" for i in range(5)],
                ["\U0001F315" for i in range(5)]]
        figures.__init__(self,array,"\U0001F315",5,3)

class coins_array_circ(figures):
    def __init__(self):
        array = [[" " for i in range(3)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                if i*i+j*j<=16:
                    array[i][j]= ["\U0001F315"]
        figures.__init__(self,array,"\U0001F315",5,5)
