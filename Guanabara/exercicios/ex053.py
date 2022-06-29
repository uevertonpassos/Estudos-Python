# Detector de palíndromo

frase = input('Digite a frase: ').strip().upper() # dividi e coloquei a frase em maíusculo para comparação
palavra = frase.split() # separei as palavras pelos espaços
junto = ''.join(palavra) # juntei todas as palavras para inverter
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palindromo!')