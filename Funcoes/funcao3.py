# Função em Pyhton com retorno de valor

def somar(a, b):
    return a + b

print("-- SOMA DE VALORES USANDO UMA FUNÇÃO -- \n")

num1 = int(input("Digite o primeiro número: ")) # Entrada do primeiro número
num2 = int(input("Digite o segundo número: ")) # Entrada do segundo número

resultado = somar(num1, num2) # Chamada da função com dois argumentos
print("\nA soma dos valores informados é: ", resultado) # Exibe o resultado da soma