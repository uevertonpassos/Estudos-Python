# iterando strings com while

frase = "o rato roeu a roupa do rei de roma"
tamanho_da_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_da_frase:   # enquanto o contador for menor que o tamanho da frase (34) o laço pemanece
    nova_string += frase[contador]   # a sting vazia está sendo concatenada, fazendo uma letra da frase ser adicionada toda vez que o laço sofre uma adição de + 1
    print(nova_string)  # mostrando a nova forma ja concatenada
    contador += 1    # adicionando + 1 ao contador para que seja adicionado também no laço while

