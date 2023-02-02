numTermos = int(input('Digite quantos termos a sequencia terá: '))
n1 = 0
n2 = 1
count = 0

while count < numTermos:
    print(f'{n1} -->', end=' ')
    fib = n1 + n2
    n1 = n2
    n2 = fib
    count +=1
print('FIM')
