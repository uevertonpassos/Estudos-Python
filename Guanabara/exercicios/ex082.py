lista_inteira = []
lista_par = []
lista_impar = []

while True:
    numero = int(input('Digite um valor: '))
    lista_inteira.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    continua = input('Deseja continuar? [S/N]: ').upper()
    if continua == 'S':
        continue
    else:
        break
print('A lista inteira de numeros digitados é: ')
print(sorted(lista_inteira))
print('A lista de valores pares digitados é: ')
print(sorted(lista_par))
print('A lista de valores ímpares é: ')
print(sorted(lista_impar))
