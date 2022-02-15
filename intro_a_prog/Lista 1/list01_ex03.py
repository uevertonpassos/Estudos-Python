import statistics
num1 = int(input('Digite o primeiro valor: '))
num2 = int (input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
media = (num1 + num2 + num3 + num4)/4
desv = [num1, num2, num3, num4]
print(f"A Média é {media} e o Desvio {statistics.stdev(desv):.2f} ")

