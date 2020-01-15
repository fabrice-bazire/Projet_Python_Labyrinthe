# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

class Matrice : 
    def __init__(self,nbLignes,nbColonnes,valeurParDefaut=0):
        """
        crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
        valeurParDefaut dans chacune des cases
        paramètres: 
        nbLignes un entier strictement positif qui indique le nombre de lignes
        nbColonnes un entier strictement positif qui indique le nombre de colonnes
        valeurParDefaut la valeur par défaut
        résultat la matrice ayant les bonnes propriétés
        """
        res=[]

        for i in range(nbLignes):

            liste = nbColonnes * [valeurParDefaut]
            res.append(liste)

        self.mat = res

    def getNbLignes(self):
        """
        retourne le nombre de lignes de la matrice
        paramètre: matrice la matrice considérée
        """
        ligne=0
        for elem in self.mat:
            ligne += 1
        return ligne

    def getNbColonnes(self):
        """
        retourne le nombre de colonnes de la matrice
        paramètre: matrice la matrice considérée
        """
        colonne=0
        element=0
        ligne = self.getNbLignes()
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                element+=1
        colonne = element//ligne
        return colonne

    def getVal(self,ligne,colonne):
        """
        retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
        paramètres: matrice la matrice considérée
                    ligne le numéro de la ligne (en commençant par 0)
                    colonne le numéro de la colonne (en commençant par 0)
        """
        return self.mat[ligne][colonne]

    def setVal(self,ligne,colonne,valeur):
        """
        met la valeur dans la case se trouve en (ligne,colonne) de la matrice
        paramètres: matrice la matrice considérée
                    ligne le numéro de la ligne (en commençant par 0)
                    colonne le numéro de la colonne (en commençant par 0)
                    valeur la valeur à stocker dans la matrice
        cette fonction ne retourne rien mais modifie la matrice
        """
        liste=self.mat
        liste[ligne].pop(colonne)
        liste[ligne].insert(colonne,valeur)
        self.mat=liste


    #------------------------------------------        
    # decalages
    #------------------------------------------
    def decalageLigneAGauche(self, numLig, nouvelleValeur=0):
        """
        permet de décaler une ligne vers la gauche en insérant une nouvelle
        valeur pour remplacer la premiere case à droite de cette ligne
        le fonction retourne la valeur qui a été éjectée
        paramèteres: matrice la matrice considérée
                    numLig le numéro de la ligne à décaler
                    nouvelleValeur la valeur à placer
        résultat la valeur qui a été ejectée lors du décalage
        """
        j = 0
        res = self.mat[numLig][0]
        while j < self.getNbColonnes()-1:
            self.setVal(numLig,j,self.getVal(numLig,j+1))
            j+=1
        self.setVal(numLig,self.getNbColonnes()-1,nouvelleValeur)
        return res

    def decalageLigneADroite(self, numLig, nouvelleValeur=0):
        """
        decale la ligne numLig d'une case vers la droite en insérant une nouvelle
        valeur pour remplacer la premiere case à gauche de cette ligne
        paramèteres: matrice la matrice considérée
                    numLig le numéro de la ligne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        j = self.getNbColonnes()-1
        res = self.mat[numLig][j]
        while j > 0:
            self.setVal(numLig,j,self.getVal(numLig,j-1))
            j-=1
        self.setVal(numLig,0,nouvelleValeur)
        return res

    def decalageColonneEnHaut(self, numCol, nouvelleValeur=0):
        """
        decale la colonne numCol d'une case vers le haut en insérant une nouvelle
        valeur pour remplacer la premiere case en bas de cette ligne
        paramèteres: matrice la matrice considérée
                    numCol le numéro de la colonne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        i = 0
        res = self.mat[0][numCol]
        while i < self.getNbLignes()-1:
            self.setVal(i,numCol,self.getVal(i+1,numCol))
            i+=1
        self.setVal(self.getNbLignes()-1,numCol,nouvelleValeur)
        return res

    def decalageColonneEnBas(self, numCol, nouvelleValeur=0):
        """
        decale la colonne numCol d'une case vers le bas en insérant une nouvelle
        valeur pour remplacer la premiere case en haut de cette ligne
        paramèteres: matrice la matrice considérée
                    numCol le numéro de la colonne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        i = self.getNbLignes()-1
        res = self.mat[i][numCol]
        while i > 0:
            self.setVal(i,numCol,self.getVal(i-1,numCol))
            i-=1
        self.setVal(i,numCol,nouvelleValeur)
        return res


    def afficheLigneSeparatrice(self,tailleCellule=4):
        ''' 
        fonction annexe pour afficher les lignes séparatrices
        paramètres: matrice la matrice à afficher
                    tailleCellule la taille en nb de caractères d'une cellule
        résultat: cette fonction ne retourne rien mais fait un affichage
        '''
        print()
        for i in range(self.getNbColonnes()+1):
            print('-'*tailleCellule+'+',end='')
        print()

    def affiche_matrice(self,tailleCellule=4):
        '''
        affiche le contenue d'une matrice présenté sous le format d'une grille
        paramètres: matrice la matrice à afficher
                    tailleCellule la taille en nb de caractères d'une cellule
        résultat: cette fonction ne retourne rien mais fait un affichage
        '''

        nbColonnes=self.getNbColonnes()
        nbLignes=self.getNbLignes()
        print(' '*tailleCellule+'|',end='')
        for i in range(nbColonnes):
            print(str(i).center(tailleCellule)+'|',end='')
        self.afficheLigneSeparatrice(tailleCellule)
        for i in range(nbLignes):
            print(str(i).rjust(tailleCellule)+'|',end='')
            for j in range(nbColonnes):
                print(str(self.getVal(i,j)).rjust(tailleCellule)+'|',end='')
            self.afficheLigneSeparatrice(tailleCellule)
        print()