#IMPORTATION(S)
import math
import os

#LES INPUTS
clefA = int(input('Clef A : '))
clefB = int(input('Clef B : '))
clefC = int(input('Clef C : '))
mot = input('Mot à convertir (sous forme de chiffres) : ')

#MOT -> CHIFFRES
s = ''
print("val=")
for i in range(len(mot)):
    val = ord(mot[i])

    if (val > 64 and val < 91):
        val = val - 64
    elif (val > 96 and val < 123):
        val = val - 96
    else:
        val = 0
    s += str(val)
    #print(val, end='')
    
print(s)

#LE TRAITEMENT
mot1 = int(s) * clefA
mot2 = mot1 + clefB
reste = mot2 % clefC
entier = mot2 // clefC
liste_re = []
liste_re.insert(1, reste)
liste_re.insert(2, entier)

#ON AFFICHE
print("Code pour '", mot, "' : ", liste_re)

#FIN
print("Vous pouvez copier-coller le code pour le partager !")
os.system("pause")
