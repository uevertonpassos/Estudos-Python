#classificando atletas
from datetime import date
anoAtual = date.today().year
anoDeNascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = anoAtual - anoDeNascimento
print(f'Esse atleta tem {idade} anos!')
if idade <= 9:
    print('Classificação MIRIM!')
elif idade <=14:
    print('Classificação INFANTIL')
elif idade <=19:
    print('Classificação JUNIOR')
elif idade <=25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
