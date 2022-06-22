soma = 0
cont = 0
for par in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'vc informou {cont} numeros pares e a soma entre eles é: {soma}')
