#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 
notas = []

for i in range(0, 4):
    notinha = float(input("Digite uma nota: "))
    notas.append(notinha)
print(notas)
print(f"a média será: {sum(notas)/4}")