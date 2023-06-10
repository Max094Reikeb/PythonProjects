import random

# ------------------------------------------------------------------------------------------------------------------------------------------------------

labyrinthe = 0
CellulesEnregistrees = 0
globNbrColonnes = 0
globNbrLignes = 0
Entree = 0
Sortie = 0
MursH = 0
MursV = 0

def ChoisirEntreeEtSortie():      
        """Définition de la cellule d'entrée et de sortie du labyrinthe"""
        global Entree                                           
        global Sortie
        global MursV
        global MursH
        a = random.randint(0,1)
        if a == 0:     # On enleve aléatoirement alors un mur, ici le mur est vertical, puis aléatoirement si c'est un mur de gauche ou de droite      
                b = random.randint(0,1)
                d = globNbrLignes-1
                c = random.randint(0,d)
                if b == 0:     # On enlève un mur à gauche et on choisit au hasard lequel
                        MursV[c][0] = False
                        MursV[(d-c)][globNbrColonnes] = False
                        Entree = [c,0]
                        Sortie = [d-c,globNbrColonnes-1]

                else:      # Autrement c'est un mur de droite et on choisit au hasard lequel
                        MursV[c][globNbrColonnes] = False
                        MursV[d-c][0] = False
                        Entree = [c,globNbrColonnes-1]
                        Sortie = [d-c,0]


        else:        # Autrement on enlève un mur horizontal

                b = random.randint(0,1)
                d = globNbrColonnes-1
                c = random.randint(0,d)
                if b == 0:      # On enlève un mur en haut
                        MursH[0][c] = False
                        MursH[globNbrLignes][(d-c)] = False
                        Entree = [0,c]
                        Sortie = [globNbrLignes-1,(d-c)]
                else:     # Sinon on enlève un mur du bas du labyrinthe
                        MursH[globNbrLignes][c] = False
                        MursH[0][(d-c)] = False
                        Entree = [globNbrLignes-1,c]
                        Sortie = [0,(d-c)]

def OuverturedunMurEntre2Cellules(xA, yA, xB, yB):
        """Destruction d'un mur entre 2 cellules en fonction des cordonnées des cellules A(xA,yA) et B(xB,yB) """
        if xA == xB:    # Les deux cellules étant sur la meme ligne, on enlève le mur vertical entre elles
                if yA < yB:
                        MursV[xA][yB] = False
                else:
                        MursV[xA][yA] = False

        if yA == yB:  # Les deux cellules sont sur la meme colonne, on enlève le mur horizontal entre elles
                if xA < xB:
                        MursH[xA+1][yA] = False
                else:
                        MursH[xB+1][yA] = False

def AlgoExplorationExhaustive():
        """Définition de l'algorithme permettant la création du labyrinthe"""
        global labyrinthe
        global CellulesEnregistrees
        CellulesEnregistrees = []
        labyrinthe = [[False]*(globNbrColonnes) for _ in range(globNbrLignes)]
        a = Entree[0]
        b = Entree[1]
        CaseSuivante = 0
        labyrinthe[a][b] = True
        CellulesEnregistrees.append([a,b])

        while True:
                        ## On décrit les différentes possibilités d'ouverture entre les cellules,
                        ## Différentes cas sont possibles en fonction de la position des cellules.
                listeVoisinsVisites = []                                
                if a == 0:
                        if b != 0 and b != (globNbrColonnes-1):    # Côté supérieur du labyrinthe excluant les coins
                                if labyrinthe[a+1][b] == False:
                                        listeVoisinsVisites.append([a+1,b])

                                if labyrinthe[a][b-1] == False:
                                        listeVoisinsVisites.append([a,b-1])

                                if labyrinthe[a][b+1] == False:
                                        listeVoisinsVisites.append([a,b+1])
                        else:
                                if b == 0:       # Coin supérieur gauche
                                        if labyrinthe[a+1][b] == False:
                                                listeVoisinsVisites.append([a+1,b])

                                        if labyrinthe[a][b+1] == False:
                                                listeVoisinsVisites.append([a,b+1])
                                else:   # Coin supérieur droit
                                        if labyrinthe[a+1][b] == False:
                                                listeVoisinsVisites.append([a+1,b])

                                        if labyrinthe[a][b-1] == False:
                                                listeVoisinsVisites.append([a,b-1])
                else:
                        if b == 0:
                                if a == (globNbrLignes - 1):            # Coin inférieur gauche
                                        if labyrinthe[a][b+1] == False:
                                                listeVoisinsVisites.append([a,b+1])

                                        if labyrinthe[a-1][b] == False:
                                                listeVoisinsVisites.append([a-1,b])


                                else:                                   # Côté gauche du labyrinthe en excluant les coins
                                        if labyrinthe[a][b+1] == False:
                                                        listeVoisinsVisites.append([a,b+1])

                                        if labyrinthe[a-1][b] == False:
                                                        listeVoisinsVisites.append([a-1,b])

                                        if labyrinthe[a+1][b] == False:
                                                        listeVoisinsVisites.append([a+1,b])


                        else:

                                if a == (globNbrLignes - 1):
                                        if b == (globNbrColonnes - 1):  # Coin inférieur droit
                                                if labyrinthe[a-1][b] == False:
                                                        listeVoisinsVisites.append([a-1,b])

                                                if labyrinthe[a][b-1] == False:
                                                        listeVoisinsVisites.append([a,b-1])
                                        else:                           # Côté inférieur du labyrinthe en excluant les coins                                               
                                                if labyrinthe[a][b-1] == False:
                                                        listeVoisinsVisites.append([a,b-1])

                                                if labyrinthe[a][b+1] == False:
                                                        listeVoisinsVisites.append([a,b+1])

                                                if labyrinthe[a-1][b] == False:
                                                        listeVoisinsVisites.append([a-1,b])
                                else:
                                        if b == (globNbrColonnes - 1):  # Côté droit du labyrinthe en excluant les coins
                                                if labyrinthe[a+1][b] == False:
                                                        listeVoisinsVisites.append([a+1,b])

                                                if labyrinthe[a][b-1] == False:
                                                        listeVoisinsVisites.append([a,b-1])

                                                if labyrinthe[a-1][b] == False:
                                                        listeVoisinsVisites.append([a-1,b])     
                                        else:                           # N'est pas une case en bordure du labyrinthe

                                                if labyrinthe[a+1][b] == False:
                                                        listeVoisinsVisites.append([a+1,b])

                                                if labyrinthe[a][b-1] == False:
                                                        listeVoisinsVisites.append([a,b-1])

                                                if labyrinthe[a][b+1] == False:
                                                        listeVoisinsVisites.append([a,b+1])

                                                if labyrinthe[a-1][b] == False:
                                                        listeVoisinsVisites.append([a-1,b])
        # On vient de créer une liste des voisins que l'on peut visiter
                if (len(listeVoisinsVisites) > 0):
                        nbrVoisinsNonVisites = 0
                        if (len(listeVoisinsVisites) > 1):
                                nbrVoisinsNonVisites = random.randint(0,(len(listeVoisinsVisites)-1))

                        CaseSuivante = listeVoisinsVisites.pop(nbrVoisinsNonVisites)                    # On choisit un voisin au hasard
                        CellulesEnregistrees.append([a,b])                                               # On sauvegarde la cellule courante
                        OuverturedunMurEntre2Cellules(a,b,CaseSuivante[0],CaseSuivante[1])              # On ouvre le mur entre les deux cellules
                else:
                        if (len(CellulesEnregistrees) > 0):
                                CaseSuivante = CellulesEnregistrees.pop()
                        else:
                                break
                a = CaseSuivante [0]
                b = CaseSuivante [1]
                labyrinthe[a][b] = True

def printMatrix(NbrLignes, NbrColonnes, MursH, MursV):

        """Définition du labyrinthe, avec des murs verticaux et horizontaux dans un quadrillage de taille NbrLignes*NbrColonnes"""
        # var
        ligne = 0
        colonne  = 0
        # begin
        for ligne in range(NbrLignes*2+1):
                string =""
                if (ligne%2) == 0:
                        for colonne in range(NbrColonnes*2+1):
                                if (colonne%2) == 0:
                                        string += "+"
                                else:
                                        if (MursH[ligne//2][(colonne-1)//2]) == True:
                                                string += "---"
                                        else:
                                                string += "   "
                else:
                        for colonne in range(NbrColonnes*2+1):
                                if (colonne%2) == 1:
                                        string += "   "
                                else:
                                        if (MursV[(ligne-1)//2][colonne//2]) == True:
                                                string += "|"
                                        else:
                                                string += " "
                print (string)
        # end
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
        """Programme Main du module Labyrinthe"""
        # var
        global globNbrLignes 
        global globNbrColonnes 
        global MursV
        global MursH
        global labyrinthe
        # begin
        print("%s\n%s\n%s" % ('='*80, __doc__, '='*80))
        # begin
        while True :
                while True:                                                             # Demande de reseignements sur le nombre de colonnes
                        try :
                                NbrColonnes = int(input("Entrez un nombre entier de colonnes du labyrinthe : "))
                                while NbrColonnes == 0 or NbrColonnes == 1 :
                                        NbrColonnes = int(input("Un labyrinthe doit avoir plus d'une colonne, veuillez taper un nombre entier supérieur à 1 : "))
                        except ValueError :
                                pass
                        else:
                                break
                while True:                                                             # Demande de reseignements sur le nombre de lignes
                        try :
                                NbrLignes = int(input("Entrez un nombre entier de lignes du labyrinthe : "))
                                while NbrLignes == 0 or NbrLignes == 1 :
                                        NbrLignes = int(input("Un labyrinthe doit avoir plus d'une ligne, veuillez taper un nombre entier supérieur à 1 : "))
                        except ValueError :
                                pass
                        else:
                                break
                globNbrColonnes = NbrColonnes
                globNbrLignes = NbrLignes
                MursH = [[True]*(NbrColonnes) for _ in range(NbrLignes+1)]
                MursV = [[True]*(NbrColonnes+1) for _ in range(NbrLignes)]
                ChoisirEntreeEtSortie()
                AlgoExplorationExhaustive()
                printMatrix(NbrLignes, NbrColonnes, MursH, MursV)
                recommencer = input("Voulez-vous générer un nouveau labyrinthe ? Oui ou Non : ")        # Demande sur le fait de rejouer ou non
                while recommencer != "Oui" and recommencer != "Non" :
                        recommencer = input("Voulez-vous générer un nouveau labyrinthe ? Oui ou Non : ")
                if recommencer == "Oui" :
                        pass
                elif recommencer == "Non" :
                        break
        # end
        # end
# ------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
        main()
# ======================================================================================================================================================
