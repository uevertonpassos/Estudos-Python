#verificando se é e que tipo de triângulo temos

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a < b +c  and b < a + c and c < a + b:
    print('É possível formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('n é possivel formar um triangulo')
