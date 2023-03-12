# 2° exercício

# perguntar a hora e exibir respostas diferentes para dia, tarde e noite

horario = input("Digite uma hora entre 0 e 23: ")
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("O horário deve estar entre 0 e 23!")
    else:
        if horario <= 11:
            print("Bom dia!")
        elif horario <= 17:
            print("Boa tarde!")
        else:
            print('Boa noite!')