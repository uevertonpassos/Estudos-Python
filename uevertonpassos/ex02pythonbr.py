'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    login = input('Escolha um login: ')
    senha = input('Agora escolha uma senha: ')

    novoUsuario = login
    novaSenha = senha

    while True:
        signIn = input('Digite o seu usuário: ')
        password = input('Digite a sua senha: ')
        if signIn == novoUsuario and password == novaSenha:
            print('Bem vindo! Login efetuado com sucesso!')
            continue
        else: 
            print('Usuário e/ou senha inválidos') 
            break  

        