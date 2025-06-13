# Veriicando usuário e senha corretos

print("-- Login -- \n")

usuario = input("Informe o usuário: ")
senha = int(input("Informe a senha: "))

print("\n")

if usuario == "Gabriella" and senha == 12345:
    print("Login OK!")
else:
    print("Login inválido")