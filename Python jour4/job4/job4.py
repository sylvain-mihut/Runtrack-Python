# Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
# “pomme”, “cerise”, “orange, Melon”. Cette fonction doit à son appel ajouter à la liste
# “fruits” une String “Mangue” à l’index 2.

def My_liste():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2,"mangue")
    print(fruits)

My_liste()