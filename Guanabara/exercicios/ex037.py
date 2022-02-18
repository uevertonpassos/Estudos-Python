# convertendo números em Binário, Octal e Hexadecimal

num = int(input("Digite um número para ser convertido: "))
print('''Escolha a opção de conversão!
[1] Para converter para BINÁRIO
[2] Para converter para OCTAL
[3] Para converter para HEXADECIMAL
''')
print('')
opção = int(input("Digite a sua escolha: "))
if opção == 1:
    print(f"O número {num} convertido em BINÁRIO é igual a: {bin(num)[2:]}")
elif opção ==2:
    print(f"O número {num} convertido para OCTAL é igual a: {oct(num)[2:]}")
elif opção ==3:
    print(f"O número {num} convertido para HEXADECIMAL é igual a: {hex(num)[2:]}")
else:
    print("Esta não é uma opção válida, tente novamente!")
