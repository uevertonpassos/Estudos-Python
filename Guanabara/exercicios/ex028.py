from random import randint

pensa = randint(0, 5)
num = int(input("De 0 a 5 em que número você acha que eu estou pensando: "))
if num == pensa:
    print('parabéns! vc acertou')
else:
    print('você errou, meu querido')
