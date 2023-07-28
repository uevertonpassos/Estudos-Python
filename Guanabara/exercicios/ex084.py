#faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista, No final mostre:

# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com pessoas mais leves.

mais_pesadas = []
mais_leves = []

while True: 
    nome = str(input("Digite o nome da pessoa: "))
    peso = float(input('Digite o peso da pessoa: '))
    sair = input("Digite 0 para sair ou 1 para continuar: ")

    
    if peso >= 100:
        mais_pesadas.append(nome)
        mais_pesadas.append(peso)
    else:
        mais_leves.append(nome)
        mais_leves.append(peso)
    if sair == "0":
        break
print("As pessoas mais pesadas são: ")
print(mais_pesadas)
print("As pessoas mais leves são: ")
print(mais_leves)