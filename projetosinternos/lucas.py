n1 = float(input('Digite o 1o numero:'))
n2 = float(input('Digite o 2o numero:'))
op = 0

while op != 5:
    print('''Digite o que deseja:
                        [1] - SOMA
                        [2] - MULTIPLICAÇÃO 
                        [3] - MAIOR
                        [4] - NOVOS NUMEROS
                        [5] - FINALIZAR''')
    op = input('Digite a opção que deseja: ')
    if op == "1":
        SOMA = n1 + n2
        print('1- SOMA')
        print(f'Resultado da soma = {SOMA} ')

    elif op == 2:
        produto = n1 * n2
        print('2- MULTIPLICAÇÃO')
        print(f'Produto da multiplicação = {produto}')

    elif op == 3:
        print('3- MAIOR')
        if n1 > n2:
            print(f'O maior é: {n1}')
        elif n2 > n1:
            print(f'O maior é: {n2}')
        else:
            print('Os numeros são iguais!!')
    if op == 5:
        print('Você finalizou...')
        break