
import os
while True:   
    print( '''CALCULADORA!

    <ESCOLHA A SUA OPERAÇÃO>

    Digite a operação que deseja realizar:
    [1] Adição
    [2] Subtração   
    [3] Multiplicação
    [4] Divisão
    ''')
  
    # Aqui se inicia o bloco de adição

    escolha = float(input("Digite a sua opção: "))
    if escolha == 1:
        valores = int(input("Digite a quantidade de valores: "))
        adicao = 0

        for jogadas in range(0, valores):
            num = float(input("Digite o valor: "))
            adicao+=num
        print(f"a soma de todos os valores foi: {adicao}")
        print("")
        print("")
        Jogar_novamente = input("Deseja realizar outra operação? [S/N]: ").lower()
        if Jogar_novamente == "s":
            pass
        else:
            print("Calculadora encerrada")
            break

    # Aqui se inicia o bloco de subtração

    if escolha == 2:
        valores = int(input("Digite a quantidade de valores: "))
        subtracao = float(input("Digite o valor inicial: "))
        for jogadas in range(0, valores):
            num = float(input("Digite o valor: "))
            subtracao-=num
        print(f"A subtração dos valores vale: {subtracao}")
        print("")
        print("")
        Jogar_novamente = input("Deseja realizar outra operação? [S/N]: ").lower()
        if Jogar_novamente == "s":
            pass
        else:
            print("Calculadora encerrada")


    # Aqui se inicia o bloco de multiplicação

    if escolha == 3:
        valores = int(input("Digite a quantidade de valores: "))
        multiplicacao = 1
        for jogadas in range(0, valores):
            num = float(input("Digite o valor: "))
            multiplicacao *= num
        print(f"a multiplicação dos valores foi: {multiplicacao}")
        print("")
        print("")
        Jogar_novamente = input("Deseja realizar outra operação? [S/N]").lower()
        if Jogar_novamente == "s":
            pass
        else:
            print("Calculadora encerrada")
            break
    
    # Aqui se inicia o bloco de multiplicação

    if escolha == 4:
        valores = int(input("Digite a quantidade de valores: "))
        divisao = float(input("Digite o primeiro valor: "))
        for jogadas in range(0, valores):
            num = float(input("Digite o valor: "))
            divisao /= num
        print(f"a divisão dos valores sera: {divisao:.2f}")
        print("")
        print("")
        Jogar_novamente = input("Deseja realizar outra operação? [S/N]: ").lower()
        if Jogar_novamente == "s":
            pass
        else:
            print("Calculadora encerrada")
            break






