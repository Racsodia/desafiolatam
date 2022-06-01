import math

print('Hola mundo!')
print(30/5)
print(math.sqrt((4*4)**0))
print(5*5/25)
print(5%2)
print((3+8)//11)
print(', '.join(['a','b','c']))
print("constitucion".count('t')) #Cuenta la cantidad de letras t en el string
print(3 * "Oscar ")
print('upper'.upper())
print('LOWER'.lower())
print('programa en python'.title())
print(len('cuantos caracteres tengo?'))
print('Había\nuna\nvez')

#tipos de variable
entero = 25
decimal = -6.5
texto ='Hola mi gente'
print(type(entero))
print(type(decimal))
print(type(texto))

nombre = 'Oscar'
apellido = 'Aguilera'

print(f'Mi nombre es {nombre} {apellido}')
print("Mi nombre es {} {}".format(nombre, apellido)) #obsoleto