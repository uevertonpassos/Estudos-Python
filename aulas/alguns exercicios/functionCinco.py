#  Desenvolva uma função que aceite uma string como argumento e exiba seu comprimento.

def comprimento(frase):
    tamanho = len(frase)
    print(f'o tamanho da String digitada é: {tamanho} caracteres')

fraseDigitada = input('Digite o que deseja contar: ')
comprimento(fraseDigitada)