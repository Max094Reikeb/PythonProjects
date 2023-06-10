#IMPORTATION MODULE MATH
from math import *

#ON IMPORTE LE CHIFFRE A CODER
number = int(input('Nombre à coder : '))

#ON TRANSFORME EN BINAIRE
while number >= 1:
	binaire = number % 2
	number = number // 2
	print(binaire)

wait = input("END")