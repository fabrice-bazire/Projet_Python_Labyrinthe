for tresor in range(1, nbTresors, 1) :
        joueur_random = random.randint(1,getNbJoueurs(joueurs))
        if nbTresorMax != 0 :
            if getNbJoueurs(joueurs) == 2 :
                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]):
                    joueurs[0][joueur_random][1].append(tresor)
            if getNbJoueurs(joueurs) == 3 :
                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) :
                    
            if getNbJoueurs(joueurs) == 4 :
                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) and len(joueurs[0][0][1]) == len(joueurs[0][3][1]) :                    
                    joueurs[0][joueur_random][1].append(tresor)
        else : 
            if getNbJoueurs(joueurs) == 2 :
                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]):
                    joueurs[0][joueur_random][1].append(tresor)
            if getNbJoueurs(joueurs) == 3 :
                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) :
            if getNbJoueurs(joueurs) == 4 :
                if len(joueurs[0][joueur_random][1]) < nbTresorMax and len(joueurs[0][0][1]) == len(joueurs[0][1][1]) and len(joueurs[0][0][1]) == len(joueurs[0][2][1]) and len(joueurs[0][0][1]) == len(joueurs[0][3][1]) :                    
                    joueurs[0][joueur_random][1].append(tresor)