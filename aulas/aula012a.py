#  Resolvendo exercícios propostos, aula 30 da udemy

# 1° Exercicio: pedir um input, informar se é par ou impar, e se não for numerico, avisar que não é

num = input("Digite um número: ")
if type(num) ==  str:
    print("não é um número!")
    num2 = input("Por favor digite um número: ")
    resto = int(num2) % 2
    if resto == 0: 
        print("Este número é Par!")
    else:
        print("Estu número é Ímpar")
else:
    ...

   


