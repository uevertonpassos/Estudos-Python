#Crie uma função que aceite dois números como argumentos e exiba sua soma.

def soma(n1, n2):
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é: {soma}')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma(n1, n2)