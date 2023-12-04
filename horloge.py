import time             # j'importe ma fonction time 

def am_pm():            #je définis ma fonction ampm AVANT pour le choix du mode d'affichage
    while True:         #boucle infinie
        type_horloge = input("Choisir le mode d'affichage de l'heure (AMPM/24H) : ").upper()    #je nomme ma variable type horloge avec un input
        if type_horloge in ['AMPM', '24H']:         
            return type_horloge             #renvoie a ma fonction
        else:
            print("Veuillez entrer une option valide (AMPM/24H).")      #si invalide print

def afficher_heure(heure_tuple, type_horloge):          #fonction pour l'affichage de mon heure
    while True:                 #boucle infinie
        heure = heure_tuple[0]          
        minute = heure_tuple[1]
        seconde = heure_tuple[2]

        seconde += 1
        if seconde > 59:
            seconde = 0
            minute += 1
        if minute > 59:
            minute = 0
            heure += 1
        if heure > 24:
            heure = 0

        time.sleep(1)               #écart de 1 seconde

        if type_horloge == 'AMPM':              # Converti en format 12 heures
            heure_affichage = heure % 12 if heure % 12 != 0 else 12     #mon heure s'affichera en multiple de 12. Si l'heure est divisible par 12 sans reste, elle prend la valeur 12  
            suffixe = 'AM' if heure < 12 else 'PM'                      #si heure inferieur a 12 affiche AM sinon affiche PM
            print(f"{heure_affichage:02d}:{minute:02d}:{seconde:02d} {suffixe}")
        else:
            print(f"{heure:02d}:{minute:02d}:{seconde:02d}")

        heure_alarme = (14, 31, 0)
        regler_alarme((heure, minute, seconde), heure_alarme)

        heure_tuple = (heure, minute, seconde)              # Met à jour la variable heure_tuple

        if (heure, minute, seconde) == (14,31,10):          #appel de ma fonction avec une condition
            pause()

def regler_alarme(heure_actuelle, heure_alarme):            #fonction alarme
    if heure_actuelle == heure_alarme:
        print("C'est l'heure de l'alarme!")

def pause():                #ma fonction pause
        print("Pause en cours")
        time.sleep(6)           #une pause de 6 seconde
        print("Fin de la pause")

type_horloge = am_pm()      #demande a l'utilisateur de choisir le mode d'affichage 

heure_depart = (14, 30, 50)     #heure de départ

afficher_heure(heure_depart, type_horloge)      #appel de ma fonction afficher heure


