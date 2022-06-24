'''
   Módulo Python - Funciones - desafío 1 semana 3 generación 49 

    La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar
    un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al
    problema. Dada una muestra de los productos que actualmente se encuentran disponibles
    en la tienda (un diccionario), se solicita implementar una función que permita entregar lo
    siguiente:
        ● Un diccionario con los productos que cumplen una cierta condición dado un umbral
        ● La función debe permitir mostrar los valores mayor que o menor que un umbral
          (siempre estrictos).
        ● Por defecto la función debe siempre mostrar los valores mayor que el umbral a
          menos que se indique lo contrario.

    Autor: Óscar Aguilera Badilla
'''
from ast import If
import sys
from unittest import result

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de video': 1500000
}

opciones = ['mayor', 'Mayor', 'menor', 'Menor']


def filtro(umbral, orden='mayor'):

    if(orden == 'mayor'):
        result = {k: v for k, v in sorted(precios.items()) if v > umbral}
    else:
        result = {k: v for k, v in sorted(
            precios.items(), reverse=True) if v < umbral}

    salida = ''
    for index, texto in enumerate(result.keys()):
        salida += texto + ', ' if index != len(result) - 1 else texto
    return salida


if(len(sys.argv) < 2 or len(sys.argv) > 3):
    print('Debe ingresar solo el valor umbral a filtrar y opcionalmente los valores mayor o menor.')
    exit()

try:
    precio_filtrado = int(sys.argv[1])
except:
    print('El primer argumento debe ser un número entero indicando el precio a filtrar.')

if(len(sys.argv) > 2 and not sys.argv[2] in opciones):
    print('Debe ingresar como segundo argumento mayor/menor ó Mayor/Menor si desea especificar el tipo de filtrado.')
    exit()
elif(len(sys.argv) > 2 and sys.argv[2] in opciones):
    orden_filtrado = sys.argv[2].lower()
    print(
        f'Los productos {orden_filtrado}es al filtrado son: {filtro(precio_filtrado,orden_filtrado)}')
else:
    print(f'Los productos mayores al filtrado son: {filtro(precio_filtrado)}')
