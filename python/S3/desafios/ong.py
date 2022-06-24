
'''
    Módulo Python - Funciones - desafío 1 semana 3 generación 49 desafíolatam
    
    Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda
    escolar que tiene la esta ONG se está enseñando a programar algunas operaciones
    avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos
    operaciones conocidas como el factorial y la productoria y se requiere que usted prepare
    una script que implemente esto.

    Autor: Óscar Aguilera B.
'''

def factorial(numero):
    multiplicacion = 1
    for i in range(1,numero+1):
        multiplicacion *= i
    return multiplicacion
    
def productoria(numeros):
    producto = 1
    print(f'numeros: {numeros}')
    for i in numeros:
        producto*=i
    return producto

def calcular(**kwargs):
    for i in kwargs.values():
        if(type(i) is list):
            print(f'La productoria de {i} es: {productoria(i)}')
        elif(type(i) is int):
            print(f'El factorial de {i} es: {factorial(i)}')
        else: 
            print('Debe ingresar un numero entero o una lista')

calcular(fact_1 =5, prod_1 = [4,6,7,4,3], fact_2 = 6)