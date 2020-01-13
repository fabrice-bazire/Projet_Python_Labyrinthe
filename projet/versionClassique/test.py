#for tresor in range(1, nbTresors, 1) :
#        joueur_random = random.randint(1,getNbJoueurs(joueurs))
#        if nbTresorMax != 0 :
#            if getNbJoueurs(joueurs) == 2 :
#                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]):
#                    joueurs[0][joueur_random][1].append(tresor)
#            if getNbJoueurs(joueurs) == 3 :
#                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) :
#                    
#            if getNbJoueurs(joueurs) == 4 :
#                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) and len(joueurs[0][0][1]) == len(joueurs[0][3][1]) :                    
#                    joueurs[0][joueur_random][1].append(tresor)
#        else : 
#            if getNbJoueurs(joueurs) == 2 :
#                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]):
#                    joueurs[0][joueur_random][1].append(tresor)
#            if getNbJoueurs(joueurs) == 3 :
#                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) :
#            if getNbJoueurs(joueurs) == 4 :
#                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) and len(joueurs[0][0][1]) == len(joueurs[0][3][1]) :                    
#                    joueurs[0][joueur_random][1].append(tresor)

import random

from matrice import *

def aff_matrice (m) :
    for ligne in range(getNbLignes(m)) :
        for colonne in range(getNbColonnes(m)):
            print(getVal(m, ligne, colonne))
            print(", ")
        print("\n")

m = Matrice(2,2, 0)
setVal(m, 0, 0, 1)
setVal(m, 0, 1, 2)
setVal(m, 1, 0, 3)
setVal(m, 1, 1, 4)
#aff_matrice(m)
nbTresors = 6
les_tresors_affectes = set()
les_tresors = []
for ligne in range(7) : 
    for colonne in range(7):
        tresor = random.randint(0,nbTresors)
        while tresor in les_tresors_affectes and tresor != 0 :
            if len(les_tresors_affectes) == nbTresors :
                tresor = 0
            else : 
                tresor = random.randint(0,nbTresors)
        les_tresors.append(tresor)
        les_tresors_affectes.add(tresor)

print(les_tresors)

def nb_occ (liste, nb):
    nbocc = 0
    for elem in liste : 
        if elem == nb :
            nbocc += 1
    return nbocc

def doublons (liste) : 
    for elem in liste : 
        if nb_occ(liste, elem) > 1 and elem != 0:
            return True 
    return False

print(doublons(les_tresors))

