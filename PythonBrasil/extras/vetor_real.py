#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 

vetor = []

for i in range(0,10):
    number = float(input("Digite um numero real: "))
    vetor.append(number)

print("Aqui estão os numeros na ordem inversa")
print(vetor[::-1])