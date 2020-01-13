from matrice import *

matrice = Matrice(7,7,5)

def test_Decalage_droite(matrice):
	numLig = 4

	decalageLigneAGauche(matrice, numLig, nouvelleValeur=0)

	res = "Fonctionnement correct"

	if getVal(matrice,4,7) == 0:
		return res
	else:
		res = "Ne fonctionne pas !"
		return res

test_Decalage_droite(matrice)