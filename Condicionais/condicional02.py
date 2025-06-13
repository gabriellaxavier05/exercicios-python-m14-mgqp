# Condicionais encadeadas

print("Verificando a nota do aluno \n")

nota = int(input("Informe a nota tirada pelo aluno: "))

print("\n")

# Verificando a nota informada do aluno
if nota >= 6:
    if nota >= 9:
        print("Nota excelente! 👏🏼")
    else:
        print("Nota boa! 👍🏼")
else:  
    print("Reprovado! ❌")