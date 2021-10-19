# 3° Exercicio

# Respostas diferentes para tamanho dos nomes

nome = input("Digite o seu nome: ")
if len(nome) <= 4:
    print("Seu nome é muito curto!")
elif len(nome) >= 5 and len(nome)<= 6:
    print("Seu nome é normal!")
elif len(nome) >= 6:
    print("Seu nome é muito grande!")
    

# ou

usuario = input("Digite o seu nome: ")
tamanho = len(usuario)
if tamanho <= 4:
    print("Seu nome é muuito curto!")
elif tamanho >= 5:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande! ")