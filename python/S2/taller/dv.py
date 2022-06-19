'''
    Taller 2: Módulo python - Carrera Data Science Desafío Latam - gen 49

    Módulo 11 es un algoritmo con el cual se calcula el dígito verificador (o DV, es el número que
    va después del guión), para los RUT en chile. Este número evita que cualquier persona pueda
    inventar un RUT aleatoriamente.
    Se pide crear un programa en Python llamado dv.py que permita ingresar el número de RUT
    sin puntos ni DV y devuelva el DV correspondiente.

    Autor: Óscar Aguilera B.
'''

rut = input('Ingresa tu RUT sin puntos ni digito verificador: ')

multiplicador = 2
suma = 0

for numero in rut[::-1]:
    suma += int(numero) * multiplicador
    multiplicador += 1
    if(multiplicador == 8):
        multiplicador = 2

resto = suma % 11

dv = 11 - resto

if(dv == 10):
    dv = 'K'
elif dv == 11:
    dv = 0

print(f'Su dígito verificador es {dv}')

