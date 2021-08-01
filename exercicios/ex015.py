# Calculando aluguel de carro

dias = int(input('Digite a quantidade de dias alugados: '))
dist = float(input('Digite a quantidade de Km percorridos: '))   #  dist quer dizer distância
aluguel = dias * 60
km = dist * 0.15
print('O total a pagar em reais pelo aluguel do carro é de R${:.2f} '.format(aluguel+km))
