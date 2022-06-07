'''
    Emprendimiento de entrega de comida donde las utilidades se miden como: 
        Ut = P * (Un + 1.5 * Up) - GT
    
    Ut: Utilidad
    P: Precio de suscripción
    Un: Número de usuarios normales
    Up: Número de usuarios premium
    GT: Gastos totales
     
'''
print('\n')
print('Para calcular la utilidad a obtener, porfavor utilice a continuación solo números. ')

subscribe = int(input('Ingrese el precio de la suscripción en pesos: '))
normal_users = int(input('Ingrese el número de usuarios normales: '))
premium_users = int(input('Ingrese el número de usuarios premium: '))
expenses = int(input('Ingrese los gastos totales en pesos: '))

utilitie = subscribe * (normal_users + 1.5 * premium_users) - expenses

print(f'Su utilidad asociada a lo ingresado tiene un valor de: ${int(utilitie)} \n')
