while True:
    frase = input('Digite a frase: ')

    tamanho_frase = len(frase)
    contador = 0
    compor = ''

    while contador < tamanho_frase:
        compor += frase[contador]
        contador += 1
        print(compor)

    for i in range(len(frase), 0, -1):
        print(frase[0:i])
    
    # Monta o COMPOR e o DECOMPOR
        