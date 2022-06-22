'''
    Taller 2: Módulo python - Carrera Data Science Desafío Latam - gen 49

    ¿Qué tan seguro es tu password? ¿Intentemos hackear un password? Mediante el siguiente
    desafío se busca utilizar un algoritmo muy sencillo, llamado fuerza bruta para determinar
    cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.
    Para ello se ingresará un password oculto. Este password puede contener sólo
    combinaciones de letras y se requiere determinar su seguridad. Un mayor número de
    intentos implica un password más seguro:

    Autor: Óscar Aguilera B.

'''
import getpass
from string import ascii_lowercase

password = getpass.getpass('Ingrese la contraseña: ')
intentos = 0
for letra in password:
    for ascii in ascii_lowercase:
        intentos += 1
        if(ascii == letra):
            break
        
        

print(f'La contraseña fue forzada en {intentos} intentos')
