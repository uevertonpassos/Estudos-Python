#Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade.

lista =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def inverter():
    print(lista[5:] + lista[0:5])
    return inverter

print(f"Invertendo a lista: {inverter()}")