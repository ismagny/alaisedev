# Génère une liste des carrés des nombres de 0 à 9

def square():
    list = []
    for i in range(0, 10):
        square = i ** 2
        list.append(square)
    print(list)

square()

