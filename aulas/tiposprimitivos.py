# int - para números inteiros ex: 7, -4, 0, 9875
# float - para números flutuantes ex: 4.5, 0.076, -15.645, 7.0
# bool - para números booleanos ex: True, False
# str - para strings (ja vem como padrão) ex: tudo que estiver entre aspas "7.4", '74'

# Exercício de verificações usando print

# String: nome
print('Ueverton', type('Ueverton'))
# Idade: int
print(25, type(25))
print('25', type(int('25'))) # transformando str em int
print(25.0, type(int(25.0))) # transformando float em int
# Altura: float
print(1.63, type(1.63))
print('1.63', type(float('1.63')))# transformando str em float
# É maior de idade: bool
print(25, 25 > 18) # testando se é ou não verdadeiro que o numero é maior(TRUE)
