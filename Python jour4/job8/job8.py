# Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste
# L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

count = 0 
tour = 0

while tour < len(L):
    if L[tour] % 2 == 0:
        count += L[tour]
    tour += 1

print(count)