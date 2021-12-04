salario = float(input("Digite o valor atual do salário: "))
if salario >= 1250:
    print(f"O seu novo salário é R$: {salario+(salario*10/100):.2f}")
else:
    print(f"O seu novo salário é R$: {salario+(salario*15/100):.2f}")
