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