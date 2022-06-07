'''
    Emprendimiento de entrega de comida donde las utilidades se miden como: 
        Ut = P * Un - GT
        R = Ut/Ua
    
    Ut: Utilidad
    Ua: Utilidad anterior (año pasado)
    P: Precio de suscripción
    Un: Número de usuarios
    GT: Gastos totales
    R: Razón entre utilidad actual y del año pasado
'''
print('\n')
print('Para calcular la razón entre la utilidad actual y la del año pasado utilice a continuación solo números. ')

subscribe = int(input('Ingrese el precio de la suscripción en pesos: '))
normal_users = int(input('Ingrese el número de usuarios normales: '))
expenses = int(input('Ingrese los gastos totales en pesos: '))
old_utilitie = int(input('Ingrese la utilidad del año pasado en pesos: '))

utilitie = subscribe * normal_users  - expenses
utilities_ratio = utilitie / old_utilitie

print(f'Su la razón entre su utilidad actual y la del año pasado tiene un valor de: {utilities_ratio:.2f} \n')