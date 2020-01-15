# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueurOO import *

class ListeJoueurs : 

    def __init__(self,nomsJoueurs):
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
        self.les_joueurs = les_joueurs
        self.joueur_courant = 0
        

    def ajouterJoueur(self, joueur):
        """
        ajoute un nouveau joueur à la fin de la liste
        paramètres: joueurs une liste de joueurs
                    joueur le joueur à ajouter
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        self.les_joueurs[len(self.les_joueurs)] = joueur

    def initAleatoireJoueurCourant(self):
        """
        tire au sort le joueur courant
        paramètre: joueurs une liste de joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        self.joueur_courant = random.randint(0,len(self.les_joueurs) - 1)

    def distribuerTresors(self,nbTresors=24, nbTresorMax=0):
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
            while len(les_tresors) % nb_joueurs == O:
                for i in range(nb_joueurs) :
                    self.les_joueurs[i+1][1].append(les_tresors[0])
                    les_tresors.pop(0)
        else : 
            while len(les_tresors) % nb_joueurs == 0 and nb_tresor_par_joueur < nbTresorMax :
                for i in range(nb_joueurs) :
                    self.les_joueurs[i+1][1].append(les_tresors[0])
                    les_tresors.pop(0)
                nb_tresor_par_joueur += 1


    def changerJoueurCourant(self):
        """
        passe au joueur suivant (change le joueur courant donc)
        paramètres: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """   
        self.joueur_courant = ((self.joueur_courant+1) % len(self.les_joueurs))

    def getNbJoueurs(self):
        """
        retourne le nombre de joueurs participant à la partie
        paramètre: joueurs la liste des joueurs
        résultat: le nombre de joueurs de la partie
        """
        return len(self.les_joueurs)

    def getJoueurCourant(self):
        """
        retourne le joueur courant
        paramètre: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        return self.les_joueurs[self.joueur_courant+1]

    def joueurCourantTrouveTresor(self):
        """
        Met à jour le joueur courant lorsqu'il a trouvé un trésor
        c-à-d enlève le trésor de sa liste de trésors à trouver
        paramètre: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        if self.getJoueurCourant()[0] != [] :
            self.getJoueurCourant().tresorTrouve()

    def nbTresorsRestantsJoueur(self,numJoueur):
        """
        retourne le nombre de trésors restant pour le joueur dont le numéro 
        est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur
        résultat: le nombre de trésors que joueur numJoueur doit encore trouver
        """
        return len(self.les_joueurs[numJoueur][1])

    def numJoueurCourant(self):
        """
        retourne le numéro du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le numéro du joueur courant
        """
        return self.joueur_courant+1

    def nomJoueurCourant(self):
        """
        retourne le nom du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le nom du joueur courant
        """
        return self.getJoueurCourant().nom

    def nomJoueur(self,numJoueur):
        """
        retourne le nom du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le nom du joueur numJoueur
        """
        return self.les_joueurs[numJoueur].nom

    def prochainTresorJoueur(self,numJoueur):
        """
        retourne le trésor courant du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le prochain trésor du joueur numJoueur (un entier)
        """
        return self.les_joueurs[numJoueur].tresors[0] #je suppose que le tresor courant est le premier trésor de la liste 

    def tresorCourant(self):
        """
        retourne le trésor courant du joueur courant
        paramètre: joueurs la liste des joueurs 
        résultat: le prochain trésor du joueur courant (un entier)
        """
        return self.getJoueurCourant().tresors[0]

    def joueurCourantAFini(self):
        """
        indique si le joueur courant a gagné
        paramètre: joueurs la liste des joueurs 
        résultat: un booleen indiquant si le joueur courant a fini
        """
        return self.getJoueurCourant().tresors == []