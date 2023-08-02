# Escreva uma função que receba uma lista de números inteiros e retorne a soma de todos os elementos.

import math
soma = []

while True:

    number = int(input("Digite um valor: "))

    print("DIGITE 00 PARA PARAR O PROGRAMA")
    soma.append(number)

    if number == 00:
        break

resultado = sum(soma)
print(f'A soma de todos os numeros da lista é: {resultado}')


