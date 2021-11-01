nome = input("Digite seu nome: ")
idade = input("Digite a sua idade: ")

if idade.isdigit():
    idade = int(idade)
else:
    pass
while idade <= 18:
    print('Você não pode entrar ainda')
    