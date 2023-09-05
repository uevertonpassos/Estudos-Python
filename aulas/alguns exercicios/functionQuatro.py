# rie uma função que receba dois números como entrada e exiba o maior deles.

def checagem(n1, n2):
    if n1 > n2:
        print(f'O número {n1} é o maior valor')
    elif n1 == n2:
        print(f'O número {n1} é igual ao {n2}')
    else: 
        print(f'o número {n2} é o maiorvalor ')

valorUm = int(input('Digite um valor: '))
valorDois = int(input('Digite outro valor: '))

checagem(valorUm, valorDois)


