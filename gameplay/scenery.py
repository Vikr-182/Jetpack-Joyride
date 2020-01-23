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

class extract:
    def __init__(self,file_name):
        a = 0 # Random
        self.__filename = file_name
    def nikal(self):
        file = open(self.__filename)
        cnt = 0
        array = []
        for each in file:
            array.append(str(each))
        barray = [[] for i in range(len(array))]
        maxi = -1
        for i in range(len(array)):
            if maxi < len(array[i]):
                maxi = len(array[i])
        for i in range(len(array)):
            for j in range(maxi):
                if j >= len(array[i]):
                    barray[i].append(" ")
                else:
                    barray[i].append(array[i][j])
        return array

def correct_beams(game_board,yy,xx,flag):
    # Disappear The beam responsible for this 
    anna = 1
    sup = 0
    y = yy
    x = xx
    game_board[y][x] = Fore.RED+"X"+Style.RESET_ALL
    while anna is 1 and sup < 3:
        # sup = sup + 1
        # print("PPT "+str(x)+"|"+str(y)+"|"+game_board[y][x])
        if game_board[y-1][x]==Fore.RED+"X"+Style.RESET_ALL and (yy!=y-1 or xx!=x):
            # print("A")
            y = y - 1
            game_board[y][x] = " "
            continue
        elif game_board[y+1][x]==Fore.RED+"X"+Style.RESET_ALL and (yy!=y+1 or xx!=x):
            # print("B")
            y = y + 1
            game_board[y][x] = " "
            print(game_board[y][x])
            continue
        elif game_board[y][x-1]==Fore.RED+"X"+Style.RESET_ALL and (yy!=y or xx!=x-1):
            # print("C")
            x = x - 1
            game_board[y][x] = " "
            continue
        elif game_board[y][x+1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y or xx!=x+1):
            # print("D")
            x = x + 1
            game_board[y][x] = " "
            continue
        elif game_board[y-1][x-1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y-1 or xx!=x-1):
            # print("E")
            x = x - 1
            y = y - 1
            game_board[y][x] = " "
            continue
        elif game_board[y-1][x+1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y-1 or xx!=x+1):
            # print("F")
            x = x + 1
            y = y - 1
            game_board[y][x] = " "
            continue
        elif game_board[y+1][x+1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y+1 or xx!=x+1):
            # print("G")
            x = x + 1
            y = y + 1
            game_board[y][x] = " "
            continue
        elif game_board[y+1][x-1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y+1 or xx!=x-1):
            # print("G")
            x = x - 1
            y = y + 1
            game_board[y][x] = " "
            continue
        else:
            anna = 0
    anna = 1
    game_board[yy][xx] = " "
    y = yy
    x = xx
    while anna is 1 and sup < 3:
        # sup = sup + 1
        # print("TOT "+str(x)+"|"+str(y)+"|"+game_board[7][100])
        if game_board[y-1][x] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y-1 or xx!=x):
            # print("A")
            y = y - 1
            game_board[y][x] = " "
            continue
        elif game_board[y+1][x] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y+1 or xx!=x):
            # print("B")
            y = y + 1
            game_board[y][x] = " "
            print(game_board[y][x])
            continue
        elif game_board[y][x-1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y or xx!=x-1):
            # print("C")
            x = x - 1
            game_board[y][x] = " "
            continue
        elif game_board[y][x+1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y or xx!=x+1):
            # print("D")
            x = x + 1
            game_board[y][x] = " "
            continue
        elif game_board[y-1][x-1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y-1 or xx!=x-1):
            # print("E")
            x = x - 1
            y = y - 1
            game_board[y][x] = " "
            continue
        elif game_board[y-1][x+1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y-1 or xx!=x+1):
            # print("F")
            x = x + 1
            y = y - 1
            game_board[y][x] = " "
            continue
        elif game_board[y+1][x+1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y+1 or xx!=x+1):
            # print("G")
            x = x + 1
            y = y + 1
            game_board[y][x] = " "
            continue
        elif game_board[y+1][x-1] ==Fore.RED+"X"+Style.RESET_ALL and (yy!=y+1 or xx!=x-1):
            print("G")
            x = x - 1
            y = y + 1
            game_board[y][x] = " "
            continue
        else:
            anna = 0