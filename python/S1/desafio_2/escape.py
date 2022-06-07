'''
    Se define la velocidad de escape de un planeta como
    la mínima velocidad necesaria para salir de este 
    venciendo a la gravedad. Se calcula como:

        Ve = sqrt(2 * g * r)

    Ve: Velocidad de escape [m/s]
    g: gravedad [m/s^2]
    r: radio del planeta [m]
'''
import math

print('Para calcular la velocidad de escape de un planeta, a continuación:')

gravity = float(input('Ingrese la fuerza de gravedad del planeta: '))
radio = float(input('Ingrese el radio del planeta en en kilómetros: '))

escape_velocity = math.sqrt(2 * gravity * radio * 1000)

print(f'La velocidad de escape del planeta según sus datos es: {escape_velocity:.1f} [m/s]')

