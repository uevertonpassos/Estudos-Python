# Crie uma função que aceite um número como argumento e verifique se ele é par ou ímpar, exibindo uma mensagem apropriada.

def EvenOdd(num):
    if num % 2== 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')

number = int(input('Digite um valor: '))
EvenOdd(number)