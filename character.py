import os
import random
import numpy as np
from colorama import init,Fore,Back,Style
from board import *
from take_input import _inputtake as inp

class person():
    def __init__(self,x_cordinate,y_cordinate,velocity):
        self.__xco = x_cordinate
        self.__yco = y_cordinate
        self.__vel[0] = velocity[0] # Along x-axis
        self.__vel[1] = velocity[1] # Along y-axis
   
class Mandalorian(person):
    def __init__(self,xco,yco,vel):
        person.__init__(self,xco,yco,vel)
        person.__figure = [[["<","O","|"],["|","O",">"]],
                         [[" ","|"," "],[" ","|"," "]],
                         [["/","|"," "],[" ","|","\\"]],
                        [["|"," ","\\"],["/"," ","|"]]]
        person.__alive = True

    def define_mandalorian(self,game_board):
        if self.__vel[1] >= 0: # Moving forward
            for i in range(4):
                for j in range(3):
                    print(person.__figure[i][1][j],end="")
                print()
        elif self.__vel[1] >= 0: # Moving forward
            for i in range(4):
                for j in range(3):
                    print(person.__figure[i][0][j],end="")
                print()

class Boss(person):
    def __init__(self,xco,yco,vel):
        person.__init__(self,xco,yco,vel)

def movemario():
        def alarmhandler(signum, frame):
                raise AlarmException

        def user_input(timeout=0.15):
                signal.signal(signal.SIGALRM, alarmhandler)
                signal.setitimer(signal.ITIMER_REAL, timeout)
                try:
                        text = inp()()
                        signal.alarm(0)
                        return text
                except AlarmException:
                        pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''

        char = user_input()
        print("PPPP")
        print(char)
        print("HHHIIII")
