import sys
import time


if(len(sys.argv) < 2):
    print('Tienes que ingresar el argumento para el timer: bomba.py "entero"')
    exit()

i = int(sys.argv[1]) #Valor inicial para el timer de la bomba

while i > 0 :
    print(f'La bomba explotará en: {i} segundos')
    time.sleep(1)
    i -= 1

print('BOOM!')