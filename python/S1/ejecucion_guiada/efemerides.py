# Se utilizan diccionarios para guardar fechas importantes

efemerides = {
    '1 de enero': 'Año nuevo',
    '27 de febrero' : 'Terremoto en Chile',
    '8 de marzo' : 'Día de la mujer trabajadora',
    '21 de mayo' : 'Glorias navales',
    '18 de septiembre': 'Fiestas patrias',
    '19 de septiembre' : 'Glorias del ejército',
    '25 de dicimebre' : 'Navidad'
}

fecha = input('Ingrese una fecha: ').lower()

print(f'Efemérida: {efemerides.get(fecha, "No hay efemérides para esta fecha")}')