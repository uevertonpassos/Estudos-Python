lista_de_notas = []
count = 0

while count <=3:
    nota = float(input("Digite a nota: "))
    lista_de_notas.append(nota)
    count +=1 

print(f"as notas foram: {lista_de_notas}")
print("")
soma = sum(lista_de_notas)
print(f"A média do aluno será: {soma/4}")
