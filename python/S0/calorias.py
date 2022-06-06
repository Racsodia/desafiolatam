'''
    Pregunta a resolver: ¿Cómo se calculan las calorías de un alimento?
    Datos:
        - Cada proteína y carbohidrato aporta 4 calorías por gramo.
        - Las grasas aportan 9 calorías por gramo.
        - El valor de las calorías se redondean al entero superior más cercano
        - Cálculo de calorías: 4 * (proteína + carbohidratos) + 9 * grasa
'''

import math
proteina = float(input('Ingrese los gramos de proteínas: \n'))
carbohidratos = float(input('Ingrese los gramos de carbohidratos: \n'))
grasa = float(input('Inrese los gramos de grasa: \n'))

calorias = 4 * (proteina + carbohidratos ) + 9 * grasa 

print(f'Las calorías totales del producto son: {math.ceil(calorias)}')