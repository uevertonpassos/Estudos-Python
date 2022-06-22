elemento  = int(input('Digite o elemento da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = elemento + (10 -1) * razao

for c in range(elemento, decimo + razao, razao):
	print(c, end = ' - ')
print('acabou!')