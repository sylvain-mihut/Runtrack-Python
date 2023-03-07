# Créez une fonction qui prend en paramètre un nombre nommé “nombre”.
# Afficher “positif” si le nombre est supérieur à 0
# Afficher “negatif” si le nombre est inférieur à 0
# appelez cette fonction plusieurs fois en y passant des paramètres différents pour
# afficher ces résultats.

def nombre(num):
    if num <0:
        print("Négatif")
    elif num >0:
        print("Positif")
    else:
        print("null")

nombre(1)
nombre(-1)
nombre(0)
nombre(3)
nombre(-3)