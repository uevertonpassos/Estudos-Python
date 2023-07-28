# Lista para armazenar as pessoas (nome, peso)
pessoas = []

while True:
    nome = str(input("Digite o nome da pessoa: "))
    peso = float(input('Digite o peso da pessoa: '))
    sair = input("Digite 0 para sair ou 1 para continuar: ")
    
    pessoas.append((nome, peso))  # Armazenar nome e peso como uma tupla
    
    if sair == "0":
        break

# Contagem de pessoas cadastradas
num_pessoas = len(pessoas)

# Filtrar as pessoas mais pesadas e mais leves
mais_pesadas = [pessoa[0] for pessoa in pessoas if pessoa[1] >= 100]
mais_leves = [pessoa[0] for pessoa in pessoas if pessoa[1] < 100]

print(f"Foram cadastradas {num_pessoas} pessoas")
print("As pessoas mais pesadas são: ")
print(mais_pesadas)
print("As pessoas mais leves são: ")
print(mais_leves)
