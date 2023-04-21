minha_tupla = ()
lista_par = ()

for i in range(0, 4):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        lista_par+=(numero,)
    minha_tupla += (numero,)


print('')
print('')
print(f'O número 9 apareceu {minha_tupla.count(9)} vezes')
if 3 in minha_tupla:
    print(f'O primeiro número 3 apareceu em {minha_tupla.index(3)}')
else:
    print('O valor  3 não apareceu em nenhuma posição')
print(f'Numeros pares: {lista_par}')

