from random import randint

count = 0
while count < 3:
    jogada = randint(0, 10)
    num = int(input('Digite um número: '))
    escolha = str(input('par ou ímpar? [P/I]: ')).upper()
    if (num + jogada) % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Ímpar"
    print("Você escolheu", num, "e a máquina escolheu", jogada, "Resultado:", resultado)
    if escolha == "P" and resultado == "Par":
        print("Parabéns você ganhou!")
    elif escolha == "I" and resultado == "Ímpar":
        print("Parabéns você ganhou!")
    else:
        print("Você perdeu!")
        count += 1
    if count == 3:
        print("Você atingiu o limite de tentativas. Fim de jogo.")
        break
