'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido.

'''


for aluno  in range(0, 9999):
    nota = float(input('Digite a nota: '))
    if nota > 10:
        print('Nota inválida, digite novamente!')
    elif nota <= 10:
        print('Nota cadastrada com sucesso')
        break
