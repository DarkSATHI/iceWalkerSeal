from js import document
from iceWalker_logique import labyrinthe, personnages, mouvement, gagne, dimensions
from PIL import Image
import base64
from io import BytesIO


def grille_iceWalker(nb_ligne: int = 10, nb_colonne: int = 10) -> None:
    '''
    Création d'un élément HTML table, par défaut un tableau de 10 lignes
    et 10 colonnes sera injecté dans la page index.html.    
    '''
    plateauJeu = document.getElementById("plateauJeu")
    table = document.createElement("table")
    table.id = "grille"
    for i in range(nb_ligne):
        tr = document.createElement("tr")
        tr.id = f'ligne{i}'
        for j in range(nb_colonne):
            td = document.createElement("td")
            td.id = f'cellule{i}_{j}'
            tr.appendChild(td)
        table.appendChild(tr)
    plateauJeu.appendChild(table)

def mur_enceinte():
    '''
    On dessine le mur d'enceinte du labyrinthe.
    '''
    table = document.getElementsByTagName("table")[0]
    table.style.border = 'solid'
    table.style.borderWidth = '0.5vw'
    table.style.borderColor = 'rgb(97, 97, 97)'

def dessiner_personnage(qui, image_base64, dico_personnages, tuile = True):
    element =  document.getElementById(f'cellule{dico_personnages[qui][0]}_{dico_personnages[qui][1]}')
    element.style.backgroundImage = f'url({image_base64})'
    if tuile:
        element.style.backgroundImage =  element.style.backgroundImage + ',url(pictures/tuile.png)'


def dessin_murs(dico_murs):
    for coordonnees, orientation in dico_murs.items():
        element =  document.getElementById(f'cellule{coordonnees[0]}_{coordonnees[1]}')
        if 'E' in orientation:
            element.style.borderRightWidth = '0.2vw'
            element.style.borderRightColor = 'rgb(97, 97, 97)'          
        if 'S' in orientation:    
            element.style.borderBottomWidth = '0.2vw'
            element.style.borderBottomColor = 'rgb(97, 97, 97)' 

def dessin_base64(planche: str, boite: tuple):
    planche_personnages = Image.open(planche)
    hero = planche_personnages.crop(boite)
    fichier_image = BytesIO()
    hero.save(fichier_image, format="png")
    image_bytes = fichier_image.getvalue()
    return "data:image/png;base64," + base64.b64encode(image_bytes).decode('ascii')


