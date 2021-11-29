# iterando strings com while

frase = "o rato roeu a roupa do rei de roma"
tamanho_da_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_da_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
