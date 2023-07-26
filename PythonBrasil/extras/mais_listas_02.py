#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

medias_TOTAL = []
aprovados = []

for i in range(0, 10):
    notas = float(input("Digite a nota um: "))
    notas2 = float(input("Digite a nota dois: "))
    notas3 = float(input("Digite a nota três: "))
    notas4 = float(input("Digite a nota quatro: "))
    media = (notas + notas2 + notas3 + notas4)/4
    medias_TOTAL.append(media)
    if media >= 7.0:
        aprovados.append(media)

print("as medias são: ")
print(medias_TOTAL)
print('')
print(f"tivemos um total de {len(aprovados)} aprovados")


