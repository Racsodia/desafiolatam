import getpass

password = getpass.getpass('Ingrese la clave secreta: ')

print(password)

while password != 'hola mundo':
    password = getpass.getpass(
        'La clave secreta es incorrecta, intenta otra vez: ')

print('Clave correcta.')

i = 0

while i < 10:
    print(f'Esto se mostrará 10 veces: {i} ')
    i += 1

