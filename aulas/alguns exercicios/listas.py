lista = [10, 20, 30, 40]

#mudando valor da lista pelo índice
lista[2] = 300
print(lista)

#apagando o último elemento da lista
lista.pop()
print(lista)

#adicionando um elemento ao final da lista
lista.append(3000)
print(lista)

#deletando indices da lista
del lista[2]
print(lista)

#inserindo valores na lista, primeiro passsar o indice, depois o que usar para substituição
lista.insert(0, 22)
print(lista)

#limpando a lista
lista.clear()
print(lista)
