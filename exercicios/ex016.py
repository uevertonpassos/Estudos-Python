# Arredondando um número flutuante
from math import ceil, floor
numReal = float(input('Digite um número real: '))
print('A parte inteira de {} arredondada para cima é: {}! '.format(numReal, ceil(numReal)))
print('A parte inteira de {} arrendondada para baixo é: {}! '.format(numReal, floor(numReal)))
