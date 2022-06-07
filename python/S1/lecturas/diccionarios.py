'''
    Diccionario: Estructura de datos compuesta por pares clave:valor
    Para acceder a los elementos de un diccionario se hace a través de su clave
'''

diccionario = {'a': 25, 'b': 'hola', 'c': {'d': 2, 'e': 'mundo'}}

print('Elemento d de clave c',diccionario['c']['d'])

# Se agrega un elemento al diccionario:

diccionario['f'] = 'nuevo elemento'

print('Se agrega el elemento f',diccionario)

# Se elimina un elemento del diccionario:

del diccionario['b']

print('Se eleimina el elemnto b',diccionario)

eliminado = diccionario.pop('a')

print('Se extrae el valo del elemento a',eliminado)
print('Se elimina el elemento a',diccionario)

# Unión de dos diccionarios:

persona = {'nombre': 'Oscar', 'apellido': 'Aguilera', 'edad': 34}
mascotas = {'mascota_1': 'Antü', 'mascota_2': 'Rimü'}

persona.update(mascotas)
print('diccionarios unidos:',persona)

mascotas = {'mascota_1': 'Antü', 'mascota_2': 'Rimü', 'edad':35}

persona.update(mascotas)
print('unión con colisión:',persona)