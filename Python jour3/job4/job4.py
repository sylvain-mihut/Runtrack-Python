# Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les multiples de
# trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
# les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".

count = 0

for count in range(1, 101):
    if count %3 == 0 and count %5 == 0:
        print("FizzBuzz")
    elif count %3 == 0:
        print("Fizz")
    elif count %5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1