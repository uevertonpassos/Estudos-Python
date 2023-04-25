
valores = []
maior = 0
menor = 999
for n in range(0, 5):
    numero = int(input("Digite um valor: "))
    if numero >= maior:
        maior = numero
    elif numero <= menor:
        menor = numero
    valores.append(numero,)
    
    
        
print(f'a lista digitada foi: {valores}')
print(f'o maior numero foi : {maior} e apareceu na posição: {valores.index(maior)}')
print(f'o menor numero foi: {menor} e apareceu na posição: {valores.index(menor)}')
