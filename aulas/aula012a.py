#  Resolvendo exercícios propostos, aula 30 da udemy

# 1° Exercicio: pedir um input, informar se é par ou impar, e se não for numerico, avisar que não é

num = input("Digite um número: ")
if num.isdigit():
    if int(num) % 2 ==0:
        print("Par")
    else:
        print("Ímpar")
else:
    print("Entrada inválida")


   


