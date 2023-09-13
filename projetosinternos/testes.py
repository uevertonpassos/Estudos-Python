lana = "GIRLFRIEND"
resultado = ""

for i, letra in enumerate(lana):
    resultado += letra * (i + 1)
    resultado += " "

# print(resultado)

# Criando uma variável organizando os caracteres por igualdade e ordem
organizado = ""
letters = set(resultado.replace(" ", ""))

# Manter a ordem das letras baseada em "GIRLFRIEND"
order = [letter for letter in lana if letter in letters]

for letter in order:
    count = resultado.count(letter)
    organizado += letter * count
    resultado = resultado.replace(letter, "", count)  # Remove as letras já adicionadas

print(organizado)
