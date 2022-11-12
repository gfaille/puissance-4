import os
import time

liste_grilles = [["_" for _ in range(7)] for _ in range(6)]

def grille (grille) :
    """ crée la grille """
    
    for case in grille :
        print(case)

def jouer_coup (coup_jouer) :
    """ variable qui est global (pour la faire sortir de la fonction), 
        verfier 
        - si coup_jouer est inférieur ou égal à 7
        - si liste_grille à l'index donner est égal à "_" 
        boucle for pour faire descendre le jeton
    """
    global coup_placer

    while True :

        if coup_jouer <= 7 :
            if liste_grilles[0][coup_jouer-1] == "_" :
                coup_placer = -1
                for i in range(6) :
                    os.system("cls")
                    if liste_grilles[i][coup_jouer-1] == "_" :
                        liste_grilles[i][coup_jouer-1] = joueur
                        coup_placer += 1

                        if i > 0 :
                            liste_grilles[i-1][coup_jouer-1] = "_"
                        grille(liste_grilles)
                        time.sleep(0.1)
                    
                return 
            else :
                return print("case déjâ utiliser !")
        else :
            return print("coups non valide !")

def verif_ligne_vertical (coup_jouer, coup_placer) :
    """ une boucle for  pour vérifier si 4 jeton son aligner verticalement
    """
    coup_jouer -= 1
    gagner = 0

    for _ in range(4) :
        if coup_placer <= 5 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_placer += 1

def verif_ligne_horizontal (coup_jouer, coup_placer) :
    """ 4 boucle for pour verifier horizontalement si 4 jeton sont aligner 
        1) verifier a partir du dernier jeton jouer à sa droite 
        2) verifier a partir du dernier jeton jouer à sa droite la difference et que si l'utilisateur joue au centre 
            il reprend le jeton à coter
        3) verifier a partir du dernier jeton jouer à sa gauche
        4) verifier a partir du dernier jeton jouer à sa droite la difference et que si l'utilisateur joue au centre 
            il reprend le jeton à coter
    """

    #############################################################
    #                                                           #
    #   reprend le dernier coup jouer et le coups placer        #
    #   vérifie si 4 jetons sont aligner en partant a droite    #
    #                                                           #
    #############################################################

    coup_jouer -= 1
    coup_jouer_preced = coup_jouer
    gagner = 0

    for _ in range(4) :
        if coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer += 1
    

    #########################################################
    #                                                       #
    #   reprend le dernier coup jouer et le coups placer    # 
    #   -1 par rapport à l'index pour vérifier              #
    #   si 4 jetons sont aligner en partant à droite        #
    #                                                       #
    #########################################################
    coup_jouer = coup_jouer_preced
    gagner = 0
    coup_jouer -= 1
    for _ in range(4) :   
        if coup_jouer <=6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer += 1

    #########################################################
    #                                                       #
    #   reprend le dernier coup jouer et le coups placer    #
    #   si 4 jetons sont aligner en partant à gauche        #
    #                                                       #
    #########################################################

    coup_jouer = coup_jouer_preced
    gagner = 0
    for _ in range(4) :   
        if coup_jouer >= 0 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer -= 1

    #########################################################
    #                                                       #
    #   reprend le dernier coup jouer et le coups placer    #
    #   +1 par rapport à l'index pour vérifier              #
    #   si 4 jetons sont aligner en partant à gauche        #
    #                                                       #
    #########################################################

    coup_jouer = coup_jouer_preced
    gagner = 0
    coup_jouer += 1
    for _ in range(4) : 
        if coup_jouer <= 6 : 
            if coup_jouer >= 0 :
                liste_grilles[coup_placer][coup_jouer]

                if liste_grilles[coup_placer][coup_jouer] == joueur :
                    gagner += 1
                    if gagner == 4 :
                        print(joueur, "à gagner !!")
                        return True
                coup_jouer -= 1
        
def verif_ligne_diagonale_droite (coup_jouer, coup_placer) :
    """ 4 boucle for pour verifier diagonalement si 4 jeton sont aligner

        1) verifie la diagonal droite descendant 
        2) verifie la diagonal droite descendant reprend le jeton à coter puis verifie
        3) verifie la diagonal droite montant
        4) verifie la diagonal droite mantant reprend le jeton à coter puis verifie
    """
    coup_jouer -= 1
    coup_jouer_preced = coup_jouer
    coup_placer_preced = coup_placer
    gagner = 0

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer += 1
            coup_placer +=1
    
    coup_jouer = coup_jouer_preced
    coup_placer = coup_placer_preced
    gagner = 0

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer -= 1
            coup_placer -=1
 
    coup_jouer = coup_jouer_preced
    coup_placer = coup_placer_preced
    gagner = 0
    coup_jouer += 1
    coup_placer += 1

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer -= 1
            coup_placer -=1

    coup_jouer = coup_jouer_preced
    coup_placer = coup_placer_preced
    gagner = 0
    coup_jouer -= 1
    coup_placer -= 1

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer += 1
            coup_placer +=1

def verif_ligne_diagonale_gauche (coup_jouer, coup_placer) :
    """ 4 boucle for pour verifier diagonalement si 4 jeton sont aligner

        1) verifie la diagonal gauche descendant 
        2) verifie la diagonal gauche descendant reprend le jeton à coter puis verifie
        3) verifie la diagonal gauche montant
        4) verifie la diagonal gauche mantant reprend le jeton à coter puis verifie
    """
    coup_jouer -= 1
    coup_jouer_preced = coup_jouer
    coup_placer_preced = coup_placer
    gagner = 0

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer -= 1
            coup_placer +=1
    
    coup_jouer = coup_jouer_preced
    coup_placer = coup_placer_preced
    gagner = 0

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer += 1
            coup_placer -=1
 
    coup_jouer = coup_jouer_preced
    coup_placer = coup_placer_preced
    gagner = 0
    coup_jouer += 1
    coup_placer -= 1

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer -= 1
            coup_placer +=1

    coup_jouer = coup_jouer_preced
    coup_placer = coup_placer_preced
    gagner = 0
    coup_jouer -= 1
    coup_placer += 1

    for _ in range(4) :
        if coup_placer >= 0 and coup_placer <= 5 and coup_jouer >= 0 and coup_jouer <= 6 :
            liste_grilles[coup_placer][coup_jouer]

            if liste_grilles[coup_placer][coup_jouer] == joueur :
                gagner += 1
                if gagner == 4 :
                    print(joueur, "à gagner !!")
                    return True
            coup_jouer += 1
            coup_placer -=1
            
joueur = "J"

while True :

    os.system("cls")
    #affiche la grille
    grille(liste_grilles)

    coup_jouer = int(input("tour au " + joueur + " de jouer : "))

    jouer_coup(coup_jouer)
    
    if verif_ligne_horizontal(coup_jouer, coup_placer) :
        grille(liste_grilles)
        time.sleep(5)
        os.system("cls")
        break
    elif verif_ligne_vertical(coup_jouer, coup_placer) :
        grille(liste_grilles)
        time.sleep(5)
        os.system("cls")
        break
    elif verif_ligne_diagonale_droite(coup_jouer, coup_placer) :
        grille(liste_grilles)
        time.sleep(5)
        os.system("cls")
        break
    elif verif_ligne_diagonale_gauche(coup_jouer, coup_placer) :
        grille(liste_grilles)
        time.sleep(5)
        os.system("cls")
        break

    if joueur == "J" :
        joueur = "R"
    else :
        joueur = "J"