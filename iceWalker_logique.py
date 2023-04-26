import csv

def labyrinthe(fichier: str) -> list:
    '''
    L'objet renvoyé par la fonction labyrinthe
    {
        (0, 1): ['S'], 
        (0, 5): ['E'], 
        (0, 9): ['S'], 
        (2, 5): ['S'], 
        (2, 6): ['S'], 
        (3, 4): ['S', 'E'], 
        (3, 6): ['E'], 
        (4, 4): ['E'], 
        (4, 6): ['E'], 
        (9, 6): ['E']
    }    
    '''
    dico_murs = {}
    with open(fichier, 'r') as donnees:
        murs = csv.reader(donnees)        
        '''
        Les données référencées par la variable murs est de type csv.reader.
        Chaque ligne du fichier csv est représentée par une liste.
        
        ['0', '1', 'S'] 
        ['0', '5', 'E'] 
        ['0', '9', 'S'] 
        ['2', '5', 'S']
        ['2', '6', 'S'] 
        ['3', '4', 'S'] 
        ['3', '4', 'E'] 
        ['3', '6', 'E'] 
        ['4', '4', 'E'] 
        ['4', '6', 'E']
        ['9', '6', 'E']
        
        '''
        for mur in murs:      
           if (int(mur[0]), int(mur[1])) in dico_murs.keys():
                dico_murs[(int(mur[0]), int(mur[1]))].append(mur[2])
           else:
               dico_murs[(int(mur[0]), int(mur[1]))] = [mur[2]]
    return dico_murs

def personnages(fichier: str) -> list:
    '''
    Le contenu du fichier csv(str)
    3,4,0
    0,9,1
    
    L'objet renvoyé par la fonction personnages
    {
        '0': (3, 4), 
        '1': (0, 9)
    }
    '''
    dico_personnages = {}
    with open(fichier, 'r') as donnees:
        personnages = csv.reader(donnees, delimiter=',')
        for personnage in personnages:
           dico_personnages[personnage[2]] = (int(personnage[0]), int(personnage[1]))
    return dico_personnages

def dimensions(fichier_dimensions):
    with open(fichier_dimensions, 'r') as donnees:
        largueur_hauteur = csv.reader(donnees, delimiter=',')
        for dim in largueur_hauteur:
            dimensions_grille = dim
    return (int(dimensions_grille[0]), int(dimensions_grille[1]))

def mouvement(dico_personnages: dict, dico_murs: dict, direction: str, dimension: tuple) -> bool:
    '''
    Cette fonction permet de mettre renvoyer True si le phoque peut se déplacer d'une case dans la position choisie,
    False dans la cas contraire.
    Si le phoque peut se déplacer, sa position est mise à jour : dico_personnages
    '''
    if direction == 'S' and dico_personnages['0'][0] < dimension[0] - 1:
        if dico_personnages['0'] not in dico_murs.keys() or 'S' not in dico_murs[dico_personnages['0']] :
            dico_personnages['0'] = (dico_personnages['0'][0] + 1, dico_personnages['0'][1])
            return True
    elif direction == 'E' and dico_personnages['0'][1] < dimension[1] - 1:
        if dico_personnages['0'] not in dico_murs.keys() or 'E' not in dico_murs[dico_personnages['0']] :
            dico_personnages['0'] = (dico_personnages['0'][0] , dico_personnages['0'][1] + 1)
            return True
    elif direction == 'N' and dico_personnages['0'][0] > 0:
        case_au_dessus = dico_personnages['0'][0] - 1, dico_personnages['0'][1]
        if case_au_dessus not in dico_murs.keys() or 'S' not in dico_murs[case_au_dessus] :
            dico_personnages['0'] = (dico_personnages['0'][0] - 1 , dico_personnages['0'][1])
            return True
    elif direction == 'O' and dico_personnages['0'][1] > 0:
        case_a_droite = dico_personnages['0'][0], dico_personnages['0'][1] - 1
        if case_a_droite not in dico_murs.keys() or 'E' not in dico_murs[case_a_droite] :
            dico_personnages['0'] = (dico_personnages['0'][0] , dico_personnages['0'][1] - 1)
            return True
    return False

def gagne(dico_personnages):
    if dico_personnages['0'] == dico_personnages['1']:
        return True
    return False

