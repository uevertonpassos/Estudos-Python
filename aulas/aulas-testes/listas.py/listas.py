'''lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)
lista_a.extend(lista_c)
print(lista_a)
'''
lista_nomes = ['Maria', 'Helena', 'Luiz']
contador = 0

for nome in lista_nomes:
    print(contador, nome)
    contador +=1

# posso usar enumerate também

lista_nomes = ['Maria', 'Helena', 'Luiz']

for nome in enumerate(lista_nomes):
    print(nome)