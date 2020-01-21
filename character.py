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
        self.__life = 10
        self.__coins = 0
        self.__vel = 0 # Velocity along y direction ( either 1+ or (var)-)
        self.__shield = 0
        
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


    def correct_beams(self,game_board,x,y,flag):
        if flag is 0:
            # from right side
            for i in range(4):
                game_board[y+i][x+3] = " "  
        elif flag is 1:
            # from left
            for i in range(4):
                game_board[y+i][x-1] = " "
        elif flag is 2:
            # from up
            for j in range(3):
                game_board[y-1][x+j] = " "
        elif flag is 3:
            # from down
            for j in range(3):
                game_board[y+4][x+j] = " "

    def move_me(self,game_board,command,xpos,x,y,xdim,ij,mag,speed):
        # Last position move forward by one column
        not_allowed_collision = ["\u274c","<"]
        wall = ["|","_"]
        coins = ["\U0001F315"]
        powerup = ["\u23e9"]
        array = [[" " for i in range(3)] for j in range(4)]
        if ij is True:
            ij = False
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[y+i][self._person__xco+j]
            for i in range(4):
                if game_board[y+i][self._person__xco+3] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                elif game_board[y+i][self._person__xco+3] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[y+i][self._person__xco+3] in powerup:
                    print("YYYYAAAAAAAAAAAAYYYYYYYY"+str(speed)+"||")
                    speed = speed/100    
                    print("NNNNNNNNNNNOWWWWWWWWWWWW"+str(speed)+"<<")
                
            for i in range(4):
                for j in range(3):
                    game_board[y+i][self._person__xco+j+1] = array[i][j]
            if self._person__xco is not 1:
                # Make back empty
                for i in range(4):
                    game_board[y+i][self._person__xco-1] = " "
            self._person__xco = self._person__xco + 1


        if command is 'w' or command is '\33[A':
            # Move up
            b = 0
            # print(str(x)+"lola"+str(y)) 
            flag = 0
            self._person__vel = 0
            if self._person__yco <= 2:
                return # Dont move
            elif self._person__yco is 10:
                # print("HULA HULA")
                bv = 0
            for i in range(3):
                if game_board[y-1][self._person__xco+i] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                    self.correct_beams(game_board,self._person__xco,self._person__yco,2)
                elif game_board[y-1][self._person__xco+i] in coins:
                    self._person__coins = self._person__coins + 1
                elif game_board[y-1][self._person__xco+i] in powerup:
                    print("YYYYAAAAAAAAAAAAYYYYYYYY"+str(speed)+"||")
                    speed = speed/100    
                    print("NNNNNNNNNNNOWWWWWWWWWWWW"+str(speed)+"<<")
            # move up
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i-1][self._person__xco+j] = array[i][j]
            if self._person__yco is not (18):
                for j in range(3):
                    game_board[self._person__yco+3][self._person__xco+j] = " "
            self._person__yco = self._person__yco - 1
            print("Now "+ str(self._person__yco)+"|")
         

        if command is 'a' or command is '\33[D':
            # Move left
            j = 0
            if self._person__xco <= (xpos+2):
                t = 0 # Dont move
                return
            
            for i in range(4):
                if game_board[self._person__yco+i][self._person__xco-1] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                elif game_board[self._person__yco+i][self._person__xco-1] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[self._person__yco+i][self._person__xco-1] in powerup:
                    print("YYYYAAAAAAAAAAAAYYYYYYYY"+str(speed)+"||")
                    speed = speed/100    
                    print("NNNNNNNNNNNOWWWWWWWWWWWW"+str(speed)+"<<")
        
            # Move left
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i][self._person__xco+j-1] = array[i][j]
            if self._person__xco is not (xpos+xdim-4):
                for i in range(4):
                    game_board[y+i][self._person__xco+4] = " "
            self._person__xco = self._person__xco - 1
            
        if command is 's' or command is '\33[B':
            # Move down
            k =  1
            if self._person__yco is 14:
            #     print("OOOOOOOOO")
                return # Dont move
            for i in range(3):
                if game_board[self._person__yco+4][self._person__xco+i] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                    self.correct_beams(game_board,self._person__xco,self._person__yco,3)
                elif game_board[self._person__yco+4][self._person__xco+i] in coins:
                    self._person__coins = self._person__coins + 1           
                elif game_board[self._person__yco+4][self._person__xco+i] in powerup:
                    print("YYYYAAAAAAAAAAAAYYYYYYYY"+str(speed)+"||")
                    speed = speed/100    
                    print("NNNNNNNNNNNOWWWWWWWWWWWW"+str(speed)+"<<")
            # move down
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i+1][self._person__xco+j] = array[i][j]
            if self._person__yco is not (14):
                for j in range(3):
                    game_board[self._person__yco][self._person__xco+j] = " "
            self._person__yco = self._person__yco + 1
        

        if command is 'd' or command is '\33[C':
            # Move right
            g = 0
            if self._person__xco >= (xpos+xdim-3):
                t = 0 # Dont move
                # print("AAAAAAAAAAAAAA")
                return
            for i in range(4):
                if game_board[y+i][self._person__xco+3] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                elif game_board[y+i][self._person__xco+3] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[y+i][self._person__xco+3] in powerup:
                    print("YYYYAAAAAAAAAAAAYYYYYYYY"+str(speed)+"||")
                    speed = speed/100    
                    print("NNNNNNNNNNNOWWWWWWWWWWWW"+str(speed)+"<<")
            # Move right
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i][self._person__xco+j+1] = array[i][j]
            if self._person__xco is not 1:
                for i in range(4):
                    game_board[y+i][self._person__xco-1] = " "
            self._person__xco = self._person__xco + 1
            
    #    # Act gravity 
        final = min(self._person__vel,14-self._person__yco)
        # Move it final times down
        for i in range(final):
            for j in range(3):
                if game_board[self._person__yco+i][self._person__xco+j] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                    correct_beams(game_board,self._person__xco,self._person__yco+i,3)
                elif game_board[self._person__yco+i][self._person__xco+j] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[self._person__yco+i][self._person__xco+j] in powerup:
                    print("YYYYAAAAAAAAAAAAYYYYYYYY"+str(speed)+"||")
                    speed = speed/100    
                    print("NNNNNNNNNNNOWWWWWWWWWWWW"+str(speed)+"<<")
        #     # Move 1 down
            array = [[" " for i in range(3)] for j in range(4)]
            for ii in range(4):
                for jj in range(3):
                    array[ii][jj] = game_board[self._person__yco+ii+i][self._person__xco+jj]
            for ii in range(4):
                for jj in range(3):
                    game_board[self._person__yco+ii+i+1][self._person__xco+jj] = array[ii][jj]
            if self._person__yco is not (14):
                for jj in range(3):
                    game_board[self._person__yco+i][self._person__xco+jj] = " "
        self._person__yco += final
            
        

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
