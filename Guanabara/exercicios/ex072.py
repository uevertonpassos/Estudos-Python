

# Definindo a lista de números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input("Digite um número de 0 a 20: "))
    if  0 <= numero <=20:
        break
    print('tente novamente')
        
    
print(f'O número {numero} por extenso é: {numeros[numero]}\n')