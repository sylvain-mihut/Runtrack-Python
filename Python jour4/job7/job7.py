# Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste
# L = [8, 24,48,2,16]

L = [8, 24, 48, 2, 16]
count = 0
tour = 0

while tour < len(L):
    if L[tour] % 3 ==0:
        count += 1
    tour +=1

print(count)
