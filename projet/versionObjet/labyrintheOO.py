# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueursOO import *
from plateauOO import *

class Labyrinthe : 

    def __init__(self,nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
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

        self.plateau=nv_plateau[0]
        self.liste_joueurs=ListeJoueurs(nomsJoueurs)
        self.carte_amovible=nv_plateau[1]
        self.phase=1
        self.dernier_coup=(None,None)

    def getPlateau(self):
        """
        retourne la matrice représentant le plateau de jeu
        paramètre: labyrinthe le labyrinthe considéré
        résultat: la matrice représentant le plateau de ce labyrinthe
        """
        return self.plateau

    def getNbParticipants(self):
        """
        retourne le nombre de joueurs engagés dans la partie
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le nombre de joueurs de la partie
        """
        return self.liste_joueurs.getNbJoueurs()

    def getNomJoueurCourant(self):
        """
        retourne le nom du joueur courant
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le nom du joueurs courant
        """
        return self.liste_joueurs.nomJoueurCourant()

    def getNumJoueurCourant(self):
        """
        retourne le numero du joueur courant
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le numero du joueurs courant
        """
        return self.liste_joueurs.numJoueurCourant()

    def getPhase(self):
        """
        retourne la phase du jeu courante
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le numéro de la phase de jeu courante
        """
        return self.phase


    def changerPhase(self):
        """
        change de phase de jeu en passant la suivante
        paramètre: labyrinthe le labyrinthe considéré
        la fonction ne retourne rien mais modifie le labyrinthe
        """
        self.phase=2   #peut etre plutot +1 avec un modulo à voir


    def getNbTresors(self):
        """
        retourne le nombre de trésors qu'il reste sur le labyrinthe
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le nombre de trésors sur le plateau
        """
        res = 0
        for lig in range(self.plateau.getNbLignes()) :
            for col in range(self.plateau.getNbColonnes()):
                if self.plateau[lig][col].tresor != 0 :
                    res += 1
        return res

    def getListeJoueurs(self):
        """
        retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
        paramètre: labyrinthe le labyrinthe considéré
        résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py
        """
        return self.liste_joueurs


    def enleverTresor(self,lin,col,numTresor):
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
        tresor = get.plateau[lin][col].getTresor()
        if tresor == numTresor:
            self.plateau[lin][col].tresor = 0

    def prendreJoueurCourant(self,lin,col):
        """
        enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
        si le joueur ne s'y trouve pas la fonction ne fait rien
        paramètres: labyrinthe: le labyrinthe considéré
                    lig: la ligne où se trouve la carte
                    col: la colonne où se trouve la carte
        la fonction ne retourne rien mais modifie le labyrinthe
        """
        joueur = self.liste_joueurs.getJoueurCourant()
        self.plateau[lin][col].pions.pop(joueur)

    def poserJoueurCourant(self,lin,col):
        """
        pose le joueur courant sur la case lin,col du plateau
        paramètres: labyrinthe: le labyrinthe considéré
                    lig: la ligne où se trouve la carte
                    col: la colonne où se trouve la carte
        la fonction ne retourne rien mais modifie le labyrinthe
        """
        joueur = self.liste_joueurs.getJoueurCourant()
        self.plateau[lin][col].pions.append(joueur)

    def getCarteAJouer(self):
        """
        donne la carte à jouer
        paramètre: labyrinthe: le labyrinthe considéré
        résultat: la carte à jouer
        """
        return self.carte_amovible

    def coupInterdit(self,direction,rangee):
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
        if rangee % 2 == 0 or self.dernier_coup==(inv_direction(direction),rangee): 
            coup=True
        return coup

    def jouerCarte(self,direction,rangee):
        """
        fonction qui joue la carte amovible dans la direction et sur la rangée passées
        en paramètres. Cette fonction
        - met à jour le plateau du labyrinthe
        - met à jour la carte à jouer
        - met à jour la nouvelle direction interdite
        paramètres: labyrinthe: le labyrinthe considéré
                    direction: un caractère qui indique la direction choisie ('N','S','E','O')
                    rangee: le numéro de la ligne ou de la colonne choisie
        Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
        """
        if not self.coupInterdit(direction,rangee):
            self.dernier_coup=[direction,rangee]
            if direction='N':
                self.plateau.decalageColonneEnHaut(rangee,self.carte_amovible)
                self.carte_amovible=self.plateau.getVal(0,rangee)
            if direction='S':
                self.plateau.decalageColonneEnBas(rangee,self.carte_amovible)
                self.carte_amovible=self.plateau.getVal(0,rangee)
            if direction='E':
                self.plateau.decalageLigneAGauche(rangee,self.carte_amovible)
                self.carte_amovible=self.plateau.getVal(rangee,0)
            if direction='O':
                self.plateau.decalageLigneADroite(rangee, self.carte_amovible)
                self.carte_amovible=self.plateau.getVal(rangee,0)

    def tournerCarte(self,sens='H'):
        """
        tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
        paramètres: labyrinthe: le labyrinthe considéré
                    sens: un caractère indiquant le sens dans lequel tourner la carte
        Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
        """
        if sens = 'H':
            self.carte_amovible.tournerHoraire()
        if sens = 'A':
            self.carte_amovible.tournerAntiHoraire()

    def getTresorCourant(self):
        """
        retourne le numéro du trésor que doit cherche le joueur courant
        paramètre: labyrinthe: le labyrinthe considéré
        resultat: le numéro du trésor recherché par le joueur courant
        """
        return self.liste_joueurs.tresorCourant()

    def getCoordonneesTresorCourant(self):
        """
        donne les coordonnées du trésor que le joueur courant doit trouver
        paramètre: labyrinthe: le labyrinthe considéré
        resultat: les coordonnées du trésor à chercher ou None si celui-ci
                n'est pas sur le plateau
        """
        tresor = self.getTresorCourant()
        if self.carte_amovible.tresor ==  tresor: 
            return None
        for lig in range(self.plateau.getNbLignes()) :
            for col in range(self.plateau.getNbColonnes()):
                if self.plateau[lig][col].tresor == tresor : 
                    return (lig, col) 
        return None


    def getCoordonneesJoueurCourant(self):
        """
        donne les coordonnées du joueur courant sur le plateau
        paramètre: labyrinthe: le labyrinthe considéré
        resultat: les coordonnées du joueur courant ou None si celui-ci
                n'est pas sur le plateau
        """
        joueur = self.liste_joueurs.getNumJoueurCourant()
        for lig in range(self.plateau.getNbLignes()) :
            for col in range(self.plateau.getNbColonnes()):
                if self.plateau[lig][col].pions == joueur : 
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
    #labyrinthe['liste_joueurs']
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
        else : #rajout
            res = 2  #rajout
    else : #rajout
        res = 2#rajout
    if isinstance(action,int) and isinstance(rangee,int):
        if action > 0 and rangee > 0 :  #rajout
            res=3
    return res
     #SaisirOrdre retourne (NSEO,135) (Nord Sud Est Ouest, 1 3 5)


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

    if getCoordonneesJoueurCourant(labyrinthe) == getCoordonneesTresorCourant(labyrinthe) :
        res=1
        tresorTrouve(labyrinthe['liste_joueurs'])
        prochainTresor(labyrinthe['liste_joueurs'])
        changerPhase(labyrinthe)
    else:
        res=0
        changerJoueurCourant(labyrinthe['liste_joueurs'])
    return res