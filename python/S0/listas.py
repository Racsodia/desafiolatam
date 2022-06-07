# Archivo donde se estudian las listas

# Definir una lista:

lista1 = [1, 2, 3, 4]

print(lista1)
print(lista1[0])
print(lista1[-2], lista1[-1])

# Métodos comunes usados en listas

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
colores = ['verde', 'rojo', 'rosa', 'azul']
# Ver métodos posibles a usar:

# print(lista_de_numeros.__dir__())

# Método para gregar un elemento a la lista:

colores.append('celeste')
print(colores)

lista_de_numeros.append(13)
print(lista_de_numeros)

# Insertar elemento en una posición específica:

lista_de_numeros.insert(11, 12)
print(lista_de_numeros)

# Método para sacar el úiltimo elemento de la lista

colores.pop()
print(colores)

colores.pop(2)
print(colores)

# Método para eliminar un elemento de la lista con un valor específico

colores.remove('rojo')
print(colores)

# Método para invertir el orden de la lista

lista_de_numeros.reverse()
print(lista_de_numeros)

# Método para ordenar los elementos de forma ascendente

colores.sort()
print(colores)

'''
    Alternativa:
        -Ordenamiento ascendente: 
            sorted([4,2,6,3,8,7])
        -Ordenamiento descendente:
            sorted([4,2,6,3,8,7],reverse = True)
'''
# Que es el triple índice? se nombra para leer los strings inversamente

# Concatenación

animales = ['gato', 'perro', 'vaca', 'cerdo']
animales_2 = ['gallina', 'gallo', 'caballo']

print(f'listas concatenadas: {animales+ animales_2}')
print(f'signo * en listas: {animales*3}')

animales[1] = 'cachorros'
print(animales)
print(sorted(animales, reverse=True))


