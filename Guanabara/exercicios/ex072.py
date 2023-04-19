

# Definindo a lista de números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input("Digite um número de 0 a 20: "))
while numero < 0 or numero > 20:
    numero = int(input("Digite um número de 0 a 20: "))
    
print(f'O número {numero} por extenso é: {numeros[numero]}\n')