contador = 0
soma = 0
while True:
    num = int(input('Quer ver a traboada de qual valor?  '))
    if num <0:
            print('programa encerrado')
            break
    for tab in range(0, 11):
         print(f'{num} x {tab} = {num * tab}')
    print('')   
         
                