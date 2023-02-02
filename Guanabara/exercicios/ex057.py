'''while True:
    sexo = input("Digite o seu sexo: ").upper()
    if sexo == "M":
        print("Perfeito")
        break
    elif sexo == "F":
        print("Perfeito")
        break
    else:
        print("Dados inválidos, digite o seu sexo: ")'''    

        #Acima a minha primeira solução
        

sexo = input("Digite o seu sexo [F/M]: ").upper()

while sexo not in "MmFf":
    sexo = input("Sexo inválido, digite novamente seu sexo: ")
print("Sexo registrado com sucesso")