speed = int(input("Digite a velocidade do carro: "))
if speed > 80:
    print(f"Você ultrapassou o limite de velocidade e será multado em R$:{7*(speed - 80)},00")
else:
    print("Parabéns, continue dirigindo com cuidado!")
