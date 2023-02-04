valor = int(input("Informe o valor a ser sacado: "))

cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

while True:
    if valor >= 50:
        cedulas_50 += 1
        valor -= 50
    elif valor >= 20:
        cedulas_20 += 1
        valor -= 20
    elif valor >= 10:
        cedulas_10 += 1
        valor -= 10
    else:
        cedulas_1 = valor
        break

print(f"{cedulas_50} cédulas de R$50")
print(f"{cedulas_20} cédulas de R$20")
print(f"{cedulas_10} cédulas de R$10")
print(f"{cedulas_1} cédulas de R$1")
