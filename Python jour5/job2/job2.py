# Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple :
# draw_rectangle(10, 3)

# On demande à l'utilisateur d'entrer la hauteur et la largeur du rectangle
height = int(input("Entrez la hauteur : "))
width = int(input("Entrez la largeur : "))

# On définit le caractère pour les côtés du rectangle
side = "|"
# On initialise le caractère de séparation avec un trait horizontal
separator = "-"

# On boucle sur chaque ligne du rectangle
for Range in range(height):
    # Si c'est la première ou la dernière ligne, on utilise un trait horizontal pour la séparation
    if Range == 0 or Range == height -1:
        separator = "-"
    # Sinon, on utilise un espace pour la séparation
    else:
        separator = " "
    # On affiche la ligne courante du rectangle en concaténant les différentes parties : côté gauche, séparation, côté droit
    print(side + separator * height + side)