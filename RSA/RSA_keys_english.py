#IMPORTATION MODULE MATH
from math import *

#WE CHOOSE P AND Q TWO PRIMARIES AND NATURALS NUMBERS
p = int(input('p = '))
q = int(input('q = '))

#WE CHECK THAT P AND Q ARE PRIMARIES
pr = 2

if q % pr == 0:
	print("ERROR :", q, "IS NOT PRIMARY")
	wait = input("ENTER ANY KEY TO QUIT")
	sys.exit()

if p % pr == 0:
	print("ERROR :", p, "IS NOT PRIMARY")
	wait = input("ENTER ANY KEY TO QUIT")
	sys.exit()

pr = pr + 1

while ((sqrt(p) >= pr) and (sqrt(q) >= pr)):
	if q % pr == 0:
		print("ERROR :", q, "IS NOT PRIMARY")
		wait = input("ENTER ANY KEY TO QUIT")
		sys.exit()

	if p % pr == 0:
		print("ERROR :", p, "IS NOT PRIMARY")
		wait = input("ENTER ANY KEY TO QUIT")
		sys.exit()

	pr = pr + 2

#WE FIND N SO N = P*Q (AND WE PRINT IT)
n = p*q
print("n = ", n)

#WE FIND PHI(n) SO PHIN = (P-1)*(Q-1) (AND WE PRINT IT)
phin = (p-1)*(q-1)
print("Phi(n) = ", phin)

#WE FIND E AND D IN THE FIRST PLACE AS EQUAL AS 2
d = 2
e = 2

#WE FIND E AS E < PHI(n) AND AS E AND PHI(n) ARE PRIMARIES BETWEEN THEM
while gcd(phin, e) != 1:
	if (e > phin):
		print("e is impossible to find... Search for any error")
		wait = input("ENTER ANY KEY TO QUIT")
		sys.exit()
	e = e + 1  #WE ADD 1 TO E AND WE RESTART THE LOOP
	print(e)

#WE FIND D, THE PRIVATE KEY (WE ALREADY HAVE N) AS (D*E)%PHI(n) = 1
while (e * d) % phin != 1:
	if (d > phin):
		print("d is impossible to find... Search for any error")
		wait = input("ENTER ANY KEY TO QUIT")
		sys.exit()
    d = d + 1
    print(d)

d = d - 1

#WE PRINT E, N, AND D
print('')
print('')
print("[----------KEYS----------]")
print("e =", e, "(public)")
print("n =", n, "(public)")
print("d =", d, "(private)")
wait = input("[-----END OF PROGRAM-----]")

#e = 565
#n = 283189
#104497,138548,241808,266740,5890,45154,84918
#d = 140312
