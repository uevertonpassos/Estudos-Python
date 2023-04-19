

# Definindo a lista de números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

try:
    while True:
        numero = int(input("Digite um número de 0 a 20: "))

        print(f'O número {numero} por extenso é: {numeros[numero]}\n')

except:
    print("Digite algo válido\n")
    while True:
        numero = int(input("Digite um número de 0 a 20: "))

        print(f'O número {numero} por extenso é {numeros[numero]}')
