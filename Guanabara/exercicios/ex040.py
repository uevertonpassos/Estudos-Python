# verificando se o aluno está ou não aprovado

notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))
média = (notaUm + notaDois)/2
if média >=7:
    print(f'Parabéns você foi aprovado e a sua média foi: {média}!')
elif média < 5:
    print(f'Você foi reprovado e a sua média foi: {média}!')
else:
    print(f'Você está em recuperação e a sua média foi: {média}!')
