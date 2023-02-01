contador = 0 #o contador vale 0

while True:
    n = int(input("Digite um valor: ")) 
    if n > 0:
        contador += n # soma o valor de N ao contador, a partir de agora o contador vale a soma do que você digitou + o antigo valor do contador
        print(contador)
    else:
        break
#o código vai repetir com o novo valor de contador
