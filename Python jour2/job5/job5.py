# Créez une fonction nommée “calcule” qui prend 3 paramètres :
# ● le premier, “num1”, est un nombre,
# ● le deuxième, "operator", est un caractère (string) contenant le type d’opération
# (+, -, *, /, %),
# ● le troisième, “num2”, est un nombre.
# La fonction doit retourner le résultat de l’opération.

def calcule(num1, operator, num2):
    if operator == '+':
            print(num1 + num2)
    elif operator == '-':
            print(num1 - num2)
    elif operator == '/':
           print(num1 / num2)
    elif operator == '*':
           print(num1 * num2)
    elif operator == '%':
           print(num1 % num2)
    else:
        print("Veuillez utilisé un opérateur de calcule")

calcule(10, '-', 2)