
valores = []
maior = 0
menor = 0
for n in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    if n == 0:
        maior = menor = valores[n]
    else:
        if valores[n] > maior:
            maior = valores[n]
        if valores[n]< menor:
            menor = valores[n]
    
    
        
print(f'a lista digitada foi: {valores}')
print(f'o maior numero foi : {maior} e apareceu na posição: {valores.index(maior)}')
print(f'o menor numero foi: {menor} e apareceu na posição: {valores.index(menor)}')
