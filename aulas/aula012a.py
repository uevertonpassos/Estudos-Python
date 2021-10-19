#  Resolvendo exercícios propostos, aula 30 da udemy

# 1° Exercicio: pedir um input, informar se é par ou impar, e se não for numerico, avisar que não é

num = input("Digite um número: ")
if num.isdigit():
    if int(num) % 2 ==0:
        print(f"O número {num} é Par!")
    else:
        print(f"O número {num} Ímpar")
else:
    print("Entrada inválida")


# ou

num_usuario = input("Digite um número: ")

if not num_usuario.isdigit():
    print("Isso não é um número!")
else:
    num_usuario = int(num_usuario)
    if not num_usuario % 2 == 0:
        print(f"O número {num_usuario} é Ímpar!")
    else:
        print(f"O número {num_usuario} é Par!")