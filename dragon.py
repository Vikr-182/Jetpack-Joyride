import os
import random
import signal
import numpy as np
from colorama import init,Fore,Back,Style
from board import *
from take_input import inputtake as inp
from alarmexception import AlarmException
from scenery import *
from character import *


class Drag(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)
        self.__f = ["" for i in range(4)]
        for i in range(4):
            self.__f[i] = extract("bonus"+str(i)+".txt").nikal()
        self.__counter = 0
    
    def get_alive(self):
        return person.__alive
    def set_alive(self,value):
        person.__alive = value
    
    def get_xco(self):
        return self._person__xco
    def set_xco(self,value):
        self._person__xco = value

    def get_yco(self):
        return self._person__yco
    def set_yco(self,value):
        self._person__yco = value
    
    def get_f(self):
        return self.__f
    def set_f(self,value):
        self.__f = value
    
    def get_counter(self):
        return self.__counter
    def set_counter(self,value):
        self.__counter = value

    def define_dragon(self,din,game_board,xpos):
        # Place a dragon at the board xpos position
        # print("ME CALLED " + str(xpos) + "||")
        for i in range(2):
            for k in range(3):
                game_board[self.get_yco()-2+i][self.get_xco()+16+k] = din.get_figure()[i][0][k]       
        for i in range(6):
            for j in range(24):
                if j < len(self.get_f()[self.get_counter()][i]):
                    game_board[i+self.get_yco()][xpos+1+j] = self.get_f()[self.get_counter()][i][j]
                else:
                    game_board[i+self.get_yco()][xpos+1+j] = " "
    
    def move_me(self,din,game_board,xpos,speed,command,move):
        # Now emit flames every 2 frames
        not_allowed_collision = [Fore.RED+"X"+Style.RESET_ALL,"P"]
        wall = ["|","_"]
        coins = [Fore.YELLOW + "O"+Style.RESET_ALL]
        powerup = [Fore.BLUE+">"+Style.RESET_ALL]
        for i in range(8):
            if game_board[self.get_yco()-2+i][self.get_xco()+24] in not_allowed_collision:
                din.set_dragon(0)
                correct_beams(game_board,self.get_yco()+i,self.get_xco()+24,0)
                return 
            elif game_board[self.get_yco()-2+i][self.get_xco()+24] in coins:
                din.set_coins(din.get_coins()+1)
            elif game_board[self.get_yco()-2+i][self.get_xco()+24] in powerup:
                speed[0] = 1
        for i in range(2):
            for k in range(3):
                game_board[self.get_yco()-2+i][self.get_xco()+1+16+k] = din.get_figure()[i][0][k]
        # Make back empty for this
        for i in range(2):
            game_board[self.get_yco()-2+i][self.get_xco()+16] = " "
        for i in range(6):
            for j in range(24):
                if j < len(self.get_f()[self.get_counter()][i]):
                    game_board[i+self.get_yco()][self.get_xco()+1+j] = self.get_f()[self.get_counter()][i][j]
                else:
                    game_board[i+self.get_yco()][self.get_xco()+1+j] = " "
        # Make back empty
        for i in range(6):
            game_board[self.get_yco()+i][self.get_xco()-1] = " "
            game_board[self.get_yco()+i][self.get_xco()] = " "
            game_board[self.get_yco()+i][self.get_xco()+speed[0]] = " "
        self.set_xco(self.get_xco()+1) 

        # Now check for command
        if command is "w":
            if self.get_yco() <= 4:
                return 
            # Check collision    
            for j in range(24):
                if game_board[self.get_yco()-3][self.get_xco()+j] in not_allowed_collision:
                    din.set_dragon(0)
                    correct_beams(game_board,self.get_yco()-3,self.get_xco()+j,0)
                    return 
                elif game_board[self.get_yco()-3][self.get_xco()+j] in coins:
                    din.set_coins(din.get_coins()+1)
                elif game_board[self.get_yco()-3][self.get_xco()+j] in powerup:
                    speed[0] = 1
            for i in range(2):
                for k in range(3):
                    game_board[self.get_yco()-2+i-1][self.get_xco()+16+k] = din.get_figure()[i][0][k]   
            for i in range(6):
                for j in range(24):
                    if j < len(self.get_f()[self.get_counter()][i]):
                        game_board[i+self.get_yco()-1][self.get_xco()+1+j] = self.get_f()[self.get_counter()][i][j]
                    else:
                        game_board[i+self.get_yco()-1][self.get_xco()+1+j] = " "

            for j in range(24):
                game_board[self.get_yco()+5][self.get_xco()+j] = " "
                # game_board[self.get_yco()+6][self.get_xco()+j] = " "
            self.set_yco(self.get_yco()-1)
        
        if command is "s":
            if self.get_yco() >= 12:
                return 
            # Check collision    
            for j in range(24):
                if game_board[self.get_yco()+6][self.get_xco()+j] in not_allowed_collision:
                    din.set_dragon(0)
                    correct_beams(game_board,self.get_yco()-3,self.get_xco()+j,0)
                    return 
                elif game_board[self.get_yco()+6][self.get_xco()+j] in coins:
                    din.set_coins(din.get_coins()+1)
                elif game_board[self.get_yco()+6][self.get_xco()+j] in powerup:
                    speed[0] = 1
            for i in range(2):
                for k in range(3):
                    game_board[self.get_yco()-1+i][self.get_xco()+16+k] = din.get_figure()[i][0][k]   
            for i in range(6):
                for j in range(24):
                    if j < len(self.get_f()[self.get_counter()][i]):
                        game_board[i+self.get_yco()+1][self.get_xco()+1+j] = self.get_f()[self.get_counter()][i][j]
                    else:
                        game_board[i+self.get_yco()+1][self.get_xco()+1+j] = " "

            for j in range(24):
                game_board[self.get_yco()][self.get_xco()+j] = " "
            self.set_yco(self.get_yco()+1)
            

     
    def remove_dragon(self,din,game_board,xpos):
        # Place din at the start position again
        for i in range(2):
            for k in range(3):
                game_board[self.get_yco()-2+i][self.get_xco()+16+k] = " "
        for i in range(6):
            for j in range(24):
                if j < len(self.get_f()[self.get_counter()][i]):
                    game_board[i+self.get_yco()][xpos+1+j] = " "
                else:
                    game_board[i+self.get_yco()][xpos+1+j] = " "
        for i in range(4):
            for j in range(3):
                game_board[14+i][xpos+1+j] = din.get_figure()[i][0][j]
        