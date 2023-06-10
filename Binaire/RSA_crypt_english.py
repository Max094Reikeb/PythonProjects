#IMPORTATION MODULE MATH
from math import *

#WE ENTER THE MESSAGE TO CODE AND THE PUBLIC KEY : E AND N
mot = input('Message to code : ')
e = int(input('e = '))
n = int(input('n = '))

#WE DO, LETTER BY LETTER THE TRANSFORMATION INTO CRYPTED CODE
for i in range(len(mot)):
    ascii = ord(mot[i]) #WE CHANGE THE LETTER IN ASCII CODE
    mc = ascii**e #WE PUT THE ASCII CODE IN POWER E
    mc2 = mc%n #WE MODULE WITH N
    print(mc2)
    

print('')

wait = input("END")
