from datetime import date
from time import sleep
anoAtual = date.today().year
maiores = 0
mulheresMenores = 0
homensCadastrados = 0
sair = ""


while True:
    idade = int(input("Digite a sua idade: "))
    if idade >=18:
        maiores += 1  
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper().strip()[0]
    print("Cadastrado com sucesso! ")
    escolha = str(input("Deseja cadastrar mais alguém? [S/N]: ")).upper().strip()[0]
    if escolha == "S":
        print("certo, recomeçando! ")
    if sexo == "F" and idade <= 20:
        mulheresMenores += 1              
    elif sexo == "M":
        homensCadastrados += 1
        sleep(1)
    else:
        print("=======================================")
        print(f'{maiores} pessoas são maiores de idade')
        print(f'foram cadastrados {homensCadastrados} homens')
        print(f'temos {mulheresMenores} mulheres com menos de vinte anos')
        print("=======================================")
    
    



