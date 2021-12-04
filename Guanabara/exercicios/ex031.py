passagem = float(input('Digite a distância em Km que irá viajar: '))
if passagem <= 200:
    print(f"A sua passagem custará R$:{passagem*0.50:.2f}")
else:
    print(f"A sua passagem custará R$:{passagem*0.45:.2f}")
