from colorama import Fore, Back, Style
import os
import time
from playsound import playsound
from scenery import *
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

#playsound('lol.mp3')

array = [[" " for j in range(8)] for i in range(8)]
y = 10
x = 94
char = Fore.RED+"X"+Style.RESET_ALL
print(Fore.YELLOW+"O"+Style.RESET_ALL)

# f = extract('mydragon.txt')
# p = f.nikal()
# for g in p:
#     print(g,end="")

a = []
for i in range(10):
    a.append([i,i+1])
a.pop(4)
print(a)

for i in range(4):
    f = extract('bonus' + str(i)+'.txt')
    p = f.nikal()
    print(len(p))

print(Fore.YELLOW+Back.GREEN+"O"+Style.RESET_ALL)
print(Fore.YELLOW+"O"+Style.RESET_ALL)
# maxi = 0
# for i in range(len(p)):
#     if maxi < len(p[i]):
#         maxi = len(p[i])

# print(maxi)

# ana = Fore.YELLOW+"O"+Style.RESET_ALL+Style.RESET_ALL
# kappa = [Fore.YELLOW+"O"+Style.RESET_ALL+Style.RESET_ALL,Fore.RED+Fore.YELLOW+"O"+Style.RESET_ALL]
# if ana ==Fore.YELLOW+"O"+Style.RESET_ALL+Style.RESET_ALL:
#     print("PPPPPPPPP")
# else:
#     print("FFFFFFFFFF"+str(ana))
# import time
# start = time.time()
# cnt = 0
# print(Back.RED+Fore.YELLOW+Back.GREEN+"O"+Style.RESET_ALL+Style.RESET_ALL)
# while True:
#     if time.time()-start>0.0001:
#         cnt = cnt + 1
#         print("RARA"+ str(cnt)+str("||"))
#         start = time.time()
# for line in file:
#     print(line,end="")
# for i in range(8):
#     for j in range(8):
#         print("\033["+str(j)+";"+str(i)+"H"+char,end="")