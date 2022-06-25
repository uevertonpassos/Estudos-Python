#  Testando se um número é ou não primo!


num = int(input('Digite o número: '))
total = 0
for c in range(1, num + 1):
    if num % c ==0:
        total += 1
if total == 2:
    print(f'esse número é primo!')
else:
    print(f'esse número não é primo')