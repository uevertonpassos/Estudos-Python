from random import choice
from time import sleep
print('                                                                   ')
print('==//'*5)
print('INSIRA AS PERGUNTAS: ')
print('==//'*5)
print('                                                                   ')
sleep(1)
p1 = input('Digite a primeira pergunta: ')
r1 = input('Digite a resposta da primeira pergunta: ')
p2 = input('Digite a segunda pergunta: ')
r2 = input('Digite a resposta da segunda pergunta: ')
p3 =input('Digite a terceira pergunta: ')
r3 = input('Digite a resposta da terceira pergunta: ')
sleep(1)
perguntas = [p1, p2, p3]
print('                                                                   ')
print('=#='*10)
print('        QUESTIONÁRIO')
print('=#='*10)
sleep(1)
ready = input('Pressione enter quando quiser começar...')
sleep(1)
resposta1 = input('Qual a resposta para: {} = '.format(choice(perguntas)))
sleep(1)
print('Processando...')
sleep(1)
if resposta1 == r1:
    print('Parabéns! Sua resposta está correta!')
else:
    print('Você errou esta questão...')
resposta2 = input('Qual a resposta para: {} = '.format(choice(perguntas)))
sleep(1)
print('Processando...')
sleep(1)
if resposta2 == r2:
    print('Parabéns! Sua resposta está correta!')
else:
    print('Você errou esta questão...')
resposta3 = input('Qual a resposta para: {} = '.format(choice(perguntas)))
sleep(1)
print('Processando...')
sleep(1)
if resposta3 == r3:
    print('Muito bem! Você acertou esta questão!')
else:
    print('Infelizmente você errou esta questão...')
