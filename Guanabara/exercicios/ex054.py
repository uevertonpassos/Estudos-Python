from datetime import date
anoAtual = date.today().year
menor = 0
maior = 0
for pessoa in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {pessoa}° pessoa: '))
    idade = anoAtual - nascimento
    if idade < 21:
        menor += 1
    else:
        maior +=1
print(f'Das sete, {menor} pessoas são menores de idade!')
print(f'E {maior} são maiores de idade!')


