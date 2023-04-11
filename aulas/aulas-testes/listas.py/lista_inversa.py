#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 

count = 0
list_of_nembers = []

while count <=9:
    numbers = int(input("Digite um valor: "))
    list_of_nembers.append(numbers)
    count +=1
print('')
print("Aqui estão os numeros digitados em ordem inversa: ")
print(list_of_nembers[::-1])
