'''
    Desafío evaluado: Estructuras de datos
    Estudiante: Óscar Aguilera B.

    El objetivo es crear una conversión de divisas: Sol, Peso argentino y dólar americano a peso chileno
    ingresando a través de argumentos al iniciar el programa los valores correspondientes.
    El cuarto elemento de los argumentos debe ser la cantidad de pesos chilenos a convertir.
'''

import sys

sol = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])
pesos_chilenos = float(sys.argv[4])

conversion_1 =  pesos_chilenos * sol
conversion_2 = peso_argentino * pesos_chilenos
conversion_3 = pesos_chilenos * dolar

print(f'Los ${pesos_chilenos:.0f} equivalen a: ')
print(f'${conversion_1:.1f} Soles peruanos')
print(f'${conversion_2:.1f} pesos argentinos')
print(f'${conversion_3:.1f} dólares')




