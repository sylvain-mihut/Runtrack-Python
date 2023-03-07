# Créez une fonction qui prend 2 paramètres :
# - Le premier reçoit un String nommé “type”
# - Le second reçoit un String nommé “saison”
# Si la valeur de “type” est égal à “fruits” et que celle de saison est égal à “hiver”, affichez
# “orange, mandarine et kiwi”
# Si la valeur de “type” est égal à “fruits” et que celle de saison est égal à “ete”, affichez
# “Poire, fraise, cassis”
# Si la valeur de “type” est égal à “legume” et que celle de saison est égal à “hiver”,
# affichez “carotte, topinambour, endive”
# Si la valeur de “type” est égal à “legume” et que celle de saison est égal à “ete”, affichez
# “artichaut, aubergine,navet”

def my_function(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, Mandarine et kiwi")
    elif type == "fruits" and saison == "ete" or type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete" or type == "legume" and saison == "été":
        print("artichaud, aubergine, navet")
    else:
        print("t'as tout casser !")

my_function("legume", "été")