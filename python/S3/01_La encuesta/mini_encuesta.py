def imprimir_menu():
    print('Opciones')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

preguntas = ['Enunciando pregunta 1', 'Enunciado pregunta 2', 'Enunciado pregunta 3']

respuestas = []

for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input('>'))

print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 1 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 1 fue {respuestas[2]}')

print('Muchas gracias por responder la encuesta')