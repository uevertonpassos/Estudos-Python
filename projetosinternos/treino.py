# tentando fazer o meu proprio projeto para treinar funções

def cadastro(nome):
    ListaCadastro.append(nome)

def delete(nome):
    if nome in ListaCadastro:
        indice = ListaCadastro.index(nome)
        del ListaCadastro[indice]



ListaCadastro = ['UEV','MÁRCIA', 'ANGÉLICA']

menu = input('''
____________________MENU_______________________
===============================================
[1] Cadastrar um novo nome
[2] Verificar se algum nome já está cadastrado
[3] Deletar algum nome cadastrado
===============================================

Escolha uma opção=> ''')

if menu == '1':
    nome = input("Digite o nome que deseja cadastrar: ").upper()
    cadastro(nome)
elif menu == '2': 
    nome = input('Digite o nome que deseja buscar no banco de dados: d').upper()
elif menu == '3':
    nome = input("Digite o nome que deseja deletar: ").upper()
    delete(nome)


print(ListaCadastro)