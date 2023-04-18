import tkinter as tk

def adicionar_palavra():
    global palavras, maior
    palavra = entrada_palavra.get()
    if palavra:
        palavras.append(palavra)
        if len(palavra) > len(maior):
            maior = palavra
        label_lista_palavras.config(text="Lista de palavras: " + str(palavras))
        label_palavra_mais_longa.config(text="Maior palavra: " + maior)
        entrada_palavra.delete(0, tk.END)

# Cria a janela principal
janela = tk.Tk()
janela.title("Palavras")

# Cria o rótulo para a entrada de palavras
label_entrada_palavra = tk.Label(janela, text="Digite uma palavra:")
label_entrada_palavra.pack()

# Cria a entrada de texto para adicionar palavras
entrada_palavra = tk.Entry(janela)
entrada_palavra.pack()

# Cria o botão para adicionar palavras
botao_adicionar_palavra = tk.Button(janela, text="Adicionar", command=adicionar_palavra)
botao_adicionar_palavra.pack()

# Cria o rótulo para a lista de palavras
label_lista_palavras = tk.Label(janela, text="Lista de palavras: ")
label_lista_palavras.pack()

# Cria o rótulo para a maior palavra
label_palavra_mais_longa = tk.Label(janela, text="Maior palavra: ")
label_palavra_mais_longa.pack()

# Define as variáveis para a lista de palavras e a maior palavra
palavras = []
maior = ""

# Executa o loop principal da aplicação
janela.mainloop()
