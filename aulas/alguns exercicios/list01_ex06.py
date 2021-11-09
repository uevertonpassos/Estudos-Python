from math import sqrt

lado1 = int(input('Digite um lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triãngulo: '))
area = sqrt (((lado1+lado2+lado3) /2) * (((lado1+lado2+lado3)/2) - lado1) * (((lado1+lado2+lado3)/2) - lado2) * (((lado1+lado2+lado3)/2) - lado3))
print(f'A área do triângulo é: {area:.2f}cm')
