from datetime import date
atual = date.today().year
anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
ano = atual - anoDeNascimento
if ano < 18:
    print(f"Ainda faltam {18-(ano )} ano(s) para o seu alistamento")
elif ano == 18:
    print('Você está na idade certa para se alistar!')
else:
    print(f'Você já passou da idade correta para se alistar, deveria ter feito isso a {ano-  18} ano(s)')
