#IMPORTATION MODULE MATH
from math import *

#WE ENTER THE CRYPTED MESSAGE AND THE PRIVATE KEY : D AND N
mot = input('Crypted message (separated by a comma) : ')
d = int(input('d = '))
n = int(input('n = '))

bloc = mot.split(',') #WE SHOW TO THE CODE THAT EVERY BLOC IS SEPARATED BY A COMMA

#WE DO, BLOC BY BLOC THE TRANSFORMATION INTO A LETTER
for lettre in bloc:
    cc = int(lettre)**d #WE PUT THE CRYPTED MESSAGE IN POWER D
    cn = cc%n #WE MODULATE WITH N
    message = chr(cn) #WE TRANSFORM THE ASCII CODE INTO A LETTER

    print(message, end="")
    
print('')

wait = input("END")
