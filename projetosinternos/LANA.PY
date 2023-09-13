lana = "GIRLFRIEND"
resultado = ""

for i, letra in enumerate(lana):
    resultado += letra * (i + 1)  
    resultado += " "

print(resultado)
