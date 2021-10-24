while True:
    print()
    num1 = input("Digite um valor: ")
    operador = input("Digite um operador: ")
    num2 = input("Digite outro valor: ")

    if not num1.isnumeric() or not num2.isnumeric():
        print("Você precisa digitar um número!")
        continue 
    num1 = int(num1)
    num2 = int(num2)

    if operador == "+":
        print(f"O resultado da soma é: {num1 + num2} ")
    elif operador == "-":
        print(f"O resultado da subtração é: {num1 - num2}")
    elif operador == "/":
        print(f"O resultado da divisão é: {num1 / num2}")
    elif operador == "*":
        print(f"O resultado da multiplicação é: {num1 * num2}")
    else:
        print("Operador inválido!")
    
    sair = input("Você deseja sair? [s]im ou [n]ão: ")  
    if sair == "s":
        break