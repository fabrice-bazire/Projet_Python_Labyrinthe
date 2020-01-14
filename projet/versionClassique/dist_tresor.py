for tresor in range(1, nbTresors, 1) :
        joueur_random = random.randint(0,getNbJoueurs(joueurs)-1)
        if nbTresorMax != 0 :
            if len(joueurs[0][joueur_random][1]) < nbTresorMax :
                ajouterTresor(joueurs[0][joueur_random], tresor)
        else : 
                if len(joueurs[0][joueur_random][1]) < nbTresor // getNbJoueurs(joueurs) :                    
                    joueurs[0][joueur_random][1].append(tresor)