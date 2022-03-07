soma = 0
cont = 0
for par in range (1,7):
    num = int(input('Digite um número: '))
    if num % 2 ==0:
        soma += num
        cont += 1
print(f'Você digitoU{cont} NUMEROS PARES e a soma deles é {soma}')
