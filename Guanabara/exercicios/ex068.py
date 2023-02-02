from random import randint

count = 0
while True:
    jogada = randint(0, 10)
    num = str(input('par ou ímpar? [P/I]: ')).upper()

    if num == "P" and jogada % 2 == 0:
        print('Parabéns, você venceu!')
        count += 1
    elif num == "i":
        if num == 1:
            print('Parabéns, você venceu!')
            count += 1
        elif (num + 3) % 2 ==0:
            print('Parabéns, você venceu!')
            count += 1
    else:
        print(f'Você perdeu e ganhou {count} vezes seguidas')
