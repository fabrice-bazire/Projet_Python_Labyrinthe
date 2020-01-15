# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans

   Module plateau
   ~~~~~~~~~~~~~~

   Ce module gère le plateau de jeu.
"""

from matriceOO import *
from carteOO import *

class Plateau :
    def __init__(self, nbJoueurs, nbTresors):
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
        self.setVal(0,0,Carte(True, False, False, True))
        self.setVal(0,6,Carte(True, True, False, False))
        self.setVal(6,0,Carte(False, False, True, True))
        self.setVal(6,6,Carte(False, True, True, False))
        self.setVal(0, 2, Carte(True, False, False, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(0, 4, Carte(True, False, False, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(2, 4, Carte(True, False, False, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(2, 0, Carte(False, False, False, True, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(2, 2, Carte(False, False, False, True, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(2, 4, Carte(False, False, False, True, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(2, 6, Carte(False, True, False, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(4, 6, Carte(False, True, False, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(4, 4, Carte(False, True, False, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(4, 2, Carte(False, False, True, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(6, 2, Carte(False, False, True, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(6, 4, Carte(False, False, True, False, les_tresors[0]))
        les_tresors.pop(0)
        self.setVal(4, 0, Carte(False, False, False, True, les_tresors[0]))
        les_cartes_amovibles = creerCartesAmovibles(14, nbTresors)
        for lig in range(self.getNbLignes()) :
            for col in range(self.getNbColonnes()) :
                if lig % 2 == 1 or col % 2 == 1 :
                    self.setVal(lig, col, les_cartes_amovibles[0])
                    les_cartes_amovibles.pop(0)
        self.plateau = plateau
        self.carte_amovible = les_cartes_amovibles[0]

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

    def prendreTresorPlateau(self,lig,col,numTresor):
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
        if self.plateau[lig][col].tresor == numTresor :
            self.plateau[lig][col].tresor = 0
            return True
        else :
            return False

    def getCoordonneesTresor(self,numTresor):
        """
        retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
        paramètres: plateau: le plateau considéré
                    numTresor: le numéro du trésor à trouver
        resultat: un couple d'entier donnant les coordonnées du trésor ou None si
                le trésor n'est pas sur le plateau
        """
        for ligne in range(7):
            for colonne in range(7):
                if self.plateau[ligne][colonne].tresor == numTresor :
                    return (ligne, colonne)
        return None

    def getCoordonneesJoueur(self,numJoueur):
        """
        retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
        paramètres: plateau: le plateau considéré
                    numJoueur: le numéro du joueur à trouver
        resultat: un couple d'entier donnant les coordonnées du joueur ou None si
                le joueur n'est pas sur le plateau
        """
        for ligne in range(7):
            for colonne in range(7):
                if numJoueur in self.plateau[ligne][colonne].pions:
                    return (ligne, colonne)
        return None

    def prendrePionPlateau(self,lin,col,numJoueur):
        """
        prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
        paramètres: plateau:le plateau considéré
                    lin: numéro de la ligne où se trouve le pion
                    col: numéro de la colonne où se trouve le pion
                    numJoueur: le numéro du joueur qui correspond au pion
        Cette fonction ne retourne rien mais elle modifie le plateau
        """
        self.plateau[lin][col].pions.pop(numJoueur)

    def poserPionPlateau(self,lin,col,numJoueur):
        """
        met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
        paramètres: plateau:le plateau considéré
                    lin: numéro de la ligne où se trouve le pion
                    col: numéro de la colonne où se trouve le pion
                    numJoueur: le numéro du joueur qui correspond au pion
        Cette fonction ne retourne rien mais elle modifie le plateau
        """
        self.plateau[lin][col].pions.append(numJoueur)


    def marquageDirect(calque,self,val,marque):
        """
        marque avec la valeur marque les éléments du calque tel que la valeur
        correspondante n'est pas un mur (de valeur differente de 1) et
        qu'un de ses voisins dans le calque à pour valeur val
        la fonction doit retourner True si au moins une case du calque a été marquée
        """
        nbLigne = self.getNbLignes()
        nbCol = self.getNbColonnes()
        estMarque = False


        for i in range (nbLigne):

            for j in range(nbCol):

                # Vérification voisin du dessous
                if (i + 1) < nbLigne:
                    if calque.getVal(i+1,j) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i+1,j)):
                            calque.setVal(i,j,marque)
                            estMarque = True


                # Vérification voisin du dessus
                if (i - 1) >= 0 :
                    if calque.getVal(i-1,j) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i-1,j)):
                            calque.setVal(i,j,marque)
                            estMarque = True

                # Vérification voisin de droite
                if (j + 1) < nbCol:
                    if calque.getVal(i,j+1) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i,j+1)):
                            calque.setVal(i,j,marque)
                            estMarque = True

                # Vérification voisin de gauche
                if (j - 1) >= 0:
                    if calque.getVal(i,j-1) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i,j-1)):
                            calque.setVal(i,j,marque)
                            estMarque = True

        return estMarque


    def accessible(self,ligD,colD,ligA,colA):
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
        nbLigne = self.getNbLignes()
        nbCol = self.getNbColonnes()
        calque=new Matrice(nbLigne,nbCol) # A VERIFIER POUR LE NEW
        calque.setVal(0,0,1)

        boucle = True
        while boucle:
            boucle = self.marquageDirect(calque,1,1)

        return calque.getVal(ligD,colD) > 0 and calque.getVal(ligA,colA) > 0


    def marquageDirect2(calque,self):
        """
        marque avec la valeur marque les éléments du calque tel que la valeur
        correspondante n'est pas un mur (de valeur differente de 1) et
        qu'un de ses voisins dans le calque à pour valeur val
        la fonction doit retourner True si au moins une case du calque a été marquée
        """
        nbLigne = self.getNbLignes()
        nbCol = self.getNbColonnes()
        marquageFait = False

        for i in range (nbLigne):

            for j in range(nbCol):

                # Vérification voisin du dessous
                if (i + 1) < nbLigne:
                    val = calque.getVal(i+1,j)
                    if calque.getVal(i+1,j) > 0 and calque.getVal(i , j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i+1,j)):
                            calque.setVal(i,j,val+1)
                            marquageFait = True


                # Vérification voisin du dessus
                if (i - 1) >= 0 :
                    val = calque.getVal(i-1,j)
                    if calque.getVal(i-1,j) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i-1,j)):
                            calque.setVal(i,j,val+1)
                            marquageFait = True

                # Vérification voisin de droite
                if (j + 1) < nbCol:
                    val = calque.getVal(i,j+1)
                    if calque.getVal(i,j+1) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i,j+1)):
                            calque.setVal(i,j,val+1)
                            marquageFait = True

                # Vérification voisin de gauche
                if (j - 1) >= 0:
                    val = calque.getVal(i,j-1)
                    if calque.getVal(i,j-1) > 0 and calque.getVal(i,j) == 0 :
                        if self.getVal(i,j).passageSud(self.getVal(i,j-1)):
                            calque.setVal(i,j,val+1)
                            marquageFait = True

        return marquageFait


    def accessibleDist(self,ligD,colD,ligA,colA):
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

        if accessible(self,ligD,colD,ligA,colA):

            calque = new Matrice(self.getNbLignes(),self.getNbColonnes())
            liste_coordonees = [(ligA,colA)]
            calque.setVal(0,0,1)

            tour = True
            while tour:
                tour = self.marquageDirect2(calque)
            val = calque.getVal(ligA,colA)

            # Test d'affichage
            #affiche_matrice(calque)

            # Tant que les lig et col ne sont pas egales
            while ligD != ligA and colD != colA:

                #Vérification voisin du dessus
                if ligA - 1 >= 0 and calque.getVal(ligA,colA)-1 == calque.getVal(ligA - 1,colA):
                        liste_coordonees.append((ligA,colA))
                        val = calque.getVal(ligA - 1,colA)

                        ligA -= 1

                #Vérification voisin du dessous
                if ligA + 1 < calque.getNbLignes(calque) and calque.getVal(ligA,colA)-1 == calque.getVal(ligA + 1,colA):
                        liste_coordonees.append((ligA,colA))
                        val = calque.getVal(ligA + 1,colA)

                        ligA += 1

                #Vérification voisin de gauche
                if colA - 1 >= 0 and calque.getVal(ligA,colA)-1 == calque.getVal(ligA,colA - 1):
                        liste_coordonees.append((ligA,colA))
                        val = calque.getVal(ligA,colA - 1)

                        colA -= 1

                #Vérification voisin du droite
                if colA + 1 < calque.getNbColonnes() and calque.getVal(ligA,colA)-1 == calque.getVal(ligA,colA + 1):
                        liste_coordonees.append((ligA,colA))
                        val = calque.getVal(ligA,colA + 1)

                        colA += 1

                liste_coordonees.reverse()
                return liste_coordonees
        else:
            return []
