import os
import random
import numpy as np
from colorama import init,Fore,Back,Style
from gameObjects import *

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
                    self.__board[i][j] = Back.RED + '|'
                else:   
                    self.__board[i][j] = Back.GREEN + '_'

    def __display(self,x1,x2):
        print("GOT "+str(x1)+" "+str(x2))
        for i in range(self.__ylim):
            for j in range(x1,x2+1):
                print(self.__board[i][j],end="")
            print()

    def __change_at(self,x,y,char):
        self.__board[x][y] = char
        print("\033["+str(y)+";"+str(x)+"H"+char)

    def render_board(self,x,y):
        
