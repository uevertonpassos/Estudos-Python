while True:
    frase = input('Digite a frase: ')


    tamanho_frase = len(frase)
    contador = 0
    compor = ''

    while contador < tamanho_frase:
        compor += frase[contador]
        contador += 1
        print(compor)
        