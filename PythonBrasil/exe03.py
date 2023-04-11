#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.  
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'g']

consoantes = 0

lista_consoantes = []

for letra in letras:
    if letra not in ['a', 'e', 'i', 'o', 'u']:
        consoantes +=1
        lista_consoantes.append(letra)

print(f"Foram encontradas {consoantes} consoantes.")
print("As consoantes encontradas foram:")

for consoante in lista_consoantes:
    print(consoante)