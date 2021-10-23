# testando formatações: 

num = 11
nome = "Ueverton"
print(f"{num:0>10}") #  preenchendo espaços à esquerda com zeros
print(f"{num:0<10}") #  preenchendo espaços à direita com zeros
print(f"{num:0^10}") #  colocando o número entre zeros

print(nome.ljust(20, "#")) #  justificado à esquerda
print(nome.rjust(20, "#")) #  justificado à direita
print(nome.lower()) #  tudo em minusculo
print(nome.upper()) #  tudo em maiúsculo

