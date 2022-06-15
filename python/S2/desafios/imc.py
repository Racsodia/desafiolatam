'''
    El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el
    peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un
    indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el
    estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:

                        IMC = W / H^2

    W : Peso de la persona en Kg
    H: Altura de la persona en metros
    IMC : Valor del índice de masa corporal en [Kg/m^2]

    Ingresasr pego en Kg y altura en centímetros por argumentos

'''
import sys

if(len(sys.argv) < 3):
    print('Debe insgresar su peso en Kg y altura en centímetros como argumentos respectivamente.')
    exit()

peso = float(sys.argv[1])
altura = float(sys.argv[2]) / 100

imc = peso / (altura ** 2)

print(f'Su IMC es: {imc:.2f}')

resultado = 'La clasificación de la OMS es: '
if imc < 18.5:
    resultado += 'Bajo Peso'
elif imc >= 18.5 and imc < 25:
    resultado += 'Adecuado'
elif imc >= 25 and imc < 30:
    resultado += 'Sobrepeso'
elif imc >= 30 and imc <35:
    resultado += 'Obesidad grado I'
elif imc >= 35 and imc < 40:
    resultado += 'Obesidad grado II'
else:
    resultado += 'Obesidad grado III'

print(resultado)




