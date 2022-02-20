# jogo de pedra papel e tesoura
from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('=#'*10)
print('''Digite a sua escolha
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('=#'*10)
sleep(1)
jogador = int(input('Digite a sua escolha: '))
if computador == 0:
    if jogador == 0:
        print(f'O computador escolheu {itens[computador]}')
        print('Empate')
    elif jogador ==1:
        print(f'O computador escolheu {itens[computador]}')
        print('Jogador vence!')
    elif jogador ==2:
        print(f'O computador escolheu {itens[computador]}')
        print('Comptador vence!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: 
    if jogador == 0:
        print(f'O computador escolheu {itens[computador]}')
        print('Computador vence!')
    elif jogador == 1:
        print(f'O computador escolheu {itens[computador]}')
        print('Empate')
    elif jogador == 2:
        print(f'O computador escolheu {itens[computador]}')
        print('Jogador vence!')
elif computador ==2:
    if jogador == 0:
        print(f'O computador escolheu {itens[computador]}')
        print('Computador vence!')
    elif jogador == 1:
        print(f'O computador escolheu {itens[computador]}')
        print('Jogador vence!')
    elif jogador == 2:
        print(f'O computador escolheu {itens[computador]}')
        print('Empate!')
else:
    print('Jogada inválida!')
