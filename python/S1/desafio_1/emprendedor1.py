'''
    Emprendimiento de entrega de comida donde las utilidades se miden como: 
        Ut = P * U - GT
    
    Ut: Utilidad
    P: Precio de suscripción
    U: Número de usuarios
    GT: Gastos totales
     
'''
print('\n')
print('Para calcular la utilidad a obtener, porfavor utilice a continuación solo números.')

subscribe = int(input('Ingrese el precio de la suscripción en pesos: '))
users = int(input('Ingrese el número de usuarios: '))
expenses = int(input('Ingrese los gastos totales en pesos: '))

utilitie = subscribe * users - expenses

print(f'Su utilidad asociada a lo ingresado tiene un valor de: ${utilitie} \n')