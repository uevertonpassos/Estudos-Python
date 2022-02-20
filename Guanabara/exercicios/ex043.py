#exibindo mensagens diferentes com IMCs diferentes

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura**2)
print(f'o IMC do usuário é {imc:.2f}')
if imc < 18.5:
    print('você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('você está no peso ideal!')
elif 25 <= imc <30:
    print('você está com sobrepeso!')
elif 30 <= imc <40:
    print('você está com obesidade!')
else:
    print('você está com obesidade mórbida!')
