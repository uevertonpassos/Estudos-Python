#Crie um programa que solicite ao usuário a entrada de dois números inteiros e exiba a soma desses números.

try:
    numUm = input("Digite um valor: ")
    numDois = input("Digite outro valor: ")
    soma = int(numUm) + int(numDois)
    print(f"a soma entre {numUm} e {numDois} vale: {soma}")

except:
    print("Você não digitou um valor numérico")
    