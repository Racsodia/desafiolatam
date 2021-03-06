'''
    Programa que emula jugar al cachipún contra la computadora.
    Se debe ingresar como argumento la jugada del usuario: piedra, papel o tijeras
'''

import random
import sys

opciones = ['piedra', 'papel', 'tijeras']

if(len(sys.argv) < 2):
    print('Debes ingresar si juegas piedra, papel o tijeras en los argumantos de ejecución')
    exit()

if not sys.argv[1] in opciones:
    print('Debes ingresar la palabra correcta, utiliza: piedra, papel o tijeras')
    exit()

resultados_posibles = {
    'piedra': {'papel': -1, 'piedra': 0, 'tijeras': 1},
    'papel': {'tijeras': -1, 'papel': 0, 'piedra': 1},
    'tijeras' : {'piedra': -1, 'tijeras': 0, 'papel':1}
}

usuario = sys.argv[1]
maquina = random.choice(opciones)

resultado = resultados_posibles[usuario][maquina]

print(f'Tu jugaste: {usuario}')
print(f'Computador jugó: {maquina}')
if( resultado == -1 ):
    print('Perdiste')

if( resultado == 0):
    print('Empataron')

if( resultado == 1):
    print('Ganaste')

