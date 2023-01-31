# joga com o usuário até que ele acerte o número pseudo aleatório que o computador "pensou"

from random import randint

vezes = 1
while True:
    pensa = randint(1, 10)
    num = int(input("Digite um número entre 1 e 10: "))
    if num == pensa:
        print(f"Acertou! pensei mesmo em {num}")
        print(f"você precisou de {vezes} tentativas")
        break
    else:
        print("Errou, tente novamente")
        vezes += 1

