def attribuer_tresor(les_tresors_affectes, nbTresors) :
        tresor = random.randint(0,nbTresors)
        while tresor in les_tresors_affectes and tresor != 0 :
            if len(les_tresors_affectes) == nbTresors :
                tresor = 0
            else : 
                tresor = random.randint(0,nbTresors)
            les_tresors_affectes.add(tresor)
        return tresor
    les_tresors_affectes = set()
    plateau = Matrice(7,7)
    for ligne in range(7) : 
        for colonne in range(7):
            if ligne % 2 == 1 and colonne % 2 == 1 :
                tresor = attribuer_tresor(les_tresors_affectes, nbTresors)
                carte = Carte(bool(random.getrandbits(1)),bool(random.getrandbits(1)),bool(random.getrandbits(1)),bool(random.getrandbits(1)),tresor)
                setVal(plateau,ligne,colonne,carte)
    setVal(plateau,0,0,Carte(True, False, False, True))
    setVal(plateau,0,6,Carte(True, True, False, False))
    setVal(plateau,6,0,Carte(False, False, True, True))
    setVal(plateau,6,6,Carte(False, True, True, False))
    setVal(plateau, 0, 2, Carte(True, False, False, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 0, 4, Carte(True, False, False, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 2, 4, Carte(True, False, False, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 2, 0, Carte(False, False, False, True, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 2, 2, Carte(False, False, False, True, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 2, 4, Carte(False, False, False, True, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 2, 6, Carte(False, True, False, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 4, 6, Carte(False, True, False, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 4, 4, Carte(False, True, False, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 4, 2, Carte(False, False, True, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 6, 2, Carte(False, False, True, False, attribuer_tresor(les_tresors_affectes, 12)))
    setVal(plateau, 6, 4, Carte(False, False, True, False, attribuer_tresor(les_tresors_affectes, 12)))
    tresor_am = random.randint(0,nbTresors)
    while tresor in les_tresors_affectes and tresor != 0 :
                if len(les_tresors_affectes) == nbTresors :
                    tresor_am = 0
                else : 
                    tresor_am = random.randint(0,nbTresors)
    carte_amovible = Carte(bool(random.getrandbits(1)),bool(random.getrandbits(1)),bool(random.getrandbits(1)),bool(random.getrandbits(1)),tresor)
    plateau[0][0]['pions'].append(1)
    if nbJoueurs > 1 :
        plateau[0][6]['pions'].append(2)
    if nbJoueurs > 2 :
        plateau[6][0]['pions'].append(3)
    if nbJoueurs > 3 :
        plateau[6][6]['pions'].append(4)
    return (plateau, carte_amovible)