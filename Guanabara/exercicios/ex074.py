from random import randint

numeros_aleatorios = tuple(randint(0, 10) for _ in range(5))

print(f'Os números gerados foram: {numeros_aleatorios}')
print(f'O maior número é: {max(numeros_aleatorios)}')
print(f'O menor número é:{min(numeros_aleatorios)}')