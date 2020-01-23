import os
import random
import signal
import numpy as np
from colorama import init,Fore,Back,Style
from board import *
from take_input import inputtake as inp
from alarmexception import AlarmException
from scenery import *
odd = 0

class person():
    def __init__(self,x_cordinate,y_cordinate):
        self.__xco = x_cordinate
        self.__yco = y_cordinate
        self.__life = 10
        self.__coins = 0
        self.__vel = 0 # Velocity along y direction ( either 1+ or (var)-)
        self.__shield = 0
        self.__bullets = []
        
class Mandalorian(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)
        person.__figure = [[["<","M","|"],["|","M",">"]],
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


    
    def move_bullets(self,game_board,xpos,xdim, iiifag,speed):
        # Make this move to next, while shooting down beams in this process
         for i in range(len(self._person__bullets)):
             # Move this 
            if len(self._person__bullets) <= i:
                continue
            x = self._person__bullets[i][0]
            y = self._person__bullets[i][1]
            wall = ["|","_"]
            coins = ["O"]
            powerup = ["\u23e9"]
            save = game_board[y][x+1]
            not_allowed_collision = ["X","P"]
            for j in range(1+speed[0]):
                if game_board[y][x+2+j] in coins or game_board[y][x+2+j] in powerup or game_board[y][x+1+j] in coins or game_board[y][x+1+j] in powerup:
                    # Do nothing
                    b = 0
                elif game_board[y][x+2+j] in not_allowed_collision:
                    correct_beams(game_board,y,x+2+j,0)
                    if len(self._person__bullets)>=1:
                        self._person__bullets.pop(i)
                    game_board[y][x+2+j] = " "
                    game_board[y][x+1+j] = " "
                    game_board[y][x+j] = " "
                    continue
                elif game_board[y][x+1+j] in not_allowed_collision:
                    correct_beams(game_board,y,x+2+j,0)
                    self._person__bullets.pop(i)
                    game_board[y][x+1+j] = " "
                    game_board[y][x+j] = " "
                    continue
                else:
                    game_board[y][x+2+speed[0]] = "*"
                    game_board[y][x] = save
                if len(self._person__bullets) > i:
                    self._person__bullets[i][0] = self._person__bullets[i][0] + 2*(j^1)+j
                if len(self._person__bullets) > i and self._person__bullets[i][0]  >= xpos + xdim : # Rmove it from frame
                    game_board[self._person__bullets[i][1]][self._person__bullets[i][0]] = " "
                    self._person__bullets.pop(i)


    def move_me(self,game_board,command,xpos,x,y,xdim,ij,mag,speed,fag,move):
        # Last position move forward by one column
        not_allowed_collision = ["X","P"]
        wall = ["|","_"]
        coins = ["O"]
        powerup = ["\u23e9"]
        array = [[" " for i in range(3)] for j in range(4)]
        if ij is True and fag is 0 and move is 1:
            ij = False
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[y+i][self._person__xco+j]
            for i in range(4):
                for j in range(1+speed[0]):
                    if game_board[y+i][self._person__xco+3+j] in not_allowed_collision:
                        self._person__life = self._person__life - 1
                        correct_beams(game_board,y+i,self._person__xco+j+3,0)
                    elif game_board[y+i][self._person__xco+j+3] in coins:
                        # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                        self._person__coins = self._person__coins + 1
                    elif game_board[y+i][self._person__xco+j+3] in powerup:
                        print("BBBBBBBBBBBBBBBBBBBBBBBB"+str(speed[0])+"||")
                        speed[0] = 1
                        print("DDDDDDDDDDDDDDDDDDDDDDDD"+str(speed[0])+"<<")
                
            for i in range(4):
                for j in range(3):
                        game_board[y+i][self._person__xco+j+1+speed[0]] = person.__figure[i][0][j]
            if self._person__xco is not 1:
                # Make back empty
                for i in range(4):
                    game_board[y+i][self._person__xco-1] = " "
                    game_board[y+i][self._person__xco] = " "
                    game_board[y+i][self._person__xco+speed[0]] = " "
            self._person__xco = self._person__xco + 1 + speed[0]

        if ij is True and fag is 1 and move is 1:
            ij = False
            # Effective dimension is 5 x 4
            array = [[" " for i in range(5)] for j in range(6)]
            for i in range(6):
                for j in range(5):
                    array[i][j] = game_board[y-1+i][self._person__xco-1+j]
            for i in range(6):
                if game_board[y-1+i][self._person__xco+4] in not_allowed_collision:
                    fag = 0
                    correct_beams(game_board,y-1+i,self._person__xco+4,0)
                    print("SHIELD LOST")
                elif game_board[y-1+i][self._person__xco+4] in coins:
                    self._person__coins = self._person__coins + 1
                elif game_board[y-1+i][self._person__xco+4] in powerup:
                    speed[0] = 1
                 
            for i in range(5):
                for j in range(4):
                    game_board[y-1+i][self._person__xco-1+j+1] = array[i][j]
            if self._person__xco is not 1:
                # Make back empty
                for i in range(5):
                    game_board[y-1+i][self._person__xco-2] = " "
            self._person__xco = self._person__xco + 1
                                        

        if command is 'w' or command is '\33[A':
            # Move up
            b = 0
            flag = 0
            self._person__vel = 0
            if self._person__yco <= 2:
                return # Dont move
            elif self._person__yco is 10:
                bv = 0
            for i in range(3):
                if game_board[y-1][self._person__xco+i] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                    correct_beams(game_board,y-1,self._person__xco+i,0)
                elif game_board[y-1][self._person__xco+i] in coins:
                    self._person__coins = self._person__coins + 1
                elif game_board[y-1][self._person__xco+i] in powerup:
                    print("NNNNNNNNNNNNNNNNNNNNNNNNNN")
                    speed[0] = 1
                    print("OOOOOOOOOOOOOOOOOOOOOOOOOO")
            # move up
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i-1][self._person__xco+j] = person.__figure[i][0][j]
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
                    correct_beams(game_board,self._person__yco+i,self._person__xco-1,0)
                elif game_board[self._person__yco+i][self._person__xco-1] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[self._person__yco+i][self._person__xco-1] in powerup:
                    print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
                    speed[0] = 1
                    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                
            # Move left
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i][self._person__xco+j-1] = person.__figure[i][0][j]
            if self._person__xco is not (xpos+xdim-4):
                for i in range(4):
                    game_board[y+i][self._person__xco+2] = " "
                    game_board[y+i][self._person__xco+3] = " "
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
                    correct_beams(game_board,self._person__yco+4,self._person__xco+i,3)
                elif game_board[self._person__yco+4][self._person__xco+i] in coins:
                    self._person__coins = self._person__coins + 1           
                elif game_board[self._person__yco+4][self._person__xco+i] in powerup:
                    print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
                    speed[0] = 1  
                    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
            # move down
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i+1][self._person__xco+j] = person.__figure[i][0][j]
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
                    correct_beams(game_board,y+i,self._person__xco+3,3)
                elif game_board[y+i][self._person__xco+3] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[y+i][self._person__xco+3] in powerup:
                    print("YYYYYYYYYYYYYYYYYYYYYYYY"+str(speed[0])+"||")
                    speed[0] = 1
                    print("ZZZZZZZZZZZZZZZZZZZZZZZZ"+str(speed[0])+"<<")
            # Move right
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self._person__yco+i][self._person__xco+j]
            for i in range(4):
                for j in range(3):
                    game_board[self._person__yco+i][self._person__xco+j+1] = person.__figure[i][0][j]
            if self._person__xco is not 1:
                for i in range(4):
                    game_board[y+i][self._person__xco-1] = " "
                    game_board[y+i][self._person__xco] = " "
            self._person__xco = self._person__xco + 1
            
    #    # Act gravity 
        final = min(self._person__vel,14-self._person__yco)
        # Move it final times down
        for i in range(final):
            for j in range(3):
                if game_board[self._person__yco+i][self._person__xco+j] in not_allowed_collision:
                    self._person__life = self._person__life - 1
                    correct_beams(game_board,self._person__yco+i,self._person__xco+j,3)
                elif game_board[self._person__yco+i][self._person__xco+j] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self._person__coins = self._person__coins + 1
                elif game_board[self._person__yco+i][self._person__xco+j] in powerup:
                    print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
                    speed[0] = 1
                    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                    
        #     # Move 1 down
            array = [[" " for i in range(3)] for j in range(4)]
            for ii in range(4):
                for jj in range(3):
                    array[ii][jj] = game_board[self._person__yco+ii+i][self._person__xco+jj]
            for ii in range(4):
                for jj in range(3):
                    game_board[self._person__yco+ii+i+1][self._person__xco+jj] = person.__figure[ii][0][jj]
            if self._person__yco is not (14):
                for jj in range(3):
                    game_board[self._person__yco+i][self._person__xco+jj] = " "
        self._person__yco += final


        

class Boss(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)
    def define_boss(self,game_board):
        # Place a dragon at 
        f = extract('mydragon.txt')
        p = f.nikal()
        x = self._person__xco
        y = self._person__yco
        for i in range(len(p)):
            for j in range(len(p[i])):
                game_board[y+i][x+j] = p[i][j]

    def interact(self,game_board,dinx,diny,din):
        # Move it towards the enemy if same then throw a bullet
        # an iceball towards the player
        # Check bullets 
        ff = extract('mydragon.txt')
        pp = ff.nikal()
        aan = len(pp)

        odd = random.randint(0,5)
        if diny >= self._person__yco - aan and diny <= self._person__yco + aan:
            if odd is 0:
                self._person__bullets.append([self._person__xco-1,self._person__yco])
            if odd is 1:
                self._person__bullets.append([self._person__xco-1,self._person__yco+5])

        # print("ME CALLED"+str(dinx)+"|||"+str(diny)+".."+str(self._person__xco)+">>"+str(self._person__yco)+"||")
        x = self._person__xco


        for i in range(aan):
            if game_board[self._person__yco+i][self._person__xco-1] is "*":
                # Lol Anna
                print("LOL ANNA")
                self._person__life = self._person__life - 1
                # Chek the bullet to pop
                for j in range(len(din._person__bullets)):
                    if len(din._person__bullets) > j and din._person__bullets[j][1] is self._person__yco+i and din._person__bullets[j][0] is self._person__xco-1:
                        # This was it , remove it
                        print("Yahan thha" + str(j)+ "||")            
                        din._person__bullets.pop(j)
                game_board[self._person__yco+i][self._person__xco-1] = " "



        if self._person__yco < diny and self._person__yco < 20 - 2 - aan:
            # Move it down
            array = []
            f = extract('mydragon.txt')
            p = f.nikal()
            for i in range(len(p)):
                for j in range(len(p[i])):
                    game_board[self._person__yco+1+i][x+j] = p[i][j]
            for j in range(len(p[0])):
                game_board[self._person__yco][j] = " "
            self._person__yco = self._person__yco + 1
        elif self._person__yco > diny :
            # Move it up
            array = []
            f = extract('mydragon.txt')
            p = f.nikal()
            an = len(p)
            for i in range(len(p)):
                for j in range(len(p[i])):
                    game_board[self._person__yco-1+i][x+j] = p[i][j]
            for j in range(len(p[an-1])):
                game_board[self._person__yco+an-1][x+j] = " "
            self._person__yco = self._person__yco - 1

    def move_bullets(self,game_board,din):
        for i in range(len(self._person__bullets)):
            # print("i = " + str(i))
            if len(self._person__bullets) > i  and self._person__bullets[i][0] <= 2:
                self._person__bullets.pop(i)
                continue
            elif len(self._person__bullets) > i and self._person__bullets[i][0] is din._person__xco+3 and  self._person__bullets[i][1] is din._person__yco:
                din._person__life = din._person__life - 1
                self._person__bullets.pop(i)
                continue
            elif len(self._person__bullets) > i:
                # Move it one step backward
                game_board[self._person__bullets[i][1]][self._person__bullets[i][0]] = " "
                game_board[self._person__bullets[i][1]][self._person__bullets[i][0]-2] = "P"
                self._person__bullets[i][0] = self._person__bullets[i][0] - 2

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

def interact_magnet(game_board,xpos,xdim,din):
    # Make the din accelerate towards the magnet
    not_allowed_collision = ["X","P"]
    wall = ["|","_"]
    coins = ["O"]
    powerup = ["\u23e9"]
    anaa = 0
    magx = -1
    magy = -1
    person.__figure = [[["<","M","|"],["|","M",">"]],
                        [[" ","|"," "],[" ","|"," "]],
                        [["/","|"," "],[" ","|","\\"]],
                    [["|"," ","\\"],["/"," ","|"]]] 
    
    while anaa is 0:
        for i in range(20):
            for j in range(xpos,xpos+xdim):
                if game_board[i][j] is "U":
                    anaa = -1
                    magy = i
                    magx = j
        if anaa is 0:
            anaa = 1
                
    if anaa is -1:
        print("MAAAAAAGGGGNNNNEEEEEEEETTTTTT"+str(magx)+"||"+str(magy))

    if magx < din._person__xco and anaa is -1:
        df = 0
       
        # Move left towards the magnet
    
        for i in range(4):
            for k in range(2):
                if game_board[din._person__yco+i][din._person__xco-1-k] in not_allowed_collision:
                    din._person__life = din._person__life - 1
                elif game_board[din._person__yco+i][din._person__xco-1-k]  in coins:
                    din._person__coins = din._person__coins + 1
        for i in range(4):
            for j in range(3):
                game_board[din._person__yco+i][din._person__xco+j-2] = person.__figure[i][0][j]
        for i in range(4):
            for k in range(2):
                game_board[din._person__yco+i][din._person__xco+j+k] = " "
            din._person__xco = din._person__xco - 2

    elif magx > din._person__xco and anaa is -1:
        # Move right towards the magnet
        fg = 0
        for i in range(4):
            for j in range(3):
                game_board[din._person__yco+i][din._person__xco+j+4] = person.__figure[i][0][j]
        for i in range(4):
            for k in range(2):
                if game_board[din._person__yco+i][din._person__xco+3+k] in not_allowed_collision:
                    din._person__life = din._person__life - 1
                elif game_board[din._person__yco+i][din._person__xco+3+k]  in coins:
                    din._person__coins = din._person__coins + 1
        for i in range(4):
            for j in range(3):
                game_board[din._person__yco+i][din._person__xco+j+4] = person.__figure[i][0][j]
        for i in range(4):
            for k in range(2):
                game_board[din._person__yco+i][din._person__xco+k] = " "
        din._person__xco = din._person__xco + 2

    else:
        # Do nothing
        h = 0
