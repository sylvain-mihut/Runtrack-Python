# Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises
# dans l’intervalle [25, 90]
# L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
result = 1

for i in L:
    if 25 <= i <= 90:
        result *= i

print(result)

