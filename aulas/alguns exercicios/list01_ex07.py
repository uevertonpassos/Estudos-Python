from math import hypot

ad_cat = int(input('Digite o cateto adjacente: '))
op_cat = int(input('Digite o cateto oposto: '))
print(f'o valor da Hipotenusa será de {hypot(ad_cat, op_cat):.0f}')
