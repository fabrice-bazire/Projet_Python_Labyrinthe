from carte import *
tresorDebut=13
nbTresors=34
liste=[]
liste_tresor = []
i=0
liste_tresor.append(tresorDebut)
while len(liste_tresor)<nbTresors:
    liste_tresor.append(tresorDebut)
    tresorDebut+=1
while len(liste)<16:
    liste.append(Carte(False, True, False, True))
while len(liste)<28:
    liste.append(Carte(True,True,False,False))
while len(liste)<34:
    liste.append(Carte(False,False,False,True))
random.shuffle(liste)
for element in liste:
    tourneAleatoire(element)
for tresor in liste_tresor:
    mettreTresor(liste[i],tresor)
    i+=1
random.shuffle(liste)
print(len(liste_tresor))
print(liste_tresor)
print(liste)
