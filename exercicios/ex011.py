# Desafio pintando paredes

# A = b * h

base = float(input('Digite o valor da base da parede: '))
altura = float(input('Digite o valor da altura da parede: '))
area = (base*altura)/2
print('Para pintar a parede você precisará de {} litros de tinta!'.format(area))
