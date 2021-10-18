# 2° exercício

# perguntar a hora e exibir respostas diferentes para dia, tarde e noite

hora = int(input("Digite que horas são: "))
if hora >= 0 and hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora<=17:
    print ("Boa tarde!")
elif hora >= 18 and hora <= 23:
    print("Boa noite!")
else:
    print("Não é uma hora válida!")
