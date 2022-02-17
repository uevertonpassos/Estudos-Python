valorCasa = float(input("Digite o valor da casa: "))
salarioComprador = float(input("Digite o salário do comprador: "))
anosAPagar = int(input("Digite em quantos anos pretende pagar: "))

porc = salarioComprador*30/100
meses = anosAPagar*12
if (valorCasa / meses) < porc:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")
    