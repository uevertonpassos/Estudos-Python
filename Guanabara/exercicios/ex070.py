'''   
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''


total = 0
caros = 0
produtos = {} #utilizei um dicionário para salvar o nome dos produtos e utilizei um min pra pegar o mais barato da mesma forma que usaria max para o mais caro

while True:
    produto = str(input("Digite o nome do produto: "))
    preço = float(input("Digite o preço do produto R$: "))
    produtos[produto] = preço
    registro = str(input("Deseja registrar outro produto? [S/N]: ")).upper().strip()[0]
    
    if registro == "S":
        total += preço
        if preço >=1000:
            caros+=1     
    else:
        total += preço
        print(f'O total a pagar será {total}')
        print(f"Temos {caros} itens acima de R$ 1000.00 reais")
        break
    
mais_barato = min(produtos, key=produtos.get)
print(f'o produto mais barato foi o :{mais_barato}')

        

