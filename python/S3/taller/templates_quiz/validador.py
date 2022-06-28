
def validate(opciones, eleccion):

    if eleccion not in opciones:
        eleccion = input("Ingrese una opcion valida: ")
        validate(opciones, eleccion)
    else:
        return eleccion


if __name__ == '__main__':

    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0', '1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
