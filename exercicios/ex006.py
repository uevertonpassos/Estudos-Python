# Dobro, Triplo e Raíz quadrada de um número

import math
num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
rq = math.sqrt(num)
print('O dobro de {} é: {}, e o seu triplo é: {}, já raiz quadrada é: {:.2f} '.format(num, dob, tri, rq))
# :.2f é formatação para duas casas decimais