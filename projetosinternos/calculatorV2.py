
from time import sleep
while True:   
    print( '''CALCULADORA!

    <ESCOLHA A SUA OPERAÇÃO>

    Digite a operação que deseja realizar:
    [1] Adição
    [2] Subtração   
    [3] Multiplicação
    [4] Divisão
    ''')
  
    escolha = int(input("Digite a sua opção: "))
    if escolha == 1:
        valores = int(input("Digite a quantidade de valores: "))
        adicao = 0

        for jogadas in range(0, valores):
            num = int(input("Digite o valor: "))
            adicao+=num
        print(f"a soma de todos os valores foi: {adicao}")
        print("")
        print("")
        Jogar_novamente = input("Deseja realizar outra operação? [S/N]")


