# Créez une fonction qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88

count = 0 

while count <= 100:
    if count == 26 or count == 37 or count == 88:
        count += 1
    else:
        print(count)
        count += 1
