num = int(input("Digite um valor: [999] para parar o programa: "))
soma = 0
while num < 999:
    soma +=num
    num = int(input("Digite um valor: [999] para parar o programa: "))
print(f'A soma de todos os numeros foi:{soma} ')