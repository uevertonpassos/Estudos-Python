par = []
impar = []


for i in range(0, 20):
    numero = int(input("Digite um valor: "))
    if numero % 2 ==0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Os números pares são: ")
print(par)
print('')
print(f"Os números ímpares são: ")
print(impar)

