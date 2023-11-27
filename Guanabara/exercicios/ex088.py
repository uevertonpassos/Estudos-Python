# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

quantJogos = int(input("Digite a quantidade de jogos a fazer: "))
cont = 0
while True:
    if quantJogos <= 0:
        print("Por favor, digite um número válido maior que zero: ")

    else: 
        for jogo in range(1, quantJogos + 1):
            palpites = random.sample(range(1, 61),6)
            palpites.sort()
            cont += 1
            print(f"Jogo: {palpites}")
    if cont == quantJogos:
        break
    