def sequencia(n):
    for i in range(1, n + 1):
        # Imprime os números i repetidas vezes na linha
        linha = ' '.join([str(i)] * i)
        print(linha)

try: 
    n = int(input("Digite um valor de N: "))
    sequencia(n)

except ValueError:
    print("Por favor digite um valor válido: ")

    