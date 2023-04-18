#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 


lista_inteira = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

list_par = []
list_impar = []

for i in range(20):
    numero = int(input("Digite um valor: "))

    if numero % 2 ==0:
        list_par.append(numero)
    else:
        list_impar.append(numero)

print(f"Números: {lista_inteira}")
print(f"Pares: {list_par}")
print(f"Ímpares: {list_impar}")




