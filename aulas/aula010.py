#  parando erros de transformações de strings para números

num1 = input("Digite um valor: ")
num2 = input("Digite outro valor: ")

if num1.isdigit and num2.isdigit:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Não é um numero")
    