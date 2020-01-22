from colorama import Fore, Back, Style
import os
import time
from playsound import playsound
# from scenery import *
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

#playsound('lol.mp3')

array = [[" " for j in range(8)] for i in range(8)]
y = 10
x = 94
char = "X"
print("\u23e9")

# f = extract('mydragon.txt')
# p = f.nikal()
# for g in p:
#     print(g,end="")

a = []
for i in range(10):
    a.append([i,i+1])
print(a)
# for line in file:
#     print(line,end="")
# for i in range(8):
#     for j in range(8):
#         print("\033["+str(j)+";"+str(i)+"H"+char,end="")