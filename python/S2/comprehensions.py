'''
    Python list comprehensions es un método para crear listas iterando con un for
'''

nombres = ['Oscar','Pablo','Juanita','Anita','Nicolás']

lista = [nombre.upper()  if nombre=='Pablo' else nombre.lower() for nombre in nombres]

habitantes = {'Alabama': 12300, 'Michigan':90345, 'San Francisco': 103405}
print(habitantes.items())
nuevo = {k:(v+12 if v<50000 else v-12) for k,v in habitantes.items() }

print(lista)
print(nuevo)