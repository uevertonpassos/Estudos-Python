nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
genero = input('Digite o seu gênero: ')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)
print(f'O IMC de {nome} é de {imc:.2f} ')

