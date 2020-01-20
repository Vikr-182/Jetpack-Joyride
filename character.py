import os
import random
import signal
import numpy as np
from colorama import init,Fore,Back,Style
from board import *
from take_input import inputtake as inp
from alarmexception import AlarmException

class person():
    def __init__(self,x_cordinate,y_cordinate):
        self.__xco = x_cordinate
        self.__yco = y_cordinate
        # self.__vel[0] = velocity[0] # Along x-axis
        # self.__vel[1] = velocity[1] # Along y-axis
   
class Mandalorian(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)
        person.__figure = [[["<","O","|"],["|","O",">"]],
                         [[" ","|"," "],[" ","|"," "]],
                         [["/","|"," "],[" ","|","\\"]],
                        [["|"," ","\\"],["/"," ","|"]]]
        person.__alive = True

    def define_mandalorian(self,game_board,x,y):
        a = 0
        if a >= 0: # Moving forward
            for i in range(4):
                for j in range(3):
                    game_board[y+i][x+j] = person.__figure[i][1][j]

        elif a < 0: # Moving forward
            for i in range(4):
                for j in range(3):
                    game_board[y+i][x+j] = person.__figure[i][0][j]

    def move_me(self,game_board,command,xpos,x,y):
        if self._person__xco is (xpos+1):
            # Last position move forward by one column
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[y+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[y+i][self._person__xco+j+1] = array[i][j]
            self._person__xco = self._person__xco + 1

        if command is 'w' or command is '\33[A':
            # Move up
            b = 0
            # print(str(x)+"lola"+str(y)) 
            move_up()
        if command is 'a' or command is '\33[D':
            # Move left
            j = 0
        if command is 's' or command is '\33[B':
            # Move down
            k = 0
        if command is 'd' or command is '\33[C':
            # Move right
            g = 0

class Boss(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)

def give_me_character():
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
                return ' '

        char = user_input()
        # if char is 'A':
        #     print("Madarchod bottle sar pe phodunga")
        return char
