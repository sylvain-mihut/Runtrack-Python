# Créez une fonction qui prend en paramètre une String nommée “langage”.
# Si la valeur de “langage” est égal à “javascript” affichez “tu es un developpeur web”
# Sinon si la valeur de “langage” est égal à “python” affichez “tu es un developpeur IA”
# Sinon si la valeur de “langage” est égal à “java” affichez “tu es un developpeur logiciel”
# Sinon si la valeur de “langage” est égal à “reactjs” affichez “tu es un developpeur mobile”
# Sinon, affichez “un jour, je serai le meilleur developpeur... ”

langage = input(">> Quelle langage utilise tu ? ")

def dev(langage):
    if langage == "javascript" or langage == "Javascript":
        print("Tu es un développeur web !")
    elif langage == "python" or langage == "Python":
        print("tu es un développeur I.A !")
    elif langage == "java" or langage == "Java":
        print("tu es un développeur logiciel !")
    elif langage == "reactjs" or langage == "Reactjs" or langage == "React" or langage == "react":
        print("tu es un développeur mobile !")
    else:
        print("Un jour, je serai le meilleur développeur ....")

dev(langage)