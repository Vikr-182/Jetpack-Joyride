from colorama import Fore, Back, Style
import os
import time
from playsound import playsound
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

#playsound('lol.mp3')

array = [[" " for j in range(8)] for i in range(8)]
y = 10
x = 94
char = "\u274c"
print("\u23e9")

# for i in range(8):
#     for j in range(8):
#         print("\033["+str(j)+";"+str(i)+"H"+char,end="")