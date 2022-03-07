nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 3:
    print('reprovado sem direito a final')
elif media < 7:
    print('reprovado mas com direito a final')
else:
    print('Aprovado')
    