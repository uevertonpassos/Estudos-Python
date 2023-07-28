#faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista, No final mostre:

# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com pessoas mais leves.

pessoas = []

while True:
    nome = str(input("Digite o nome da pessoa: "))
    peso = float(input('Digite o peso da pessoa: '))
    sair = input("Digite 0 para sair ou 1 para continuar: ")
    
    pessoas.append((nome, peso))  
    
    if sair == "0":
        break


num_pessoas = len(pessoas)


mais_pesadas = [pessoa[0] for pessoa in pessoas if pessoa[1] >= 100]
mais_leves = [pessoa[0] for pessoa in pessoas if pessoa[1] < 100]

print(f"Foram cadastradas {num_pessoas} pessoas")
print("As pessoas mais pesadas são: ")
print(mais_pesadas)
print("As pessoas mais leves são: ")
print(mais_leves)
