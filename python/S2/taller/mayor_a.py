'''
    Taller 2: Módulo python - Carrera Data Science Desafío Latam - gen 49

    Programa que retorna todos los meses en los cuales una empresa superó el umbral ingresado como parámetro

    Autor: Óscar Aguilera B.
'''

import sys

ventas = {
    'Enero':15000,
    'Febrero':22000,
    'Marzo':12000,
    'Abril':17000,
    'Mayo':81000,
    'Junio':13000,
    'Julio':21000,
    'Agosto':41200,
    'Septiembre':25000,
    'Octubre':21500,
    'Noviembre':91000,
    'Diciembre':21000
}

if(len(sys.argv) < 2):
    print('Debe ingresar un número umbral como parámetro')
    exit()

umbral = int(sys.argv[1])

resultado = {k:v for k,v in ventas.items() if v > umbral }

print(resultado)