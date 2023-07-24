#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

consoantes = []
vogais = ["a", "e", "i", "o", "u"]

for i in range(0,10):
    letra = str(input("Digite algo: "))
    if letra not in vogais:
        consoantes.append(letra)

print(f"teremos {len(consoantes)} consoantes")
print(consoantes)

#parei aqui?