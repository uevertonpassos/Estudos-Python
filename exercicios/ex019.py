# Randomizando um aluno para apagar o quadro
from random import choice
alunoUm = input('Digite o nome do primeiro aluno: ')
alunoDois = input('Digite o nome do segundo aluno: ')
alunoTres = input('Digite o nome do terceiro aluno: ')
alunoQuatro = input('Digite o nome do quarto aluno: ')
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
print('O aluno escolhido foi: {} '.format(choice(lista)))