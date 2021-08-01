# mais porcentagem

sal = float(input('Digite o salário: '))
preçoDesc = sal+(sal*20/100)
#desc = sal - preçoDesc
print('O preço original do produto era de R${} e você recebeu o desconto de R${} e o preço final será de R${} '.format(sal, sal-preçoDesc, preçoDesc))
