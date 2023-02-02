resposta = 'S'
soma = quant = media = 0

while resposta in 'Ss':
    num = float(input('Digite um valor:'))
    soma +=num
    quant+=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    
    resposta = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
media = soma/quant
print(f'vc digitou {quant} números e a média foi {media}')
print(f'o menor valor digitado foi {menor} e o maior foi {maior}')
