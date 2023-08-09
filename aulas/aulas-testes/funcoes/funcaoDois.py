# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 

def soma(num1, num2, num3):
    somando = (num1 + num2 + num3)
    print(f"A soma entre os três valores é: {somando}")

numeroUm = int(input("Digite um valor: "))
numeroDois = int(input("Digite outro valor: "))
numeroTres = int(input("Digite o terceiro valor: ")) 
soma(numeroUm, numeroDois, numeroTres)



