#IMPORTATION MODULE MATH
from math import *

#ON IMPORTE LE NOMBRE BINAIRE A DECODER ET LE NOMBRE DE BITS
binaire = input('Nombre à décoder : ')
n = int(input('Nombre de bits : '))

n = n - 1 #ON SOUSTRAIT 1 AU NOMBRE DE BITS

orone = binaire.split('.') #ON INDIQUE QUE CHAQUE 0 OU 1 EST SEPARE PAR UN POINT
#ON TRAITE PAR 0 ET 1 LA TRANSFORMATION EN CHIFFRE
for lettre in orone:
	while n >= 0:
		lettre = int(lettre)
		bt = bt + 2**n * lettre
		wait = input("END")
		n = n - 1
    
print(bt)

wait = input("END")