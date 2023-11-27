#### Code de BARAR Bilal 
#### Permet de calculer le nombre de possibilité de mot de passe 


##### A faire 
## Calculer le nombre de possibilité de mot de passe 
## Calculer la puissance de notre CPU/ GPU 
## Faire une opération qui permet d'avoir le temps final 



#### Rappelles 
## possibilite symboles de 0 à 9, A Z, a z 
## 52 Symbole A Z, a z 
## 10 symbole : 0 à 9
## 90 symboles : 0 à 9, A à Z, a à z et  ! #$*% ? &[|]@^µ§ :/ ;.,<>°²³
## 36 : Lettre min + Chiffre


#########################
############# Import 
#######################

import locale



############################
###########Fonction 
##########################

## Permet de calculer le nombre de possibilité de mot de passe en prenant en compte toutes les possibilité 
def calculer_possibilites_mot_de_passe_all(longueur, nbchar):

    nombre_possibilites = 0 

    for i in range(longueur): 
        nombre_possibilites = nombre_possibilites+ nbchar ** longueur
    
    return nombre_possibilites

# Ici on connait la longueur ??
def calculer_possibilites_mot_de_passe_fixe(longueur, nbchar):
    
    return nbchar ** longueur


def afficher_nombre_par_trois(n):
    nombre_formatte = f'{n:,}'.replace(',', ' ')
    return nombre_formatte


def tpm_RTX4090_Hscat_22000(nombreposs): 

    return nombreposs/(66000)
    
    ## Au cas ou un M2 c'est juste 2936.72 H/s


def sec_to_days(dec):
    return dec/86400

def days_to_years(days):
    return days/365


##################
#### Code 
##################

possibilite = 10
longueur = 10


print("\n")
print("Nombre de possibilité pour toute combinaison : " , afficher_nombre_par_trois(calculer_possibilites_mot_de_passe_all(longueur,possibilite)))
print("le temps en seconde en fonction de la vitesse pour la RTX 4090 en mode 22000 est : " , tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_all(longueur,possibilite))," secondes" )
print("Ce temps en jours : " , sec_to_days(tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_all(longueur,possibilite))), " jours")
print("Ce temps en année : " , days_to_years(sec_to_days(tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_all(longueur,possibilite)))), " années",  "\n" )


print("Nombre de possibilité pour une longueur connue ", afficher_nombre_par_trois(calculer_possibilites_mot_de_passe_fixe(longueur,possibilite)))
print("le temps en seconde en fonction de la vitesse pour la RTX 4090 en mode 22000 est : " , tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_fixe(longueur,possibilite)), " secondes")
print("Ce temps en jours : " , sec_to_days(tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_fixe(longueur,possibilite))), " jours")
print("Ce temps en année : " , days_to_years(sec_to_days(tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_fixe(longueur,possibilite)))), " années",  "\n" )

print("Facteur de rapidité entre longueur fixe et all :  ", tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_all(longueur,possibilite))/tpm_RTX4090_Hscat_22000(calculer_possibilites_mot_de_passe_fixe(longueur,possibilite)) )


cdcdcd