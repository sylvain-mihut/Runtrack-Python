# Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l'inversant. Par
# exemple, « nikana » deviendra « anakin ».

mot = input('donnez un mot')
lettre = len(mot)-1

while lettre >= 0:
    print(mot[lettre])
    lettre -= 1