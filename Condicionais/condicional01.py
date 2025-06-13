# Condicionais em Python 

print("-- Verificação de idade --\n")

idade = int(input("Informe sua idade: "))

# Fazendo a verificação/comparação e apresentando o resultado
if idade >= 18 and idade <= 59:
    print("Maior de idade e adulto.")
elif idade >= 60:
    print("Maior de idade e idoso.")
else:
    print("Menor de idade.")