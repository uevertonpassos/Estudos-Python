a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))


delta = (b**2 ) - 4 * a * c

if a == 0:
    print('O valor de A tem que ser maior que 0')
elif delta < 0:
    print("Não possui raizes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print(f'x1 = {x1} e x2 = {x2}')
