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

            for i in palavras:
                if len(adicionar_palavra) > len(maior):
                    maior = adicionar_palavra
        elif pergunta == "n":
            print("Saindo")
            return
        else:
            print("Digite algo válido")
            return

palavraMaior()
print(f"Aqui está a lista das palavras: ")
print(palavras)
print("")
print(f"A maior palavra será: {maior}")
