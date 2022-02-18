# Comparando números

numUm = int(input('Digite um número: '))
numDois = int(input('Digite outro número: '))
if numUm > numDois:
    print(f'O número {numUm} é o maior que {numDois}')
elif numUm < numDois:
    print(f'O numero {numDois} é maior que {numUm}')
else:
    print('Os dois números são iguais')
