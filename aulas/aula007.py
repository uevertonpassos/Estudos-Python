# Formatação de Strings

''' Existem alguns tipos de formatação de strings, entre eles:

'''

nome = "Ueverton"
idade = 25
# abaixo os exemplos
print(nome, 'tem', idade, 'anos!')
print(f'{nome} tem {idade} anos!')
print('{} tem {} anos!'.format(nome, idade))
# pode ser usarda de outra forma tbm
print('{n} tem {i} anos!'.format(n=nome, i=idade))