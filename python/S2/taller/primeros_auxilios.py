'''
    Taller 2: Módulo python - Carrera Data Science Desafío Latam - gen 49

    Programa que señala los pasos para entregar primeros auxilios. Se deben ingresar por teclado las respuestas
    y el programa dede ir indicado como proceder.

    Autor: Óscar Aguilera B. 

'''


print('Por favor, responda con (si) sí o no \n')
estimulos = input('¿Responde a estímulo? ')
ambulancia = 'no'
if (estimulos == 'sí' or estimulos == 'si'):
    print('Valorar la necesidad de llevarlo al hospital más cercano \n')
    exit()
else:
    print('Abrir vía aérea')
    respira = input('¿Respira? ')
    if(respira == 'sí' or respira == 'si'):
        print('Permitirle posición de suficiente respiración')
        exit()
    else:
        print('Administrar 5 ventilaciones y llamar a una ambulancia')
        while(ambulancia == 'no'):
            signos = input('¿Signos de vida? ')
            if(signos == 'sí' or signos == 'si'):
                print('Reevaluar la espera de la ambulancia')
            else:
                print('Administrar compresiones torácicas hasta que llegue la ambulancia')
            ambulancia = input('¿Llegó la ambulancia? ')

