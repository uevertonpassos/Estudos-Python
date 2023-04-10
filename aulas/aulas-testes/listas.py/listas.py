lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)
lista_a.extend(lista_c)
print(lista_a)

lista_nomes = ['Maria', 'Passos']

for nome in lista_nomes:
    print(nome, " é um otário")
