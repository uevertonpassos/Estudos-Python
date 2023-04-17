lista = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8, 9]

def calcular_media(lista):
    soma = sum(lista)
    quantidade = len(lista)
    media = soma / quantidade
    return media

resultado = calcular_media(lista)

print(resultado)

