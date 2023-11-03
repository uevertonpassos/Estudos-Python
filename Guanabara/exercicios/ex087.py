'''
Aprimore o desafio anterior,mostrando final:                                                    A) A soma de todos os valores pares digitados.                                                                                      B) A soma dos valores da terceira coluna.                                                                                         C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição ({i+1}), ({j+1}): "))

soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = matriz[1][0]

for i in range(3):
    for j in range(3):
        if matriz[i][j] %2 ==0:
            soma_pares += matriz[i][j]
        if j  == 2:
            soma_terceira_coluna += matriz[i][j]
        if  i ==1 and matriz [i][j] > maior_segunda_linha:
            maior_segunda_linha = matriz [i][j]

print(f"A soma de todos os valores pares digitados: {soma_pares}")
print(f"A soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f" O maior valor da segunda linha: {maior_segunda_linha}")

