# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 45
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    nv_plateau = Plateau(len(nomsJoueurs),nbTresors)
    affichePlateau(nv_plateau[0])
    labyrinthe = {}

    labyrinthe['plateau']=nv_plateau[0]
    labyrinthe['liste_joueurs']=ListeJoueurs(nomsJoueurs)
    distribuerTresors(labyrinthe['liste_joueurs'],nbTresors, nbTresorsMax)
    labyrinthe['carte_amovible']=nv_plateau[1]
    labyrinthe['phase']=1
    labyrinthe['dernier_coup']=(None,None)

    return labyrinthe

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe['plateau']

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(labyrinthe['liste_joueurs'])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe['liste_joueurs'])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe['liste_joueurs'])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """
    return labyrinthe['phase']


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    if labyrinthe['phase'] == 2 :  
        labyrinthe['phase'] = 1
    if labyrinthe['phase'] == 1 :  
        labyrinthe['phase'] = 2


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    res = 0
    for lig in range(getNbLignes(labyrinthe['plateau'])) :
        for col in range(getNbColonnes(labyrinthe['plateau'])):
            if labyrinthe['plateau'][lig][col]['tresor'] != 0 :
                res += 1
    return res

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py
    """
    return (labyrinthe['liste_joueurs'])


def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe.
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    tresor = getTresor(labyrinthe['plateau'][lin][col])
    if tresor == numTresor:
        labyrinthe['plateau'][lin][col]['tresor'] = 0

def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    joueur = getJoueurCourant(labyrinthe['liste_joueurs'])
    labyrinthe['plateau'][lin][col]['pions'].pop(joueur)

def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    joueur = getJoueurCourant(labyrinthe['liste_joueurs'])
    labyrinthe['plateau'][lin][col]['pions'].append(joueur)

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer
    """
    return labyrinthe['carte_amovible']

def coupInterdit(labyrinthe,direction,rangee):
    """
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    def inv_direction(direction):
        if direction=='N':
            direction='S'
        if direction=='E':
            direction='O'
        if direction=='O':
            direction='E'
        if direction=='S':
            direction='N'
    coup=False
    if labyrinthe['dernier_coup']==(inv_direction(direction),rangee): 
        coup=True
    return coup

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passée
    en paramètre n. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    if not coupInterdit(labyrinthe,direction,rangee):
        labyrinthe['dernier_coup']=(direction,rangee)
        if direction=='N':
            labyrinthe['carte_amovible'] = decalageColonneEnHaut(plateau,rangee,labyrinthe['carte_amovible'])
        elif direction=='S':
            labyrinthe['carte_amovible'] = decalageColonneEnBas(plateau,rangee,labyrinthe['carte_amovible'])
        elif direction=='O':
            labyrinthe['carte_amovible'] = decalageLigneAGauche(plateau,rangee,labyrinthe['carte_amovible'])
        elif direction=='E':
            labyrinthe['carte_amovible'] = decalageLigneADroite(plateau,rangee,labyrinthe['carte_amovible'])

def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyrinthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    if sens == 'H':
        tournerHoraire(labyrinthe['carte_amovible'])
    if sens == 'A':
        tournerAntiHoraire(labyrinthe['carte_amovible'])

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyrinthe: le labyrinthe considéré
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(labyrinthe['liste_joueurs'])

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyrinthe: le labyrinthe considéré
    resultat: les coordonnées du trésor à chercher ou None si celui-ci
              n'est pas sur le plateau
    """
    tresor = getTresorCourant(labyrinthe)
    if labyrinthe['carte_amovible']['tresor'] ==  tresor: 
        return None
    for lig in range(getNbLignes(labyrinthe['plateau'])) :
        for col in range(getNbColonnes(labyrinthe['plateau'])):
            if labyrinthe['plateau'][lig][col]['tresor'] == tresor : 
                return (lig, col) 
    return None


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyrinthe: le labyrinthe considéré
    resultat: les coordonnées du joueur courant ou None si celui-ci
              n'est pas sur le plateau
    """
    joueur = getNumJoueurCourant(labyrinthe['liste_joueurs'])
    for lig in range(getNbLignes(labyrinthe['plateau'])) :
        for col in range(getNbColonnes(labyrinthe['plateau'])):
            if labyrinthe['plateau'][lig][col]['pions'] == joueur : 
                return (lig, col) 
    return None


def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    direction=(None,None)
    res=4
    if action=='T':
        tournerHoraire(labyrinthe['carte_amovible'])
        res=0
    if rangee in [1,3,5]:
        if action in ['N','S','E','O']:
            if not coupInterdit(labyrinthe,direction,rangee):
                jouerCarte(labyrinthe,direction,rangee)
                res=1
            else:
                res=2
    if isinstance(action,int) and isinstance(rangee,int):
        if action > 0 and rangee > 0 :  
            res=3
    return res


def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    if accessibleDist(getCoordonneesJoueurCourant(labyrinthe),ligA,colA) == [] : 
        return None
    else : 
        return accessibleDist(getCoordonneesJoueurCourant(labyrinthe),ligA,colA)

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    # Vérifie si trésor trouvé
        # Si oui : attribuer nouveau trésor courant
    # Retour phase 1
    # changerJoueurCourant()
    if joueurCourantAFini(labyrinthe['liste_joueurs']):
        return 2
    else : 
        if getCoordonneesJoueurCourant(labyrinthe) == getCoordonneesTresorCourant(labyrinthe) :
            res=1
            tresorTrouve(getJoueurCourant(labyrinthe['liste_joueurs']))
            if prochainTresor(getJoueurCourant(labyrinthe['liste_joueurs'])) == None : 
                res = 2
            changerPhase(labyrinthe)
        else:
            res=0
            changerJoueurCourant(labyrinthe['liste_joueurs'])
    return res