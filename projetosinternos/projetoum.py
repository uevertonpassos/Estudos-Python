limite = int(input("Digite o limite: "))

for i in range(1, limite):
    atk = str(input('Deseja atacar? [S/N]: '))
    if atk in "Ss":
        print("Atacando")
    elif atk in "Nn":
        print('Não atacando')
    else:
        print('Entre com um valor válido')
        