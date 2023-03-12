# While com Else // treinando contadores e acumuladores

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    #if contador > 5:
        #break
    acumulador = acumulador + contador
    contador += 1
else:
    print("Cheguei no Else")

#  se eu não quebrar o laço, o contador e o acumulador continuam valendo até que o laço se torne falso e então pule para o else