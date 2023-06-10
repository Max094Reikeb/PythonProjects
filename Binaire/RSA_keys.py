#IMPORTATION MODULE MATH
from math import *

#ON CHOISI P ET Q DEUX ENTIERS NATURELS PREMIERS
p = int(input('p = '))
q = int(input('q = '))

#ON VERIFIE QUE P ET Q SOIENT PREMIERS
i = 2

if p % i == 0:
	print("ERREUR :", q, "EST PAS PREMIER, IL EST DIVISIBLE PAR", i)
	wait = input("APPUYEZ SUR UNE TOUCHE POUR QUITTER LE PROGRAMME")
	sys.exit()

if q % i == 0:
	print("ERREUR :", p, "EST PAS PREMIER, IL EST DIVISIBLE PAR", i)
	wait = input("APPUYEZ SUR UNE TOUCHE POUR QUITTER LE PROGRAMME")
	sys.exit()

i = i + 1

while ((sqrt(p) >= i) and (sqrt(q) >= i)):
	if p % i == 0:
		print("ERREUR :", q, "EST PAS PREMIER, IL EST DIVISIBLE PAR", i)
		wait = input("APPUYEZ SUR UNE TOUCHE POUR QUITTER LE PROGRAMME")
		sys.exit()

	if q % i == 0:
		print("ERREUR :", p, "EST PAS PREMIER, IL EST DIVISIBLE PAR", i)
		wait = input("APPUYEZ SUR UNE TOUCHE POUR QUITTER LE PROGRAMME")
		sys.exit()

	i = i + 2

#ON CALCULE N TEL QUE N = P*Q (ET ON L'AFFICHE)
n = p*q
print("n = ", n)

#ON CALCULE PHI(n) TEL QUE PHIN = (P-1)*(Q-1) (ET ON L'AFFICHE)
phin = (p-1)*(q-1)
print("Phi(n) = ", phin)

#ON DETERMINE E ET D PAR DEFAUT AVEC E ET D > 2
e = 2
d = 2

#ON CALCULE E TEL QUE E < PHI(n) ET QUE E ET PHI(n) SOIENT PREMIERS ENTRE EUX
while gcd(phin, e) != 1:
	if (e > phin):
		print("e est impossible à trouver... Vérifie qu'il n'y a pas d'erreur")
		wait = input("APPUYEZ SUR UNE TOUCHE POUR QUITTER LE PROGRAMME")
		sys.exit()
	e = e + 1  #ON AJOUTE 1 A E ET ON RECOMMENCE LE TEST
	print(e)

#ON CALCULE D, LA CLEF PRIVEE (ON A DEJA N) TEL QUE (D*E)%PHI(n) = 1
while (e * d) % phin != 1:
	if (d > phin):
		print("d est impossible à trouver... Vérifie qu'il n'y a pas d'erreur")
		wait = input("APPUYEZ SUR UNE TOUCHE POUR QUITTER LE PROGRAMME")
		sys.exit()
	d = d + 1
	print(d)

d = d - 1

#ON AFFICHE E, N, ET D
print('')
print('')
print("[----------KEYS----------]")
print("e =", e, "(public)")
print("n =", n, "(public)")
print("d =", d, "(privé)")
wait = input("[-----END OF PROGRAM-----]")

#e = 565
#n = 283189
#104497,138548,241808,266740,5890,45154,84918
#d = 140312
