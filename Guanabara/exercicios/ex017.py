# Descobrindo a a Hipotenusa de um triângulo retângulo
from math import hypot

oCat = int(input('Digite o valor do cateto oposto do triângulo: '))
aCat = int(input('Digite o valor do cateto adjacente do triângulo: '))
print('O valor da hipotenusa do triângulo é de {:.2f}! '.format(hypot(oCat, aCat)))
