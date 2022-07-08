'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

'''

while True:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade:'))       
    salario = float(input('Digite o seu salário: '))
    sexo = input('Qual o seu sexo? [F] [M]: ')
    estCivil = input('Digite o seu estado civil: s, c, v, d' )

    if nome.count(nome) < 3:
        print('Nome validado!')
    else:
        print('Precisamos de um nome maior')
    
    if idade >= 0 and idade <= 150:
        print('Idade validada!')
    else:
        print('Sua idade está muito acima')
    
    if salario == 0:
        print('Salário indevido')
    else:
        print('Salário validado')
    if sexo == "F":
        print('Bem vinda!')
    else:
        print('Bem vindo!')
    if estCivil == 's' or 'c' or 'v' or 'd':
        print('Estado civil validado')