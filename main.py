import os,signal,time
from playsound import playsound
from colorama import init,Fore
from board import *
import numpy as np
init()

print("\033\143")
key = True
a = 0
while key is True:
    sample = board(2000,30,100,2)
    sample._board__display()
    while key is True:
        a = a + 1
    key = True
    print('Hi')
