# Créer une fonction avec 3 paramètres correspondant à trois longueurs a, b, c. À l'aide de
# ces trois longueurs, déterminer s'il est possible de construire un triangle. Déterminer
# ensuite si ce triangle est rectangle, isocèle,

def triangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a == b and b == c and c == a:
            print("C'est un triangle equilateral")
        elif a == b or b == c or c == a:
            if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
                print("c'est un triangle rectangle et isocèle")
            else:
                print("c'est un triangle isocèle")
        elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("c'est un triangle rectangle")    
        else:
            print("c'est un tiangle quelconque")
    else:
        print("ce n'est pas un triangle")

triangle(5,5,5)