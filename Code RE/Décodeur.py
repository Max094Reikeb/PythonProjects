#IMPORTATION(S)
import math
import os

#LES INPUTS
clefA = int(input('Clef A : '))
clefB = int(input('Clef B : '))
clefC = int(input('Clef C : '))
reste = int(input('1er nombre du code : '))
entier = int(input('2eme nombre du code : '))

#LE TRAITEMENT
message1 = entier * clefC
print (message1)
message2 = message1 + reste
print (message2)
message3 = message2 - clefB
print (message3)
message4 = message3 / clefA

print("Votre correspondant à voulu dire :", message4)

#FIN
os.system("pause")
