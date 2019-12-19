# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans

   Module carte
   ~~~~~~~~~~~~

   Ce module gère les cartes du labyrinthe.
"""
import random


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']
#             0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    carte = {'nord':nord,'est':est,'sud':sud,'ouest':ouest,'tresor':tresor,'pions':pions }

    return carte


def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    cpt=0
    if (c['nord']):
        cpt+=1
    if (c['sud']):
        cpt+=1
    if (c['est']):
        cpt+=1
    if (c['ouest']):
        cpt+=1
    if cpt<3:
        res=True
    else:
        res=False
    return res



def murNord(c):
    """print(len(c['pions']))if c['nord']:
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['nord']


def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte( nord, est, sud, ouest, tresor=0, pions=[]
    """
    return c['sud']
def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['est']

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c['ouest']

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['pions']



def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['pions']=listePions

def getNbPions(c):
    """print(len(c['pions']))
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    if len(c['pions'])>0:
        res=len(c['pions'])
    else:
        res=0
    return res
def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    res= False
    for pions in c['pions']:
        if pion == pions:
            res=True
    return res

def getTresor(c):
    """( nord, est, sud, ouest, tresor=0, pions=[]
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['tresor']

def prendreTresor(c):
    """if c['nord']:
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """

    ancient_tresor=getTresor(c)
    c['tresor']=0
    return ancient_tresor


def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res= prendreTresor(c)
    c['tresor']=tresor
    return res

def prendrePion(c,pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    for indice in range(len(c['pions'])):
        if c['pions'][indice]==pion:
            c['pions'].pop(indice)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if not possedePion(c,pion):
        c['pions'].append(pion)





def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    Sud=c['sud']
    Est=c['est']
    Ouest=c['ouest']
    Nord=c['nord']
    c['nord']=Ouest
    c['est']=Nord
    c['sud']=Est
    c['ouest']=Sud

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    Sud=c['sud']
    Est=c['est']
    Ouest=c['ouest']
    Nord=c['nord']
    c['nord']=Est
    c['est']=Sud
    c['sud']=Ouest
    c['ouest']=Nord



def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    c['nord']=(random.randint(0,20))*tournerHoraire(c)
    c['est']=(random.randint(0,20))*tournerHoraire(c)
    c['sud']=(random.randint(0,20))*tournerHoraire(c)
    c['ouest']=(random.randint(0,20))*tournerHoraire(c)

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire
    est de la forme bNbEbSbO où bN, bE, bS et bO valent
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res=0
    if c['nord']:
        res+=1
    if c['est']:
        res+=2
    if c['sud']:
        res+=4
    if c['ouest']:
        res+=8
    return res



def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    if code==0:
        c['nord']=False
        c['est']=False
        c['sud']=False
        c['ouest']=False
    if code==1:
        c['nord']=True
        c['est']=False
        c['sud']=False
        c['ouest']=False
    if code==2:
        c['nord']=False
        c['est']=True
        c['sud']=False
        c['ouest']=False
    if code==3:
        c['nord']=True
        c['est']=True
        c['sud']=False
        c['ouest']=False
    if code==4:
        c['nord']=False
        c['est']=False
        c['sud']=True
        c['ouest']=False
    if code==5:
        c['nord']=True
        c['est']=False
        c['sud']=True
        c['ouest']=False
    if code==6:
        c['nord']=False
        c['est']=True
        c['sud']=True
        c['ouest']=False
    if code==7:
        c['nord']=True
        c['est']=True
        c['sud']=True
        c['ouest']=False

    if code==8:
        c['nord']=False
        c['est']=False
        c['sud']=False
        c['ouest']=True
    if code==9:
        c['nord']=True
        c['est']=False
        c['sud']=False
        c['ouest']=True
    if code==10:
        c['nord']=False
        c['est']=True
        c['sud']=False
        c['ouest']=True
    if code==11:
        c['nord']=True
        c['est']=True
        c['sud']=False
        c['ouest']=True
    if code==12:
        c['nord']=False
        c['est']=False
        c['sud']=True
        c['ouest']=True
    if code==13:
        c['nord']=True
        c['est']=False
        c['sud']=True
        c['ouest']=True
    if code==14:
        c['nord']=False
        c['est']=True
        c['sud']=True
        c['ouest']=True
    if code==15:
        c['nord']=True
        c['est']=True
        c['sud']=True
        c['ouest']=True





def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """

    res=listeCartes[coderMurs(c)]
    return res



def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['nord']:
        if not carte2['sud']:
            res=True
    return res

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['sud']:
        if not carte2['nord']:
            res=True
    return res

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['ouest']:
        if not carte2['est']:
            res=True
    return res

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['est']:
        if not carte2['ouest']:
            res=True
    return res
