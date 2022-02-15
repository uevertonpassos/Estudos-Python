num1 = int(input('Digite um valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2 and num1 != num2:
    print(f'Eles são diferentes entre si e o maior valor entre eles é o {num1}')
elif num1 < num2 and num1 != num2:
    print(f'Eles são diferentes entre si e o menor valor entre eles é {num1}') 
elif num1 == num2:
    print('Eles são iguais')

else:
    print('Você não digitou nada válido')
    