# Écrire un programme qui affiche les nombres premiers jusqu’à 1000.

check = True
count = 2

for count in range(2,1000):
    for div in range(2, count):
        if count % div == 0:
            check = False
    if check == True:
        print(count)        
    check = True