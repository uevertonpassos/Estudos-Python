def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ''
        for j in range(i):
            linha += str(i) + ' '
        print(linha)

n = int(input('Digite um número: '))
imprimir_padrao(n)