import tkinter as tk
from tkinter import messagebox

def calcular_media(notas):
    return sum(notas) / len(notas)

def mostrar_boletim():
    texto_boletim.delete(1.0, tk.END)
    for aluno in boletim:
        nome_aluno, notas_aluno = aluno[0], aluno[1:]
        media_aluno = calcular_media(notas_aluno)
        texto_boletim.insert(tk.END, f"{nome_aluno}: Média = {media_aluno:.2f}\n")

def mostrar_notas_individualmente():
    nome_busca = entrada_nome.get()
    encontrado = False

    for aluno in boletim:
        if aluno[0] == nome_busca:
            encontrado = True
            notas_aluno = aluno[1:]
            messagebox.showinfo("Notas", f"Notas de {nome_busca}: {notas_aluno}")
            break

    if not encontrado:
        messagebox.showwarning("Aviso", f"Aluno {nome_busca} não encontrado.")

def adicionar_aluno():
    nome = entrada_nome_aluno.get()
    nota1 = float(entrada_nota1.get())
    nota2 = float(entrada_nota2.get())

    boletim.append([nome, nota1, nota2])
    messagebox.showinfo("Sucesso", f"Aluno {nome} adicionado ao boletim.")
    mostrar_boletim()

# Criar janela principal
janela = tk.Tk()
janela.title("Boletim Escolar")

# Configurar esquema de cores
janela.configure(bg='black')

# Variáveis para armazenar dados dos alunos
boletim = []

# Widgets
rotulo_nome_aluno = tk.Label(janela, text="Nome do Aluno:", bg='black', fg='white')
entrada_nome_aluno = tk.Entry(janela, bg='black', fg='white')

rotulo_nota1 = tk.Label(janela, text="Nota 1:", bg='black', fg='white')
entrada_nota1 = tk.Entry(janela, bg='black', fg='white')

rotulo_nota2 = tk.Label(janela, text="Nota 2:", bg='black', fg='white')
entrada_nota2 = tk.Entry(janela, bg='black', fg='white')

botao_adicionar = tk.Button(janela, text="Adicionar Aluno", command=adicionar_aluno, bg='blue', fg='white')

rotulo_nome = tk.Label(janela, text="Nome do Aluno para Consulta:", bg='black', fg='white')
entrada_nome = tk.Entry(janela, bg='black', fg='white')

botao_consultar = tk.Button(janela, text="Consultar Notas", command=mostrar_notas_individualmente, bg='blue', fg='white')

texto_boletim = tk.Text(janela, height=10, width=30, bg='black', fg='white')
texto_boletim.insert(tk.END, "Boletim:\n")

# Posicionamento dos widgets na grade
rotulo_nome_aluno.grid(row=0, column=0)
entrada_nome_aluno.grid(row=0, column=1)

rotulo_nota1.grid(row=1, column=0)
entrada_nota1.grid(row=1, column=1)

rotulo_nota2.grid(row=2, column=0)
entrada_nota2.grid(row=2, column=1)

botao_adicionar.grid(row=3, column=0, columnspan=2)

rotulo_nome.grid(row=4, column=0)
entrada_nome.grid(row=4, column=1)

botao_consultar.grid(row=5, column=0, columnspan=2)

texto_boletim.grid(row=6, column=0, columnspan=2)

# Loop principal da janela
janela.mainloop()
