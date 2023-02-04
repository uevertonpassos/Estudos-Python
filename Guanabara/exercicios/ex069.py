from datetime import date

ano_atual = date.today().year
maiores = 0
mulheres_menores = 0
homens_cadastrados = 0

while True:
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        maiores += 1
    else:
        sexo = input("Digite o seu sexo (M/F): ").strip().upper()[0]
        while sexo not in ["M", "F"]:
            sexo = input("Por favor, digite M ou F para o sexo: ").strip().upper()[0]
        if sexo == "F" and idade <= 20:
            mulheres_menores += 1
        elif sexo == "M":
            homens_cadastrados += 1
    novo_cadastro = input("Deseja cadastrar mais alguém (S/N)? ").strip().upper()[0]
    if novo_cadastro != "S":
        break

print("=======================================")
print(f"{maiores} pessoas são maiores de idade")
print(f"Foram cadastrados {homens_cadastrados} homens")
print(f"Temos {mulheres_menores} mulheres com menos de vinte anos")
print("=======================================")
