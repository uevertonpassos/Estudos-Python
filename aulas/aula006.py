# Variáveis

# Variaveis detém o valores a serem usados posteriormente no código

#exercício proposto:

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
print('{} tem  {} anos e o seu imc é de {:.2f}'.format(nome, idade, imc))   
