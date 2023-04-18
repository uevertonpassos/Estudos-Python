frase = "o rato roeu a roupa do rei de roma"
tamanho_da_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Digite a letra que quer subistituir: ')

while contador < tamanho_da_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
