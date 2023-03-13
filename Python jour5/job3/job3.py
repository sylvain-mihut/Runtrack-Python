# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
# lignes/n+1 colonnes traversé par une diagonale.

def My_function(n):
    # Dessine le bord supérieur du rectangle
    print("+" + "-" * (n+2) + "+")
    # Boucle pour dessiner chaque ligne du rectangle
    for i in range(n+1):
        # Dessine un "|" pour encadrer la ligne
        print("|", end="")
        # Boucle pour dessiner chaque caractère de la ligne
        for j in range(n+2):
            if i == j:
                # Si on est sur la diagonale de la ligne, dessine un "#"
                print("#", end="")
            elif i + j == n:
                # Si on est sur la diagonale inverse de la ligne, dessine un " "
                print(" ", end="")
            else:
                # Sinon, dessine un "#"
                print("#", end="")
        # Dessine un "|" pour encadrer la ligne
        print("|")
    # Dessine le bord inférieur du rectangle
    print("+" + "-" * (n+2) + "+")

My_function(eval(input("dimension ? ")))            