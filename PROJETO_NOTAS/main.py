import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print(f"{nomeDoAluno}, {nota}, {nota2}, {nota3}")

texto = customtkinter.CTkLabel(janela, text = "Tabela de Notas")

nomeDoAluno = customtkinter.CTkEntry(janela, placeholder_text="Nome do Aluno")
nota = customtkinter.CTkEntry(janela, placeholder_text="Primeira nota")
nota2 = customtkinter.CTkEntry(janela, placeholder_text="Segunda nota")
nota3 = customtkinter.CTkEntry(janela, placeholder_text="Terceira nota  ") 
botao = customtkinter.CTkButton(janela, text="atribuir", command=clique)

texto.pack(padx=10, pady=10)
nomeDoAluno.pack(padx=10, pady=10)
nota.pack(padx=10, pady=10)
nota2.pack(padx=10, pady=10)
nota3.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

janela.mainloop()