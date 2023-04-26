lista = []

for i in range(5):
    valor = int(input('Digite um valor: '))
    if i == 0:
        lista.append(valor)
    else:
        posicao = 0
        while posicao < len(lista) and valor > lista[posicao]:
            posicao += 1
        lista.insert(posicao, valor)

print('A lista ordenada é:', lista)
