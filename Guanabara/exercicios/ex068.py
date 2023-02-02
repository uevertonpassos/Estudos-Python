from random import randint

count = 0
while True:
    jogada = randint(0, 10)
    escolha = str(input('par ou ímpar? [P/I]: ')).upper()
    num = int(input('Digite sua jogada: '))
    calc = num + jogada 
    if escolha == "P" and calc % 2 == 0:
        print(f'Parabéns, você venceu! você jogou: {num} e o computador jogou: {jogada}')
        count += 1
    elif escolha == "I" and calc % 2 == 1:
        print(f'Parabéns, você venceu! você jogou: {num} e o computador jogou: {jogada}')
        count += 1
    else:
        print(f'Você perdeu! você jogou: {num} e o computador jogou: {jogada}')
        break

print(f'Fim de jogo! você jogou {count} vezes')
