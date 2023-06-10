#IMPORTATION MODULE MATH
from math import *

#ON IMPORTE LE CODE ET LA CLEF PRIVEE D ET N
code = input('Code (séparé par une virgule) : ')
d = int(input('d = '))
n = int(input('n = '))

bloc = code.split(',') #ON INDIQUE QUE CHAQUE BLOC EST SEPARE PAR UNE VIRGULE

#ON TRAITE BLOC PAR BLOC LA TRANSFORMATION EN LETTRES
for lettre in bloc:
    cc = int(lettre)**d #ON MET LE CODE ASCII EN PUISSANCE D
    cpd = cc%n #ON MODULE AVEC N
    message = chr(cpd) #ON TRANSFORME LE CODE ASCII EN LETTRE

    print(message, end="")
    
print('')

wait = input("END")
