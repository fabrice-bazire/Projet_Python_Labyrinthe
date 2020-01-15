# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

class Joueur :
    def __init__(self, nom) :
        """
        creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
        paramètre: nom une chaine de caractères
        retourne le joueur ainsi créé
        """
        self.nom = nom
        self.tresors = []

    def ajouterTresor(self,tresor):
        """
        ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
        paramètres:
            joueur le joueur à modifier
            tresor un entier strictement positif
        la fonction ne retourne rien mais modifie le joueur
        """
        if tresor not in self.tresors:
            self.tresors.append(tresor)

    def prochainTresor(self):
        """
        retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
        paramètre:
            joueur le joueur
        résultat un entier représentant le trésor ou None
        """
        if self.tresors == []:
            return None
        else:
            return self.tresors[0]
            
    def tresorTrouve(self):
        """ 
        enleve le premier trésor à trouver car le joueur l'a trouvé
        paramètre:
            joueur le joueur
        la fonction ne retourne rien mais modifie le joueur
        """
        if self.tresors != []:
            self.tresors.pop(0)

    def getNbTresorsRestants(self):
        """
        retourne le nombre de trésors qui reste à trouver
        paramètre: joueur le joueur
        résultat: le nombre de trésors attribués au joueur
        """
        return len(self.tresors)

    def getNom(self):
        """
        retourne le nom du joueur
        paramètre: joueur le joueur
        résultat: le nom du joueur 
        """
        return self.nom