from iceWalker_logique import *

dico_murs = labyrinthe("labyrinthes/laby0.csv")
dico_personnages = personnages("labyrinthes/personnages0.csv")
largeur, hauteur = dimensions("labyrinthes/dimensions0.csv")
estGagnant = False
while not estGagnant:
    direction = input("Donner une direction pour déplacer le phoque(E|S|O|N) : ")
    estDeplacement = True
    while estDeplacement:
        estDeplacement = mouvement(dico_personnages, dico_murs, direction, (largeur, hauteur))
        print(dico_personnages['0'])
    estGagnant = gagne(dico_personnages)
print("Le phoque a mangé le poisson!!!")    