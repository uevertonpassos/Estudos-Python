#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
par = []
impar = []


for i in range(0, 20):
    numero = int(input("Digite um valor: "))
    if numero % 2 ==0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Os números pares são: ")
print(par)
print('')
print(f"Os números ímpares são: ")
print(impar)


