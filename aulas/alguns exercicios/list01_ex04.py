graus_celcius = float(input('Digite a temperatura em Celcius: '))
fahrenheit = 9 * graus_celcius/5+32
kelvin = graus_celcius - 32 / 1.8 + 273
ranquine = graus_celcius * 9/5 + 491,67
reamur = graus_celcius * 4/5

print('')
esc = input('Digite [F]ahrenheit, [K]elvin, [RA]nquine, [RE]amur: ')
if esc == "F":
    print(f'O valor convertido de Celsius para Fahrenheit é: {fahrenheit}°')
elif esc == "K":
    print(f'O valor convertido  de Celcius para Kelvin é: {kelvin}°')
elif esc == "RA":
    print(f'O valor convertido de Celcius para Ranquine é {ranquine}°')
elif esc == "RE":
    print(f'O valor convertido de Celcius para Réamur é: {reamur}°')
else:
    print('Você sabe o que ta fazendo?')

