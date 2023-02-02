
while True:
    numUm = float(input("Digite o primeiro valor: "))
    numDois = float(input("Digite o segundo valor: "))
    soma = numUm + numDois
    multi= numUm * numDois

    print('''
    ==//====//====//====//====//==
    Escolha a operação a seguir: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos número
    [5] Sair do programa
    ==//====//====//====//====//==
    ''')
    resposta  = input("Digite a sua escolha: ")
    if resposta == "1":
        print(f"A soma entre {numUm} e {numDois} é {soma}")
        print('')
    elif resposta == "2":
        print(f"A multiplicação entre {numUm} e {numDois} é {multi}")
        print('')
    elif resposta == "3":
        if numUm > numDois:
            print(f"o maior valor é o {numUm}")
            print('')
        else:
            print(f"o maior valor é o {numDois}")
            print('')
    elif resposta == "4":
        print("Certo, entre com valores novos ")
        print('')
    elif resposta == "5":
        print("Fim do programa, volte sempre!")
        break
    


