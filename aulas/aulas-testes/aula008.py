# Exercitando operadores relacionais e lógicos

usuario = input('Digite o seu usuário: ')
senha = int(input("Digite a sua senha: "))

lana_usuario = "Lana"
lana_senha = 1402

uev_usuario = "Ueverton"
uev_senha = 1402


if lana_usuario == usuario and lana_senha == senha or usuario == uev_usuario and senha == uev_senha:
    print(f"Abrindo a porta para você, {usuario}")
else: 
    print("Usuário ou Senha estão incorretos")

