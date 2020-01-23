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
        self.__dragon = 0
        self.__f = ["" for i in range(4)]
        for i in range(4):
            self.__f[i] = extract("bonus"+str(i)+".txt")
        self.__count = 0
        
        
class Mandalorian(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)
        person.__figure = [[["<","M","|"],["|","M",">"]],
                         [[" ","|"," "],[" ","|"," "]],
                         [["/","|"," "],[" ","|","\\"]],
                        [["|"," ","\\"],["/"," ","|"]]]
        person.__alive = True
    def get_figure(self):
        return person.__figure
    def set_figure(self,i,j,value):
        person.__figure[i][j] = value
    
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

    def get_life(self):
        return self._person__life
    def set_life(self,value):
        self._person__life = value

    def get_coins(self):
        return self._person__coins
    def set_coins(self,value):
        self._person__coins = value
    
    def get_vel(self):
        return self._person__vel
    def set_vel(self,value):
        self._person__vel = value

    def get_shield(self):
        return self._person__shield
    def set_shield(self,value):
        self._person__shield = value

    def get_bullets(self):
        return self._person__bullets
    def set_bullets(self,i,value):
        self._person__bullets[i] = value

    def get_dragon(self):
        return self._person__dragon
    def set_dragon(self,value):
        self._person__dragon = value

    def get_f(self):
        return self._person__f 
    def set_f(self,value):
        self._person__f = value

    def get_count(self):
        return self._person__count 
    def set_count(self,value):
        self._person__count = value


    def define_mandalorian(self,game_board,x,y):
        a = 0
        if a >= 0: # Moving forward
            for i in range(4):
                for j in range(3):
                    game_board[y+i][x+j] = self.get_figure()[i][1][j]

        elif a < 0: # Moving forward
            for i in range(4):
                for j in range(3):
                    game_board[y+i][x+j] = self.get_figure()[i][0][j]

    
    def move_bullets(self,game_board,xpos,xdim, fag,speed):
        # Make this move to next, while shooting down beams in this process
         for i in range(len(self.get_bullets())):
             # Move this 
            if len(self.get_bullets()) <= i:
                continue
            x = self.get_bullets()[i][0]
            y = self.get_bullets()[i][1]
            wall = ["|","_"]
            coins = [Fore.YELLOW + "O"+Style.RESET_ALL]
            powerup = [Fore.BLUE+">"+Style.RESET_ALL]
            save = game_board[y][x+1]
            not_allowed_collision = [Fore.RED+"X"+Style.RESET_ALL,"P"]
            for j in range(1+speed[0]):
                if game_board[y][x+2+j] in coins or game_board[y][x+2+j] in powerup or game_board[y][x+1+j] in coins or game_board[y][x+1+j] in powerup:
                    # Do nothing
                    b = 0
                elif game_board[y][x+2+j] in not_allowed_collision:
                    correct_beams(game_board,y,x+2+j,0)
                    if len(self.get_bullets())>=1:
                        self.get_bullets().pop(i)
                    game_board[y][x+2+j] = " "
                    game_board[y][x+1+j] = " "
                    game_board[y][x+j] = " "
                    continue
                elif game_board[y][x+1+j] in not_allowed_collision:
                    correct_beams(game_board,y,x+2+j,0)
                    self.get_bullets().pop(i)
                    game_board[y][x+1+j] = " "
                    game_board[y][x+j] = " "
                    continue
                else:
                    game_board[y][x+2+speed[0]] = "*"
                    game_board[y][x] = save
                if len(self.get_bullets()) > i:
                    self.get_bullets()[i][0] = self.get_bullets()[i][0] + 2*(j^1)+j
                if len(self.get_bullets()) > i and self.get_bullets()[i][0]  >= xpos + xdim : # Rmove it from frame
                    game_board[self.get_bullets()[i][1]][self.get_bullets()[i][0]] = " "
                    self.get_bullets().pop(i)


    def move_me(self,game_board,command,xpos,x,y,xdim,ij,mag,speed,fag,move):
        print("ME CALLED:"+str(xpos)+"||")
        # Last position move forward by one column
        not_allowed_collision = [Fore.RED+"X"+Style.RESET_ALL,"P"]
        wall = ["|","_"]
        coins = [Fore.YELLOW + "O"+Style.RESET_ALL]
        powerup = [Fore.BLUE+">"+Style.RESET_ALL]
        array = [[" " for i in range(3)] for j in range(4)]

            # The dragon is activated now need to change the game completely until the dragon does not go out .
        if ij is True and fag is 0 and move is 1:
            ij = False
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[y+i][self.get_xco()+j]
            for i in range(4):
                for j in range(1+speed[0]):
                    if game_board[y+i][self.get_xco()+3+j] in not_allowed_collision:
                        self.set_life(self.get_life()-1)
                        correct_beams(game_board,y+i,self.get_xco()+j+3,0)
                    elif game_board[y+i][self.get_xco()+j+3] in coins:
                        # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                        self.set_coins(self.get_coins()+1)
                    elif game_board[y+i][self.get_xco()+j+3] in powerup:
                        print("BBBBBBBBBBBBBBBBBBBBBBBB"+str(speed[0])+"||")
                        speed[0] = 1
                        print("DDDDDDDDDDDDDDDDDDDDDDDD"+str(speed[0])+"<<")
                
            for i in range(4):
                for j in range(3):
                        game_board[y+i][self.get_xco()+j+1+speed[0]] = self.get_figure()[i][0][j]
            if self.get_xco() is not 1:
                # Make back empty
                for i in range(4):
                    game_board[y+i][self.get_xco()-1] = " "
                    game_board[y+i][self.get_xco()] = " "
                    game_board[y+i][self.get_xco()+speed[0]] = " "
            self.set_xco(self.get_xco()+1+speed[0])

        if ij is True and fag is 1 and move is 1:
            ij = False
            # Effective dimension is 5 x 4
            array = [[" " for i in range(5)] for j in range(6)]
            for i in range(6):
                for j in range(5):
                    array[i][j] = game_board[y-1+i][self.get_xco()-1+j]
            for i in range(6):
                if game_board[y-1+i][self.get_xco()+4] in not_allowed_collision:
                    fag = 0
                    correct_beams(game_board,y-1+i,self.get_xco()+4,0)
                    print("SHIELD LOST")
                elif game_board[y-1+i][self.get_xco()+4] in coins:
                    self.set_coins(self.get_coins()+1)
                elif game_board[y-1+i][self.get_xco()+4] in powerup:
                    speed[0] = 1
                
            for i in range(5):
                for j in range(4):
                    game_board[y-1+i][self.get_xco()-1+j+1] = array[i][j]
            if self.get_xco() is not 1:
                # Make back empty
                for i in range(5):
                    game_board[y-1+i][self.get_xco()-2] = " "
            self.set_xco(self.get_xco()+1)
                                        


        if command is 'w' or command is '\33[A':
            # Move up
            b = 0
            flag = 0
            self.set_vel(0)
            if self.get_yco() <= 2:
                return # Dont move
            elif self.get_yco() is 10:
                bv = 0
            for i in range(3):
                if game_board[y-1][self.get_xco()+i] in not_allowed_collision:
                    self.set_life(self.get_life()-1)
                    correct_beams(game_board,y-1,self.get_xco()+i,0)
                elif game_board[y-1][self.get_xco()+i] in coins:
                    self.set_coins(self.get_coins()+1)
                elif game_board[y-1][self.get_xco()+i] in powerup:
                    print("NNNNNNNNNNNNNNNNNNNNNNNNNN")
                    speed[0] = 1
                    print("OOOOOOOOOOOOOOOOOOOOOOOOOO")
            # move up
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self.get_yco()+i][self.get_xco()+j]
            for i in range(4):
                for j in range(3):
                    game_board[self.get_yco()+i-1][self.get_xco()+j] = self.get_figure()[i][0][j]
            if self.get_yco() is not (18):
                for j in range(3):
                    game_board[self.get_yco()+3][self.get_xco()+j] = " "
            self.set_yco(self.get_yco()-1)
            print("Now "+ str(self.get_yco())+"|")
        

        if command is 'a' or command is '\33[D':
            # Move left
            j = 0
            if self.get_xco() <= (xpos+2):
                t = 0 # Dont move
                return
            
            for i in range(4):
                if game_board[self.get_yco()+i][self.get_xco()-1] in not_allowed_collision:
                    self.set_life(self.get_life()-1)
                    correct_beams(game_board,self.get_yco()+i,self.get_xco()-1,0)
                elif game_board[self.get_yco()+i][self.get_xco()-1] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self.set_coins(self.get_coins()+1)
                elif game_board[self.get_yco()+i][self.get_xco()-1] in powerup:
                    print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
                    speed[0] = 1
                    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                
            # Move left
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self.get_yco()+i][self.get_xco()+j]
            for i in range(4):
                for j in range(3):
                    game_board[self.get_yco()+i][self.get_xco()+j-1] = self.get_figure()[i][0][j]
            if self.get_xco() is not (xpos+xdim-4):
                for i in range(4):
                    game_board[y+i][self.get_xco()+2] = " "
                    game_board[y+i][self.get_xco()+3] = " "
            self.set_xco(self.get_xco()-1)
            
        if command is 's' or command is '\33[B':
            # Move down
            k =  1
            if self.get_yco() is 14:
            #     print("OOOOOOOOO")
                return # Dont move
            for i in range(3):
                if game_board[self.get_yco()+4][self.get_xco()+i] in not_allowed_collision:
                    self.set_life(self.get_life()-1)
                    correct_beams(game_board,self.get_yco()+4,self.get_xco()+i,3)
                elif game_board[self.get_yco()+4][self.get_xco()+i] in coins:
                    self.set_coins(self.get_coins()+1)          
                elif game_board[self.get_yco()+4][self.get_xco()+i] in powerup:
                    print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
                    speed[0] = 1  
                    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
            # move down
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self.get_yco()+i][self.get_xco()+j]
            for i in range(4):
                for j in range(3):
                    game_board[self.get_yco()+i+1][self.get_xco()+j] = self.get_figure()[i][0][j]
            if self.get_yco() is not (14):
                for j in range(3):
                    game_board[self.get_yco()][self.get_xco()+j] = " "
            self.set_yco(self.get_yco()+1)
        

        if command is 'd' or command is '\33[C':
            # Move right
            g = 0
            if self.get_xco() >= (xpos+xdim-3):
                t = 0 # Dont move
                # print("AAAAAAAAAAAAAA")
                return
            for i in range(4):
                if game_board[y+i][self.get_xco()+3] in not_allowed_collision:
                    self.set_life(self.get_life()-1)
                    correct_beams(game_board,y+i,self.get_xco()+3,3)
                elif game_board[y+i][self.get_xco()+3] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self.set_coins(self.get_coins()+1)
                elif game_board[y+i][self.get_xco()+3] in powerup:
                    print("YYYYYYYYYYYYYYYYYYYYYYYY"+str(speed[0])+"||")
                    speed[0] = 1
                    print("ZZZZZZZZZZZZZZZZZZZZZZZZ"+str(speed[0])+"<<")
            # Move right
            array = [[" " for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    array[i][j] = game_board[self.get_yco()+i][self.get_xco()+j]
            for i in range(4):
                for j in range(3):
                    game_board[self.get_yco()+i][self.get_xco()+j+1] = self.get_figure()[i][0][j]
            if self.get_xco() is not 1:
                for i in range(4):
                    game_board[y+i][self.get_xco()-1] = " "
                    game_board[y+i][self.get_xco()] = " "
            self.set_xco(self.get_xco()+1)
            
    #    # Act gravity 
        final = min(self.get_vel(),14-self.get_yco())
        # Move it final times down
        for i in range(final):
            for j in range(3):
                if game_board[self.get_yco()+i][self.get_xco()+j] in not_allowed_collision:
                    self.set_life(self.get_life()-1)
                    correct_beams(game_board,self.get_yco()+i,self.get_xco()+j,3)
                elif game_board[self.get_yco()+i][self.get_xco()+j] in coins:
                    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                    self.set_coins(self.get_coins()+1)
                elif game_board[self.get_yco()+i][self.get_xco()+j] in powerup:
                    print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
                    speed[0] = 1
                    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                    
        #     # Move 1 down
            array = [[" " for i in range(3)] for j in range(4)]
            for ii in range(4):
                for jj in range(3):
                    array[ii][jj] = game_board[self.get_yco()+ii+i][self.get_xco()+jj]
            for ii in range(4):
                for jj in range(3):
                    game_board[self.get_yco()+ii+i+1][self.get_xco()+jj] = self.get_figure()[ii][0][jj]
            if self.get_yco() is not (14):
                for jj in range(3):
                    game_board[self.get_yco()+i][self.get_xco()+jj] = " "
        self.set_yco(self.get_yco()+final)


        

class Boss(person):
    def __init__(self,xco,yco):
        person.__init__(self,xco,yco)
    def define_boss(self,game_board):
        # Place a dragon at 
        f = extract('mydragon.txt')
        p = f.nikal()
        x = self.get_xco()
        y = self.get_yco()
        for i in range(len(p)):
            for j in range(len(p[i])):
                game_board[y+i][x+j] = p[i][j]

    def get_xco(self):
        return self._person__xco
    def set_xco(self,value):
        self._person__xco = value

    def get_yco(self):
        return self._person__yco
    def set_yco(self,value):
        self._person__yco = value

    def get_life(self):
        return self._person__life
    def set_life(self,value):
        self._person__life = value

    def get_coins(self):
        return self._person__coins
    def set_coins(self,value):
        self._person__coins = value
    
    def get_vel(self):
        return self._person__vel
    def set_vel(self,value):
        self._person__vel = value

    def get_shield(self):
        return self._person__shield
    def set_shield(self,value):
        self._person__shield = value

    def get_bullets(self):
        return self._person__bullets
    def set_bullets(self,i,value):
        self._person__bullets[i] = value


    def interact(self,game_board,dinx,diny,din):
        # Move it towards the enemy if same then throw a bullet
        # an iceball towards the player
        # Check bullets 
        ff = extract('mydragon.txt')
        pp = ff.nikal()
        aan = len(pp)

        odd = random.randint(0,5)
        if diny >= self.get_yco() - aan and diny <= self.get_yco() + aan:
            if odd is 0:
                self.get_bullets().append([self.get_xco()-1,self.get_yco()])
            if odd is 1:
                self.get_bullets().append([self.get_xco()-1,self.get_yco()+5])

        # print("ME CALLED"+str(dinx)+"|||"+str(diny)+".."+str(self.get_xco())+">>"+str(self.get_yco())+"||")
        x = self.get_xco()


        for i in range(aan):
            if game_board[self.get_yco()+i][self.get_xco()-1] is "*":
                # Lol Anna
                print("LOL ANNA")
                self.set_life(self.get_life()-1)
                # Chek the bullet to pop
                for j in range(len(din.get_bullets())):
                    if len(din.get_bullets()) > j and din.get_bullets()[j][1] is self.get_yco()+i and din.get_bullets()[j][0] is self.get_xco()-1:
                        # This was it , remove it
                        print("Yahan thha" + str(j)+ "||")            
                        din.get_bullets().pop(j)
                game_board[self.get_yco()+i][self.get_xco()-1] = " "



        if self.get_yco() < diny and self.get_yco() < 20 - 2 - aan:
            # Move it down
            array = []
            f = extract('mydragon.txt')
            p = f.nikal()
            for i in range(len(p)):
                for j in range(len(p[i])):
                    game_board[self.get_yco()+1+i][x+j] = p[i][j]
            for j in range(len(p[0])):
                game_board[self.get_yco()][j] = " "
            self.set_yco(self.get_yco()+1)
        elif self.get_yco() > diny :
            # Move it up
            array = []
            f = extract('mydragon.txt')
            p = f.nikal()
            an = len(p)
            for i in range(len(p)):
                for j in range(len(p[i])):
                    game_board[self.get_yco()-1+i][x+j] = p[i][j]
            for j in range(len(p[an-1])):
                game_board[self.get_yco()+an-1][x+j] = " "
            self.set_yco(self.get_yco()-1)

    def move_bullets(self,game_board,din):
        for i in range(len(self.get_bullets())):
            # print("i = " + str(i))
            if len(self.get_bullets()) > i  and self.get_bullets()[i][0] <= 2:
                self.get_bullets().pop(i)
                continue
            elif len(self.get_bullets()) > i and self.get_bullets()[i][0] is din.get_xco()+3 and  self.get_bullets()[i][1] is din.get_yco():
                din.set_life(din.get_life()-1)
                self.get_bullets().pop(i)
                continue
            elif len(self.get_bullets()) > i:
                # Move it one step backward
                game_board[self.get_bullets()[i][1]][self.get_bullets()[i][0]] = " "
                game_board[self.get_bullets()[i][1]][self.get_bullets()[i][0]-2] = "P"
                self.get_bullets()[i][0] = self.get_bullets()[i][0] - 2

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
    not_allowed_collision = [Fore.RED+"X"+Style.RESET_ALL,"P"]
    wall = ["|","_"]
    coins = [Fore.YELLOW + "O"+Style.RESET_ALL]
    powerup = [Fore.BLUE+">"+Style.RESET_ALL]
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

    if magx < din.get_xco() and anaa is -1:
        df = 0
       
        # Move left towards the magnet
    
        for i in range(4):
            for k in range(2):
                if game_board[din.get_yco()+i][din.get_xco()-1-k] in not_allowed_collision:
                    din.set_life(din.get_life()-1)
                elif game_board[din.get_yco()+i][din.get_xco()-1-k]  in coins:
                    din.set_coins(din.get_coins()+1)
        for i in range(4):
            for j in range(3):
                game_board[din.get_yco()+i][din.get_xco()+j-2] = din.get_figure()[i][0][j]
        for i in range(4):
            for k in range(2):
                game_board[din.get_yco()+i][din.get_xco()+j+k] = " "
            din.set_xco(din.get_xco()-2)

    elif magx > din.get_xco() and anaa is -1:
        # Move right towards the magnet
        fg = 0
        for i in range(4):
            for j in range(3):
                game_board[din.get_yco()+i][din.get_xco()+j+4] = din.get_figure()[i][0][j]
        for i in range(4):
            for k in range(2):
                if game_board[din.get_yco()+i][din.get_xco()+3+k] in not_allowed_collision:
                    din.set_life(din.get_life()-1)
                elif game_board[din.get_yco()+i][din.get_xco()+3+k]  in coins:
                    din.set_coins(din.get_coins()+1)
        for i in range(4):
            for j in range(3):
                game_board[din.get_yco()+i][din.get_xco()+j+4] = din.get_figure()[i][0][j]
        for i in range(4):
            for k in range(2):
                game_board[din.get_yco()+i][din.get_xco()+k] = " "
        din.set_xco(din.get_xco()+2)

    else:
        # Do nothing
        h = 0
