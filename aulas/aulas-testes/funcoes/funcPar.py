
#Escreva uma função que receba uma lista de números e retorne apenas os números pares.

lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_par = []

def verificar_par(lista):
    for numero in lista:
        if numero % 2 == 0:
            lista_par.append(numero)


verificar_par(lista)
print(f"os numeros pares foram {lista_par}")

