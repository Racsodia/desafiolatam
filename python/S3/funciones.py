from traceback import print_tb


def imprimir_menu():
    print('Opciones:')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')


imprimir_menu()


def sumar_numeros():
    primer_numero = 5
    segundo_numero = 5
    print(primer_numero + segundo_numero)


sumar_numeros()


def suma(x, y):
    print(x + y)


print(suma(2, 2), suma(3,3) + suma(4,2))


def retorna_suma(x, y):
    return x + y


retorno = 3 + retorna_suma(10, 15)

print(f'la suma es {retorno}')

#Al asignar un valor inicial al parámetro, pasa a ser opcional:
def suma_eleva(x, y, z = 2):
    return x + y, x ** y

resultado_suma, resultado_elevado = suma_eleva(2,3)

print(resultado_suma,resultado_elevado)

#*args para utilizar n parámetros 

def nargs(*args):
    return args

output = nargs(1,[2,3],'hola',{'clave': [3,4]},'chao')

print(type(output))

def nargs2(*args):
    for i in args:
        print(i)

nargs2(1,[2,3],'hola',{'clave': [3,4]},'chao')

#kwargs para utilizar n parámetros pero con nombre de cada uno y su valor (asignación) y los convierte en un diccionario

def nkwargs(**kwargs):
    print(kwargs)
    for i in kwargs.values():
        print(i)

nkwargs(numero1 = 1, numero2 = 2)

#variables globales

impuesto = 1 

def utilidad(ventas, gastos):
    global impuesto #Con esto se puede editar el valor de la variable global inpuesto
    impuesto = 2
    return ventas - gastos - impuesto

print(utilidad(10,3))
print(impuesto)

