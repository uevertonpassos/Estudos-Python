#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz 3x3: ")
for linha in matriz:
    for valor in linha:
        print(f"({valor})", end=" ")
    print()
    
