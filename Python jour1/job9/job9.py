mot=str (input("Entrez un mot et je vous dirai combien il contient de \"e\" :")) 

compteur=0

for lettre in mot:
    if lettre == 'e':
        compteur+=1
print ("il y ",compteur," dans votre mot")


for i in range(0,15):
    if i == 10:
        print("on est sur 10")
    else:
        print(i)