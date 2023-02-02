from random import randint
from math import floor

resposta = 's'

while True:
    dado = int(input('Qual o tipo de dado? '))
    quantidaded = int(input('Quantos dados são? '))
    moda = int(input('Qual o seu modificador de ataque? '))
    vantagem = int(input('Qual o seu bonus de dano? '))
    margem = int(input('Qual sua margem para crítico? '))
    multiplicador = int(input('Qual o seu multiplicador de crítico? '))
    n = int(input('Quantas vezes quer testar? '))
    rold = randint(1, dado)
    totald = 0
    ataque = 0
    for t in range(1, n+1):
        rol = randint(1,20)
        if rol >= margem:
            for d in range(1,(quantidaded*multiplicador)+1):
                dano = randint(1, dado)
                totald += dano
        else:
            for d in range(1, quantidaded):
                dano = randint(1, dado)
                totald += dano
        ataque += rol
    print(f'A sua média de ataque é {floor((ataque/n)+moda)} A sua média de dano é {floor((totald/n)+vantagem)}')
    print('''
    
    ''')
    print('Ataque novamente...')


