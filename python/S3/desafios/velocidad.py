'''
    Módulo Python - Funciones - desafío 1 semana 3 generación 49 desafíolatam

    Otra solución que se encuentra pendiente es la encargada por una empresa de flotas que
    debe medir mediante telemetría las velocidades de cada una de sus correas
    transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que,
    para poder entregar energía a las correas más lentas, es necesario ralentizar las más
    rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se
    requiere levantar una alerta de la posición de las correas transportadoras que están por
    sobre el promedio.
        
        ● Para ello se pide determinar una funcionalidad que calcule el promedio de una lista
        de velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta
        con mucha capacidad por lo que se pide no depender de librerías externas.
        
        ● Listar las posiciones de todas las correas transportadoras que están sobre el
        promedio.

    Autor: Óscar Aguilera B.
'''

velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]

def promedio(valores):
    promedio = 0   
    if not type(valores) is list:
        print('Debe ingresar una lista con números a la función')
    else:

        for i in valores:
            promedio += i
        promedio = promedio/len(valores)

    return promedio

def sobre_promedio(correas):

    return [index for index,vel in enumerate(correas) if vel > promedio(correas)]

print(sobre_promedio(velocidad))