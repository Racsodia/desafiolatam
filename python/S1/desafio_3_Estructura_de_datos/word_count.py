import sys

with open(sys.argv[1], 'r') as file:
    texto = file.read()

    palabras = texto.split(' ')

    print(f'Este texto tiene {len(palabras)} palabras')
    print(f'El número de caracteres distintos es: {len(set(texto))}')
    print(f'El número de palabras distintas es: {len(set(palabras))}')