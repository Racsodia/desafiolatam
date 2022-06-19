
lista1 = [1, 2, 3, 4, 5, 6, 7]
for lista in lista1:
    print(lista)

for lista in range(1, 3):
    print(lista)

for palabra in "Aguilera":
    print(palabra)

for contador, elemento in enumerate(lista1):
    print(elemento, contador)

notas = {'Raúl': 2, 'Milton': 4, 'Oscar': 5, 'Dani': 7}

for i, j in enumerate(notas):
    print(i, j)

nombres = ['Raúl', 'Milton', 'Oscar', 'Dani']
notas = [2, 4, 5, 7]

for i,j in zip(nombres,notas):
    print(i,j)

dict_notas = dict(zip(nombres,notas))
print(dict_notas)