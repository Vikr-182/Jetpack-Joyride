import os
import random
import numpy as np
from colorama import init,Fore,Back,Style

class gameSettings:
    def __init__(self,lives,coins):
        self._life = lives
        self._paisa = coins
        self._shield = False

    def displaySettings(self,life,coins,debug,debug2,sh,BOSS):
        print("Number of Lives left: ",end="")
        print(str(life),end="")
        # for i in range(life):
        #     print("\u2665",end="")
        print("\t",end="")
        print("||Number of Coins Earned: ",end="")
        print(coins,end="")
        print("\t",end="")
        print("||BOSS:\t",end="")
        print(str(BOSS.get_life())+str("||"),end="")
        print("\t||Shield Activated:",end="")
        print(sh)
        print("\t" + str(debug))
        print("\t"+str(debug2))

class figures:
    def __init__(self,initarray,character,xdim,ydim):
        self._figure = initarray
        self._ch = character
        self._xdim = xdim
        self._ydim = ydim
    
    def get_figure(self):
        return self._figure
    def set_figure(self,value):
        self._figure = value

    def get_ch(self):
        return self._ch
    def set_ch(self,value):
        self._ch = value

    def get_xdim(self):
        return self._xdim
    def set_xdim(self,value):
        self._xdim = value
    
    def get_ydim(self):
        return self._ydim
    def set_ydim(self,value):
        self._ydim = value

    def display(self,board,x1,x2,y1,y2):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if len(board[j])>i and len(self._figure[j-y1])>i-x1:
                    board[j][i] = self._figure[j-y1][i-x1]   

class coins_array_rect(figures):
    def __init__(self):
        self._array = [[" " for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                self._array[i][j]= Fore.YELLOW+"O"+Style.RESET_ALL
        figures.__init__(self,self._array,Fore.YELLOW+"O"+Style.RESET_ALL,5,3)
    
    def get_array(self,array):
        return self._array
    def set_array(self,value):
        self._array = value


class coins_array_circ(figures):
    def __init__(self):
        self._array = [[" " for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                if i*i+j*j<=16:
                    self._array[i][j]= Fore.YELLOW+"O"+Style.RESET_ALL
        figures.__init__(self,self._array,Fore.YELLOW+"O"+Style.RESET_ALL,5,5)
    def get_array(self,array):
        return self._array
    def set_array(self,value):
        self._array = value


class beams(figures):
    def __init__(self,flag):
        self._beam = Fore.RED+"X"+Style.RESET_ALL
        self._array = [[" " for i in range(4)] for j in range(4)]
        for i in range(4):
            for j in range(4):
                if i is j and flag is 0:            # 45 deg left
                    self._array[i][j] = self._beam
                elif i is 4-j and flag is 1:        # 45 deg right
                    self._array[i][j] = self._beam
                elif i is 0 and flag is 2:          # vertical
                    self._array[i][j] = self._beam
                elif j is 0 and flag is 3:          # horizontal
                    self._array[i][j] = self._beam
        figures.__init__(self,self._array,self._beam,4,4)

    def get_beam(self):
        return self._beam
    def set_beam(self,value):
        self._beam = value
    
    def get_array(self,array):
        return self._array
    def set_array(self,value):
        self._array = value

class magnet(figures):
    def __init__(self):
        self._pop = Fore.RED+Back.WHITE+"U"+Style.RESET_ALL
        self._array = []
        self._array[0] = pop
        figures.__init__(self,array,pop,1,1)
    
    def get_pop(self):
        return pop
    def set_pop(self,value):
        self._pop = value
    
    def get_array(self):
        return self._array
    def set_array(self,value):
        self._array = value