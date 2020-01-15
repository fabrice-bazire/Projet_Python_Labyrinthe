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


class Carte :

	def __init__(self, nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    self.nord = nord
    self.est = est
    self.sud = sud
    self.ouest = ouest
    self.tresor = tresor
    self.pions = pions


    def estValide(self):
        """
        retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
        paramètre: c une carte
        """
        cpt=0
        if (self.nord):
            cpt+=1
        if (self.sud):
            cpt+=1
        if (self.est):
            cpt+=1
        if (self.ouest):
            cpt+=1
        if cpt<3:
            res=True
        else:
            res=False
        return res



    def murNord(self):
        """print(len(c['pions']))if c['nord']:
        retourne un booléen indiquant si la carte possède un mur au nord
        paramètre: c une carte
        """
        return self.nord


    def murSud(self):
        """
        retourne un booléen indiquant si la carte possède un mur au sud
        paramètre: c une carte( nord, est, sud, ouest, tresor=0, pions=[]
        """
        return self.sud

    def murEst(self):
        """
        retourne un booléen indiquant si la carte possède un mur à l'est
        paramètre: c une carte
        """
        return self.est

    def murOuest(self):
        """
        retourne un booléen indiquant si la carte possède un mur à l'ouest
        paramètre: c une carte
        """
        return self.ouest

    def getListePions(self):
        """
        retourne la liste des pions se trouvant sur la carte
        paramètre: c une carte
        """
        return self.pions



    def setListePions(self,listePions):
        """
        place la liste des pions passées en paramètre sur la carte
        paramètres: c: est une carte
                    listePions: la liste des pions à poser
        Cette fonction ne retourne rien mais modifie la carte
        """
        self.pions=listePions

    def getNbPions(self):
        """print(len(c['pions']))
        retourne le nombre de pions se trouvant sur la carte
        paramètre: c une carte
        """
        if len(self.pions)>0:
            res=len(self.pions)
        else:
            res=0
        return res

    def possedePion(self,pion):
        """
        retourne un booléen indiquant si la carte possède le pion passé en paramètre
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        """
        res= False
        for pions in self.pions:
            if pion == pions:
                res=True
        return res

    def getTresor(self):
        """( nord, est, sud, ouest, tresor=0, pions=[]
        retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
        paramètre: c une carte
        """
        return self.tresor

    def prendreTresor(self):
        """if c['nord']:
        enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
        paramètre: c une carte
        résultat l'entier représentant le trésor qui était sur la carte
        """

        ancient_tresor=self.getTresor()
        self.tresor=0
        return ancient_tresor


    def mettreTresor(self,tresor):
        """
        met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
        paramètres: c une carte
                    tresor un entier positif
        résultat l'entier représentant le trésor qui était sur la carte
        """
        res= self.prendreTresor()
        self.tresor=tresor
        return res

    def prendrePion(self,pion):
        """
        enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        for indice in range(len(self.pions)):
            if self.pions[indice]==pion:
                self.pions.pop(indice)

    def poserPion(self, pion):
        """
        pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        if not self.possedePion(pion):
            self.pions.append(pion)

    def tournerHoraire(self):
        """
        fait tourner la carte dans le sens horaire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien
        """
        Sud=self.sud
        Est=self.est
        Ouest=self.ouest
        Nord=self.nord
        self.nord=Ouest
        self.est=Nord
        self.sud=Est
        self.ouest=Sud

    def tournerAntiHoraire(self):
        """
        fait tourner la carte dans le sens anti-horaire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien
        """
        Sud=self.sud
        Est=self.est
        Ouest=self.ouest
        Nord=self.nord
        self.nord=Est
        self.est=Sud
        self.sud=Ouest
        self.ouest=Nord



    def tourneAleatoire(self):
        """
        faire tourner la carte d'un nombre de tours aléatoire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien
        """
        nb_tour=random.randint(1,3)
        for i in range(nb_tour):
            self.tournerHoraire()

    def coderMurs(self):
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
        if self.nord:
            res+=1
        if self.est:
            res+=2
        if self.sud:
            res+=4
        if self.ouest:
            res+=8
        return res



    def decoderMurs(self,code):
        """
        positionne les murs d'une carte en fonction du code décrit précédemment
        paramètres c une carte
                code un entier codant les murs d'une carte
        Cette fonction modifie la carte mais ne retourne rien
        """
        if code==0:
            self.nord=False
            self.est=False
            self.sud=False
            self.ouest=False
        if code==1:
            self.nord=True
            self.est=False
            self.sud=False
            self.ouest=False
        if code==2:
            self.nord=False
            self.est=True
            self.sud=False
            self.ouest=False
        if code==3:
            self.nord=True
            self.est=True
            self.sud=False
            self.ouest=False
        if code==4:
            self.nord=False
            self.est=False
            self.sud=True
            self.ouest=False
        if code==5:
            self.nord=True
            self.est=False
            self.sud=True
            self.ouest=False
        if code==6:
            self.nord=False
            self.est=True
            self.sud=True
            self.ouest=False
        if code==7:
            self.nord=True
            self.est=True
            self.sud=True
            self.ouest=False

        if code==8:
            self.nord=False
            self.est=False
            self.sud=False
            self.ouest=True
        if code==9:
            self.nord=True
            self.est=False
            self.sud=False
            self.ouest=True
        if code==10:
            self.nord=False
            self.est=True
            self.sud=False
            self.ouest=True
        if code==11:
            self.nord=True
            self.est=True
            self.sud=False
            self.ouest=True
        if code==12:
            self.nord=False
            self.est=False
            self.sud=True
            self.ouest=True
        if code==13:
            self.nord=True
            self.est=False
            self.sud=True
            self.ouest=True
        if code==14:
            self.nord=False
            self.est=True
            self.sud=True
            self.ouest=True
        if code==15:
            self.nord=True
            self.est=True
            self.sud=True
            self.ouest=True





    def toChar(self):
        """
        fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
        paramètres c une carte
        """

        res=listeCartes[self.coderMurs()]
        return res



    def passageNord(self,carte2):
        """
        suppose que la carte2 est placée au nord de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le nord
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self.nord:
            if not carte2.sud:
                res=True
        return res

    def passageSud(self,carte2):
        """
        suppose que la carte2 est placée au sud de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le sud
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self.sud:
            if not carte2.nord:
                res=True
        return res

    def passageOuest(self,carte2):
        """
        suppose que la carte2 est placée à l'ouest de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'ouest
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self.ouest:
            if not carte2.est:
                res=True
        return res

    def passageEst(self,carte2):
        """
        suppose que la carte2 est placée à l'est de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'est
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self.est:
            if not carte2.ouest:
                res=True
        return res
