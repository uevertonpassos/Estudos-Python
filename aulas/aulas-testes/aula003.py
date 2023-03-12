'''COMANDO PRINT'''

# Tentando separar os numeros de um cpf corretamente
# cpf: 824.176.070-18

# Como eu acho que é:
print('O cpf correto é:','824', '176', '070', '18',  sep='.')

# Tentando fazer do meu jeito
print('O cpf correto é: 824{}176{}070{}18'.format('.','.', '-'))

# Resposta correta
print('O cpf correto é:','824', '176', '070',  sep='.', end='-')
print('18')
print("Perfeito!")