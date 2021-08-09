def calculate():
    operation = input('''Por favor, digite 
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    Informequal você deseja utilizar: ''')
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    if operation == '+':
        print('{} + {} é igual a:'.format(num1, num2))
        print(num1 + num2)
    elif operation == '-':
        print('{} - {} é igual a:'.format(num1, num2))
        print(num1 - num2)
    elif operation == '*':
        print('{} * {} é igual a:'.format(num1, num2))
        print(num1 * num2)
    elif operation == '/':
        print('{} / {} é igual a:'.format(num1, num2))
        print(num1 / num2)
    else:
        print('Você não digitou uma operação válida!')
    
    again()

def again():
    calc_again = input('''Você deseja calcular novamente?
    Se sim, digite S, se não, digite N: ''')
    if calc_again == 'S':
        calculate()
    elif calc_again == 'N':
        print('Tudo bem, volte sempre!')
    else:
        again()
calculate()
