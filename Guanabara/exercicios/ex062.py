pri_termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = pri_termo
count = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count < total:
        print(f'{termo} --> ', end='')
        termo += razao
        count +=1
    print('pausa')
    mais = int(input("Digite quantos termos a mais você quer pesquisar:  "))
print(f'progressão finalizada com {total} termos')


   