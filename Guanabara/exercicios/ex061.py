pri_termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = pri_termo
count = 0

while count < 11:
    print(f'{termo} --> ', end='')
    termo += razao
    count +=1
   