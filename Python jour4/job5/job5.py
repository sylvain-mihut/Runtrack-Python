# Écrire un programme qui créé une liste nommée “L” d’au moins 5 entiers puis
# successivement :
# - Afficher la valeur de L[1]
# - Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
# - Puis afficher la valeur du dernier terme de la liste.

L = [5, 6, 7, 8, 9]
print(L[1])

def New_L3():
    L[3] = L[2]+L[4]
    # print(L[3])

New_L3()

print(L[4])