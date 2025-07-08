# créez une fonction qui prend en paramètre une suite de longueur indéterminée de int
# et qui renvoi la valeur en bit de la multiplication de ceux ci

def taille_multiplication(*entier):
    suite = 0
    for i in entier:
        suite *= i
    return bin(suite)

print(taille_multiplication(1,2,3))



