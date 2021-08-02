# Tirando o Seno, Cosseno e Tangente de um ângulo
from math import sin, cos, tan, radians
ang = int(input('Digite o ângulo: '))
print('O seno de {} é: {:.2f}, o cosseno é: {:.2f} e a sua tangente é: {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))

