#IMPORTATION MODULE MATH
from math import *

#ON IMPORTE LE MOT A CODER ET LA CLEF PUBLIQUE E ET N
mot = input('Mot à coder : ')
e = int(input('e = '))
n = int(input('n = '))

#ON TRAITE LETTRE PAR LETTRE LA TRANSFORMATION EN ASCII
for i in range(len(mot)):
    ca = ord(mot[i]) #ON LA CHANGE EN CARACTERE ASCII
    mpc = ca**e #ON MET LE CODE ASCII EN PUISSANCE E
    mc = mpc%n #ON MODULE AVEC N
    print(mc)
    

print('')

wait = input("END")
