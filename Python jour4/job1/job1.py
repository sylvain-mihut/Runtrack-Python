# Écrire une fonction qui retourne une liste nommée “fruits” qui contient les string
# “pomme”, “cerise”, “orange”.

def My_liste():
    fruits = ["pomme", "cerise", "orange"]
    
    mot = 0 
    long = len(fruits)
    
    while mot < long:
        print(fruits[mot])
        mot += 1

My_liste()