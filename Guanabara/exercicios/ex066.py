contador = 0
soma = 0

while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        print('Acabou')
        break
    else:
        contador +=1
        soma +=num
print(f'Vc digitou {contador} valores e a soma entre eles vale {soma}')
