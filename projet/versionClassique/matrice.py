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

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
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

    return res

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    ligne=0
    for elem in matrice:
        ligne += 1
    return ligne

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    colonne=0
    element=0
    ligne = getNbLignes(matrice)
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            element+=1
    colonne = element//ligne
    return colonne

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    liste=matrice
    liste[ligne].pop(colonne)
    liste[ligne].insert(colonne,valeur)
    matrice=liste


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
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
    res = matrice[numLig][0]
    while j < getNbColonnes(matrice)-1:
        setVal(matrice,numLig,j,getVal(matrice,numLig,j+1))
        j+=1
    setVal(matrice,numLig,getNbColonnes(matrice)-1,nouvelleValeur)
    return res

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    j = getNbColonnes(matrice)-1
    res = matrice[numLig][j]
    while j > 0:
        setVal(matrice,numLig,j,getVal(matrice,numLig,j-1))
        j-=1
    setVal(matrice,numLig,0,nouvelleValeur)
    return res

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    i = 0
    res = matrice[0][numCol]
    while i < getNbLignes(matrice)-1:
        setVal(matrice,i,numCol,getVal(matrice,i+1,numCol))
        i+=1
    setVal(matrice,getNbLignes(matrice)-1,numCol,nouvelleValeur)
    return res

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    i = getNbLignes(matrice)-1
    res = matrice[i][numCol]
    while i > 0:
        setVal(matrice,i,numCol,getVal(matrice,i-1,numCol))
        i-=1
    setVal(matrice,i,numCol,nouvelleValeur)
    return res


def afficheLigneSeparatrice(matrice,tailleCellule=4):
    ''' 
    fonction annexe pour afficher les lignes séparatrices
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()

def affiche_matrice(matrice,tailleCellule=4):
    '''
    affiche le contenue d'une matrice présenté sous le format d'une grille
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''

    nbColonnes=getNbColonnes(matrice)
    nbLignes=getNbLignes(matrice)
    print(' '*tailleCellule+'|',end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule)+'|',end='')
    afficheLigneSeparatrice(matrice,tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule)+'|',end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice,i,j)).rjust(tailleCellule)+'|',end='')
        afficheLigneSeparatrice(matrice,tailleCellule)
    print()

#matrice = [[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]]

#affiche_matrice(matrice)

#decalageColonneEnHaut(matrice,4,917)

#affiche_matrice(matrice)