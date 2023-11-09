# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Lista composta para armazenar nome e notas de cada aluno
boletim = []

# Preencher a lista composta com dados dos alunos
for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Adicionar dados à lista composta
    boletim.append([nome, nota1, nota2])

# Mostrar boletim com média de cada aluno
print("\nBoletim:")
for aluno in boletim:
    nome_aluno = aluno[0]
    notas_aluno = aluno[1:]
    media_aluno = sum(notas_aluno) / len(notas_aluno)
    
    print(f"{nome_aluno}: Média = {media_aluno}")

# Permitir que o usuário visualize as notas de cada aluno individualmente
while True:
    escolha = input("\nDeseja ver as notas de algum aluno individualmente? (S/N): ").upper()

    if escolha == 'S':
        nome_busca = input("Digite o nome do aluno: ")

        # Procurar o aluno na lista composta
        encontrado = False
        for aluno in boletim:
            if aluno[0] == nome_busca:
                encontrado = True
                print(f"\nNotas de {nome_busca}: {aluno[1:]}")
                break

        if not encontrado:
            print(f"Aluno {nome_busca} não encontrado.")

    elif escolha == 'N':
        break
    else:
        print("Opção inválida. Por favor, digite S ou N.")
        
