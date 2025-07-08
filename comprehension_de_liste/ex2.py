# Génère une liste des nombres pairs entre 0 et 20 inclus

def even_numbers():
    liste = []

    for i in range(0, 21):
        if i % 2 == 0:
            liste.append(i)

    print(liste)

even_numbers()
