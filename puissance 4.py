liste_grilles = [["_" for _ in range(7)] for _ in range(6)]

def grille (grille) :
    """ crée la grille """
    
    for case in grille :
        print(case)

def jouer_coup () :
    
    #affiche la grille
    grille(liste_grilles)

    #print("tour au " + joueur + "de jouer")
    coup_jouer = input()
   

def verif_grille () :
    pass

while True :
    break