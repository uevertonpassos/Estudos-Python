#Crie uma função que receba uma lista de palavras e retorne a palavra mais longa.

palavras = []
maior = ""

def palavraMaior():
    global maior
    while True:
        pergunta = input("Digite [S] para adicionar uma palavra nova ou [N] para sair: ").lower()
        if pergunta == "s":
            adicionar_palavra = input("Digite a palavra: ")
            palavras.append(adicionar_palavra)
            if len(adicionar_palavra) > len(maior):
                    maior = adicionar_palavra
        elif pergunta == "n":
            print("Saindo")
            return
        else:
            print("Digite algo válido")

palavraMaior()
print(f"Aqui está a lista das palavras: ")
print(palavras)
print(f"A maior palavra será: {maior}")
