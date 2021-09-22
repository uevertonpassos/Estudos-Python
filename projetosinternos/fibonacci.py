numTermos = int(input("Quantos termos terá a sequência? "))

n1, n2 = 0, 1
contador = 0

if numTermos <= 0:
   print("Por favor, insira um número inteiro positivo")
elif numTermos == 1:
   print("A sequencia de Fibonacci com: {} termos".format(numTermos))
   print(n1)

else:
   print(" A sequência de Fibonacci:")
   while contador < numTermos:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       contador += 1

