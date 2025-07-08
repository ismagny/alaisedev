# crée une liste de liste
# pour les tables de multiplications de 1 à 10
# [[1,2,3,...], [2,4,6,...],...]

list = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(list)
