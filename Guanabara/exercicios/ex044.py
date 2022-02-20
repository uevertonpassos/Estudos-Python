# simulador de loja // gerenciador de pagamentos

preço = float(input("Digite o valor a pagar R$: "))
descontoDez = preço - (preço*10/100)
descontoCinco = preço - (preço*5/100)
juros = preço + (preço*5/100)

print('''ESCOLHA A OPÇÃO DE PAGAMENTO!
[1] À vista em dinheiro / cheque 
[2] À vista no cartão
[3] Em 2x no cartão
[4] Em 3x ou mais no cartão''')

pagamento = int(input('Digite a opção de pagamento: '))
if pagamento == 1:
    print(f'Com o desconto o pagamento anteriormente de R$ {preço} agora será de R$: {descontoDez}')
elif pagamento ==2:
    print(f'Com o desconto o pagamento anteriormente de R$: {preço} agora será de R$: {descontoCinco}')
elif pagamento == 3:
    print(f'O pagamento continuará com o preço de R$: {preço} em duas parcelas de {preço/2} cada')
elif pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print(f'O pagamento que seria de  R$ {pagamento} com os júros passará a ser R$: {juros} em {parcelas} de {preço/parcelas:.2f}')
else:
    print('Você digitou uma opção errada, tente novamente!')
