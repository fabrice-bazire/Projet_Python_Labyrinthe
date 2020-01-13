from matriceAPI2 import *

#-----------------------------------------
# entrées sorties sur les matrices
#-----------------------------------------
def sauveMatrice(matrice,nomFic):
    '''
    '''
    fic=open(nomFic,'w')
    ligne=str(getNbLignes(matrice))+','+str(getNbColonnes(matrice))+'\n'
    fic.write(ligne)
    for i in range(getNbLignes(matrice)):
        ligne=''
        for j in range(getNbColonnes(matrice)-1):
            val=getVal(matrice,i,j)
            if val==None:
                ligne+=','
            else:
                ligne+=str(val)+','
                val=getVal(matrice,i,j+1)
            if val==None:
                ligne+='\n'
            else:
                ligne+=str(val)+'\n'
    fic.write(ligne)
    fic.close()

def chargeMatrice(nomFic,typeVal='int'):
    '''
    '''
    fic=open(nomFic,'r')
    ligneLinCol=fic.readline()
    listeLinCol=ligneLinCol.split(',')
    matrice=Matrice(int(listeLinCol[0]),int(listeLinCol[1]))
    i=0  
    for ligne in fic:
        listeVal=ligne.split(",")
        j=0
        for elem in listeVal:
            if elem=="" or elem=="\n":
                setVal(matrice,i,j,None)
            elif typeVal=='int':
                setVal(matrice,i,j,int(elem))
            elif typeVal=='float':
                setVal(matrice,i,j,float(elem))
            elif typeVal=='bool':
                setVal(matrice,i,j,bool(elem))
            else:
                setVal(matrice,i,j,elem)
            j+=1
        i+=1
    return matrice

def afficheLigneSeparatrice(matrice,tailleCellule=4):
    '''
    Affichage d'une matrice
    fonction annexe pour afficher les lignes séparatrices
    '''
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()
   
def afficheMatrice(matrice,tailleCellule=4):
    '''
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


   
#--------------------------------
# fonctions sur les labyrinthes
#--------------------------------

def marquageDirect(calque,mat,val,marque):
    '''
    marque avec la valeur marque les éléments du calque tel que la valeur 
    correspondante n'est pas un mur (de valeur differente de 1) et 
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    '''
    nbLigne = getNbLignes(mat)
    nbCol = getNbColonnes(mat)
    estMarqué = False

    for i in range (nbLigne):

        for j in range(nbCol):

            if getVal(mat,i,j)!=1 and getVal(calque,i,j) == 0:
                
                # Vérification voisin du dessous
                if i<nbLigne-1 and getVal(calque,i+1,j) == val :
                        setVal(calque,i,j,marque)
                        estMarqué = True

                # Vérification voisin du dessus
                if i-1>=0 and getVal(calque,i-1,j) == val :
                        setVal(calque,i,j,marque)
                        estMarqué = True

                # Vérification voisin de droite
                if j<nbCol-1 and getVal(calque,i,j+1) == val :
                        setVal(calque,i,j,marque)
                        estMarqué = True

                # Vérification voisin de gauche
                if j-1>=0 and getVal(calque,i,j-1) == val :
                        setVal(calque,i,j,marque)
                        estMarqué = True

    return estMarqué

def estAccessible(mat,pos1,pos2):
    '''
    verifie qu'il existe un chemin entre pos1 et pos2 dans la matrice mat
    '''
    nbLigne = getNbLignes(mat)
    nbCol = getNbColonnes(mat)

    calque=Matrice(nbLigne,nbCol)
    setVal(calque,0,0,1)

    estMarqué = True

    while estMarqué:
        estMarqué = marquageDirect(calque,mat,1,1)

    if getVal(calque,pos1[0],pos1[1]) > 0 and getVal(calque,pos2[0],pos2[1]) > 0 :
        res = True
    else:
        res =  False
    return res
    
def labyrintheValide(mat):
    '''
    verifie qu'il existe un chemin entre la case en haut à gauche et la case
    en bas à droite de la matrice
    '''
    nbLigne = getNbLignes(mat)
    nbCol = getNbColonnes(mat)
    return estAccessible(mat,(0,0),(nbLigne-1,nbCol-1))

def estAccessible2(mat,pos1,pos2):
    '''
    vérifie l'accessibilité entre deux positions mais en calculant le nombre de cases
    depuis le point de départ
    la fonction retourne le calque si les deux cases sont accessibles et None sinon
    '''
    nbLigne = getNbLignes(mat)
    nbCol = getNbColonnes(mat)
    val = 1
    marquage = val + 1

    calque=Matrice(nbLigne,nbCol)
    setVal(calque,0,0,1)

    estMarqué = True

    while estMarqué:
        estMarqué = marquageDirect(calque,mat,val,marquage)
        val += 1
        marquage = val + 1

    if getVal(calque,pos1[0],pos1[1]) > 0 and getVal(calque,pos2[0],pos2[1]) > 0 :
        afficheMatrice(calque)
        res = calque
    else:
        res =  None
    return res



def cheminDecroissant(calque,pos1,pos2):
    '''
    recherche un chemin décroissant à partir de pos1 vers pos2
    le chemin est une liste de positions
    la fonction suppose que le calque contient effectivement les valeurs permettant
    de retrouver ce chemin
    '''
    (x,y)=pos1
    (x2,y2)=pos2
    for i in range(len(calque)):
        for j in range(len(calque[i])):
            while i != x2 and j != y2:
                if i == x and j == y 
                    if getVal(calque,i,j-1) == getVal(calque,x,y)-1:

                        #Vérifie si la valeur autour vaut val -1
                        # Faire quoi ?



def plusCourtChemin(matrice,pos1,pos2):
    '''
    recherche le plus court chemin entre pos1 et pos2. 
    s'il n'y pas de chemin entre ces deux positions la fonction retourne None
    sinon elle retourne le chemin
    '''
    pass





#Matrice calque : initiale 1 au depart et que des 0
# Taille de la matrice = taille calque

# Si 0 succeptible d'etre marqué 
#on regarde autour si une case a 1 si oui on marque la case (faire pour chaque)

# Pour chaque ligne
# Pour chaque colonne
# Si position est couloir
# Si autour de position = un chemin marqué
# Marqué la position 
# Si au moins un marquage effectuer, on recommence, jusqu'a plus de changement
# 3 tours = inondation marquage laby
# 1 tour (pas de changement) de "verification"

#Pour chaque 1 (chemin) on additione et devient le numéro de la case 

#Si chemin alors est-ce que marquage possible ?

# 1  0  0  0  0  0  0
# 1  1  1  0  0  0  0
# 0  0  1  0  0  0  0
# 0  0  1  0  1  1  1
# 0  0  1  1  1  0  1
# 0  0  0  1  0  0  1
# 0  0  0  1  0  0  1
# 0  0  0  1  0  0  1
# 0  0  0  1  1  0  1
# 0  0  0  0  1  1  1

#______________________

# 1  0  0  0  0  0  0

# 2  3  4  0  0  0  0 

# 0  0  5  0  0  0  0

# 0  0  6  0  10 11 12

# 0  0  7  8  9  0  13

# 0  0  0  9  0  0  14

# 0  0  0  10 0  0  15

# 0  0  0  11 0  0  16

# 0  0  0  12 13 0  17

# 0  0  0  0  14 15 17
#______________________

#departs arrive = 17 plus court
#17 chemins plus petits

#Coordonnées : (x,y)

# Voisins : (x+1,y)
#           (x-1,y)
#           (x,y+1)
#           (x,y-1)

#val et marque change au fur et a mesure de la fonction

#estMarqué = False
# pour i in range (nbLigne)
#   pour j in range (nbCol)
#       si cette case est susceptible d'etre marquée ...
#       si un des voisins a été marqué avec la valeur val
#       alors
#           cette case est marqué avec la valeur marque
# estMarqué = True