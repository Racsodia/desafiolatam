
import random
import sys

opciones = ['piedra', 'papel', 'tijeras']

resultados_posibles = {
    'piedra': {'papel': -1, 'piedra': 0, 'tijeras': 1},
    'papel': {'tijeras': -1, 'papel': 0, 'piedra': 1},
    'tijeras' : {'piedra': -1, 'tijeras': 0, 'papel':1}
}


if(len(sys.argv) < 2):
    print('Debes ingresar si juegas piedra, papel o tijeras en los argumantos de ejecución')
    exit()

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

