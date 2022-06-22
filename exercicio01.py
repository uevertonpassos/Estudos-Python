numeroUm = int(input('Digite o número inicial: '))
numeroDois = int(input('Digite onde parar: '))
passo = int(input('Digite de quanto em quando é para pular: '))
for c in range(numeroUm, numeroDois + 1, passo):
    print(c)
print('Acabou')

