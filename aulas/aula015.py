# Laço WHILE
#  While é usado para repetição, quer dizer que "enquanto" alguma coisa for x, repita esta ação, exemplo: 

x = 0
while x < 10:
    print(x)
    x = x + 1
print("Acabou aqui")

# Enquanto x for menor que 10, o programa irá rodar a contagem, quando for igual ou menor, vai exibir o ultimo print pulando o laço
#  Pode usar  a palavra "continue" para pular para proxima parte do laço, exemplo:

y = 0
while y < 10:
    continue
    print(y)
    y = y + 1
print("Acabou aqui: ")

# O código só irá executar até a linha 17 e pular direto para a 21
#  Também pode-se usar a palavra "break" para encerrar o loop do while, exemplo:

b = 0
while b < 10:
    if b == 3:
        b = b + 1
        break
    print (b)
    b = b + 1
print("acabou aqui")

# o while será quebrado assi mque o valor de b for igual a 3 e pulará direto para o print 



    