#### Code de BARAR Bilal 
#### Permet de calculer le nombre de possibilité de mot de passe 


##### A faire 
## Calculer le nombre de possibilité de mot de passe 
## Calculer la puissance de notre CPU/ GPU 
## Faire une opération qui permet d'avoir le temps final 



#########################
############# Import 
#######################

import locale



############################
###########Fonction 
##########################

## Permet de calculer le nombre de possibilité de mot de passe 
def calculer_possibilites_mot_de_passe(longueur, nbchar):

    nombre_possibilites = 0 

    for i in range(longueur): 
        nombre_possibilites = nombre_possibilites+ nbchar ** longueur
    
    return nombre_possibilites


def afficher_nombre_par_trois(n):
    nombre_formatte = f'{n:,}'.replace(',', ' ')
    return nombre_formatte


def temps_de_calcul_sec(vitesse, nombreposs): 

    return nombreposs/vitesse



##################
#### Code 
##################@



print("Nombre de possibilité : " , afficher_nombre_par_trois(calculer_possibilites_mot_de_passe(20,62)))



