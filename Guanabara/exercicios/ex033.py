num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))
if num1 < num2 and num2 < num3:
    print(f"O maior número é {num3}")
    print(f"E o menor é o {num1} ")
elif num3 < num1 and num1 < num2:
    print(f"O maior numero é o {num2}")
    print(f"e o menor é o {num2}")
elif num2 < num1 and num3 < num1:
    print(f"O maior numero é o {num1}")
    print(f"e o menor é o {num2}")

