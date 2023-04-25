lista_de_valores = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in lista_de_valores:
        print('Este valor ja está na lista, por favor digite outro')
    else:
        lista_de_valores.append(valor)
    pergunta = input("Deseja continuar? [S] ou [N]: ").upper()
    if pergunta != "S":
        print(f"A lista final é: {sorted(lista_de_valores)}")
        break