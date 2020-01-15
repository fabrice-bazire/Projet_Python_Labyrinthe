# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans

   Module plateau
   ~~~~~~~~~~~~~~

   Ce module gère le plateau de jeu.
"""

from matrice import *
from carte import *


def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    les_tresors = []
    for indice in range(13) :
        les_tresors.append(indice+1)
    random.shuffle(les_tresors)
    plateau = Matrice(7,7)
    setVal(plateau,0,0,Carte(True, False, False, True))
    setVal(plateau,0,6,Carte(True, True, False, False))
    setVal(plateau,6,0,Carte(False, False, True, True))
    setVal(plateau,6,6,Carte(False, True, True, False))
    setVal(plateau, 0, 2, Carte(True, False, False, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 0, 4, Carte(True, False, False, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 2, 4, Carte(True, False, False, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 2, 0, Carte(False, False, False, True, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 2, 2, Carte(False, False, False, True, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 2, 4, Carte(False, False, False, True, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 2, 6, Carte(False, True, False, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 4, 6, Carte(False, True, False, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 4, 4, Carte(False, True, False, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 4, 2, Carte(False, False, True, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 6, 2, Carte(False, False, True, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 6, 4, Carte(False, False, True, False, les_tresors[0]))
    les_tresors.pop(0)
    setVal(plateau, 4, 0, Carte(False, False, False, True, les_tresors[0]))
    les_tresors.pop(0)
    les_cartes_amovibles = creerCartesAmovibles(14, nbTresors)
    for lig in range(getNbLignes(plateau)) :
        for col in range(getNbColonnes(plateau)) :
            if lig % 2 == 1 or col % 2 == 1 :
                setVal(plateau, lig, col, les_cartes_amovibles[0])
                les_cartes_amovibles.pop(0)
    return (plateau, 0)


def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    liste=[]
    i=0
    liste_tresor = []
    liste_tresor.append(tresorDebut)
    while len(liste_tresor)<nbTresors:
        liste_tresor.append(tresorDebut)
        tresorDebut+=1
    while len(liste)<16:
        liste.append(Carte(False, True, False, True))
    while len(liste)<28:
        liste.append(Carte(True,True,False,False))
    while len(liste)<34:
        liste.append(Carte(False,False,False,True))
    random.shuffle(liste)
    for element in liste:
        tourneAleatoire(element)
    for tresor in liste_tresor:
        if i < len(liste) :
            mettreTresor(liste[i],tresor)
        i+=1
    random.shuffle(liste)
    return liste


def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    if plateau[lig][col]['tresor'] == numTresor :
        plateau[lig][col]['tresor'] = 0
        return True
    else :
        return False

def getCoordonneesTresor(plateau,numTresor):
    """"
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for ligne in range(7):
        for colonne in range(7):
            if plateau[ligne][colonne]['tresor'] == numTresor :
                return (ligne, colonne)
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for ligne in range(7):
        for colonne in range(7):
            if numJoueur in plateau[ligne][colonne]['pions']:
                return (ligne, colonne)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    plateau[lin][col]['pions'].pop(numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    plateau[lin][col]['pions'].append(numJoueur)

def marquageDirect(calque,plateau,val,marque):
    """
    marque avec la valeur marque les éléments du calque tel que la valeur
    correspondante n'est pas un mur (de valeur differente de 1) et
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    """
    nbLigne = getNbLignes(plateau)
    nbCol = getNbColonnes(plateau)
    estMarque = False


    for i in range (nbLigne):

        for j in range(nbCol):

            # Vérification voisin du dessous
            if (i + 1) < getNbLignes(plateau):
                if getVal(calque, (i + 1) , j) > 0 and getVal(calque, i , j) == 0 :
                    if passageSud(getVal(plateau,i,j),getVal(plateau,i+1,j)):
                        setVal(calque,i,j,marque)
                        estMarque = True


            # Vérification voisin du dessus
            if (i - 1) >= 0 :
                if getVal(calque, (i-1),j) > 0 and getVal(calque, i , j) == 0 :
                    if passageNord(getVal(plateau,i,j),getVal(plateau,i-1,j)):
                        setVal(calque,i,j,marque)
                        estMarque = True

            # Vérification voisin de droite
            if (j + 1) < getNbColonnes(plateau):
                if getVal(calque, i, (j+1)) > 0 and getVal(calque, i , j) == 0 :
                    if passageEst(getVal(plateau,i,j),getVal(plateau,i,j+1)):
                        setVal(calque,i,j,marque)
                        estMarque = True

            # Vérification voisin de gauche
            if (j - 1) >= 0:
                if getVal(calque, i, (j-1)) > 0 and getVal(calque, i , j) == 0 :
                    if passageOuest(getVal(plateau,i,j),getVal(plateau,i,j-1)):
                        setVal(calque,i,j,marque)
                        estMarque = True

    return estMarque


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    nbLigne = getNbLignes(plateau)
    nbCol = getNbColonnes(plateau)
    calque=Matrice(nbLigne,nbCol)
    setVal(calque,0,0,1)

    boucle = True
    while boucle:
        boucle = marquageDirect(calque,plateau,1,1)

    return getVal(calque,ligD,colD) > 0 and getVal(calque,ligA,colA) > 0


def marquageDirect2(calque,plateau):
    """
    marque avec la valeur marque les éléments du calque tel que la valeur
    correspondante n'est pas un mur (de valeur differente de 1) et
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    """
    nbLigne = getNbLignes(plateau)
    nbCol = getNbColonnes(plateau)
    marquageFait = False

    for i in range (nbLigne):

        for j in range(nbCol):

            # Vérification voisin du dessous
            if (i + 1) < getNbLignes(plateau):
                val = getVal(calque,i+1,j)
                if getVal(calque, (i + 1) , j) > 0 and getVal(calque, i , j) == 0 :
                    if passageSud(getVal(plateau,i,j),getVal(plateau,i+1,j)):
                        setVal(calque,i,j,val+1)
                        marquageFait = True


            # Vérification voisin du dessus
            if (i - 1) >= 0 :
                val = getVal(calque,i-1,j)
                if getVal(calque, (i-1),j) > 0 and getVal(calque, i , j) == 0 :
                    if passageNord(getVal(plateau,i,j),getVal(plateau,i-1,j)):
                        setVal(calque,i,j,val+1)
                        marquageFait = True

            # Vérification voisin de droite
            if (j + 1) < getNbColonnes(plateau):
                val = getVal(calque,i,j+1)
                if getVal(calque, i, (j+1)) > 0 and getVal(calque, i , j) == 0 :
                    if passageEst(getVal(plateau,i,j),getVal(plateau,i,j+1)):
                        setVal(calque,i,j,val+1)
                        marquageFait = True

            # Vérification voisin de gauche
            if (j - 1) >= 0:
                val = getVal(calque,i,j-1)
                if getVal(calque, i, (j-1)) > 0 and getVal(calque, i , j) == 0 :
                    if passageOuest(getVal(plateau,i,j),getVal(plateau,i,j-1)):
                        setVal(calque,i,j,val+1)
                        marquageFait = True

    return marquageFait


def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin,
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """

    if accessible(plateau,ligD,colD,ligA,colA):

        calque=Matrice(getNbLignes(plateau),getNbColonnes(plateau))
        liste_coordonees = [(ligA,colA)]
        setVal(calque,0,0,1)

        tour = True
        while tour:
            tour = marquageDirect2(calque,plateau)
        val = getVal(calque,ligA,colA)

        # Test d'affichage
        #affiche_matrice(calque)

        # Tant que les lig et col ne sont pas egales
        while ligD != ligA and colD != colA:

            #Vérification voisin du dessus
            if ligA - 1 >= 0 and getVal(calque,ligA,colA)-1 == getVal(calque,ligA - 1,colA):
                    liste_coordonees.append((ligA,colA))
                    val = getVal(calque,ligA - 1,colA)

                    ligA -= 1

            #Vérification voisin du dessous
            if ligA + 1 < getNbLignes(calque) and getVal(calque,ligA,colA)-1 == getVal(calque,ligA + 1,colA):
                    liste_coordonees.append((ligA,colA))
                    val = getVal(calque,ligA + 1,colA)

                    ligA += 1

            #Vérification voisin de gauche
            if colA - 1 >= 0 and getVal(calque,ligA,colA)-1 == getVal(calque,ligA,colA - 1):
                    liste_coordonees.append((ligA,colA))
                    val = getVal(calque,ligA,colA - 1)

                    colA -= 1

            #Vérification voisin du droite
            if colA + 1 < getNbColonnes(calque) and getVal(calque,ligA,colA)-1 == getVal(calque,ligA,colA + 1):
                    liste_coordonees.append((ligA,colA))
                    val = getVal(calque,ligA,colA + 1)

                    colA += 1

            liste_coordonees.reverse()
            return liste_coordonees
    else:
        return []



#---------------------------------------------------------------------------#
def affichePlateau(plateau):
    for lig in range(getNbLignes(plateau)) :
        for col in range(getNbColonnes(plateau)) :
            print('carte[', lig, '][', col, '] : ', plateau[lig][col])
        print('\n\n')



#p,_ = Plateau(4,24)
#print(accessible(p,0,0,2,1))
#print(accessibleDist(p,0,0,2,1))
#affiche_matrice(accessible(p,0,0,0,3))

#affichePlateau(p)
