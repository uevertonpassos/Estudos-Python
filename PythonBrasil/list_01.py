#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 

count = 0
list_of_numbers = []

while count <= 5:
    number = int(input("Enter an integer value: "))
    list_of_numbers.append(number)
    count+=1
    
print("")
print("Thank you! This is the list of numbers: ")
print(list_of_numbers) 

