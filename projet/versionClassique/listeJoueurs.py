# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    cpt = 1
    les_joueurs = {}
    for joueur in nomsJoueurs :
        les_joueurs[cpt] = Joueur(joueur) #cpt est le numéro du joueur que l'on ajoute à la liste
        cpt += 1
    return [les_joueurs, 0] #ici 1 represente le numéro du joueur courant
    

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs une liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs[0][len(joueurs[0])] = joueur

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs une liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs[1] = random.randint(0,len(joueurs[0]) - 1)

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    #distribuer les trésors : parcourir le nbtresors et attribuer à un joueur aleatoirement si ce joueur a moins de nbtresormax 
    les_tresors = []
    nb_tresor_par_joueur = 0
    for i in range(nbTresors) :
        les_tresors.append(i+1)
    random.shuffle(les_tresors)
    nb_joueurs = len(joueurs[0])
    if nbTresorMax == 0 :
        while len(les_tresors) >= nb_joueurs :
            for i in range(nb_joueurs) :
                joueurs[0][i+1][1].append(les_tresors[0])
                les_tresors.pop(0)
    else : 
        while len(les_tresors) >= nb_joueurs and nb_tresor_par_joueur < nbTresorMax :
            for i in range(nb_joueurs) :
                joueurs[0][i+1][1].append(les_tresors[0])
                les_tresors.pop(0)
            nb_tresor_par_joueur += 1


def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    joueurs[1] = ((joueurs[1]+1) % len(joueurs[0]))

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs[0])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    return joueurs[0][joueurs[1]+1]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if getJoueurCourant(joueurs)[0] != [] :
        tresorTrouve(getJoueurCourant(joueurs))

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return len(joueurs[0][numJoueur][1])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs[1]+1

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return getJoueurCourant(joueurs)[0]

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return joueurs[0][numJoueur][0]

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return joueurs[0][numJoueur][1][0] #je suppose que le tresor courant est le premier trésor de la liste 

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    if getJoueurCourant(joueurs)[1] != [] :
        return getJoueurCourant(joueurs)[1][0]
    else : 
        return 0

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    return getJoueurCourant(joueurs)[1] == []