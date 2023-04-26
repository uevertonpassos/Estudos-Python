lista = []

while True:
    confirm = input('Deseja adicionar um valor a lista? [S/N]: ').lower()
    if confirm == 's':
        numero = int(input('Digite um valor: '))
        lista.append(numero)
    else:
        print(f'Foram digitados {len(lista)} números')
        print(f'Aqui está a lista ordenada de forma decrescente {sorted(lista, reverse=True)}')
        #prestar atenção no método reverse
        if 5 in lista:
            print('O numero 5 foi colocado na lista')
        else:
            print('O número 5 não apareceu')
        
