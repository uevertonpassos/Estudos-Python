# Escolhendo uma ordem de apresentação
from random import shuffle
alunoUm = input('Digite o nome do primeiro aluno: ')
alunoDois = input('Digite o nome do segundo aluno: ')
alunoTres = input('Digite o nome do terceiro aluno: ')
alunoQuatro = input('Digite o nome do quarto aluno: ')
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
shuffle(lista)
print('O aluno escolhido foi: {} '.format(lista))
