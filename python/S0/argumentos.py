import sys

nombre = sys.argv[1]
apellido = sys.argv[2]

print(f'El nombre de este archivo es: {sys.argv[0]} \n')
print(f'El nombre instroducido es: {nombre} {apellido}')
print(f'El len de argv es: {len(sys.argv)}')