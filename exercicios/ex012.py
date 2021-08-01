# Calculando reajuste de 5% do produto
valor = float(input('Digite o valor atual do produto R$: '))
novoValor = valor - (valor*5/100)
print('O produto anteriormente custava R${}! Com o desconto, o novo preço será R${:.2f}'.format(valor, novoValor))

