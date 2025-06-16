# Dicionário para armazenar os usuários cadastrados
usuarios = {}

# Função para cadastrar um usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Informe o nome do usuário: ")

    # Verifica se o nome já existe na base
    if nome in usuarios:
        print("⚠️ Esse nome já está cadastrado. Use outro nome.")
        return

    idade = int(input("Informe a idade do usuário: "))
    renda_mensal = float(input("Informe a renda mensal do usuário: "))
    historico_credito = input("Informe o histórico de crédito do usuário (sim ou não): ").lower()

    # Armazena no dicionário
    usuarios[nome] = {
        "idade": idade,
        "renda_mensal": renda_mensal,
        "historico_credito": historico_credito
    }

    print(f"✅ Usuário {nome} cadastrado com sucesso!")


# Função para verificar se é elegível para empréstimo
def verificar_elegibilidade(nome):
    if nome not in usuarios:
        print("⚠️ Usuário não encontrado.")
        return

    usuario = usuarios[nome]
    idade = usuario["idade"]
    renda = usuario["renda_mensal"]
    historico = usuario["historico_credito"]

    if idade > 18 and renda > 1000 and historico != "não":
        print(f"✅ Usuário {nome} é elegível para empréstimo.")
    else:
        print(f"❌ Usuário {nome} NÃO é elegível para empréstimo.")


# Função para exibir dados de um usuário específico
def exibir_usuario(nome):
    if nome not in usuarios:
        print("⚠️ Usuário não encontrado.")
        return

    usuario = usuarios[nome]
    print(f"\n--- Dados do Usuário {nome} ---")
    print(f"Idade: {usuario['idade']}")
    print(f"Renda Mensal: {usuario['renda_mensal']}")
    print(f"Histórico de Crédito: {usuario['historico_credito']}")


# Função para exibir a base de usuários
def exibir_base_usuarios():
    print("\n--- Base de Usuários ---")
    total = len(usuarios)
    print(f"Total de usuários cadastrados: {total}")

    if total > 0:
        print("Nomes dos usuários:")
        for nome in usuarios:
            print(f"- {nome}")
    else:
        print("Nenhum usuário cadastrado ainda.")


# Menu principal
while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar usuário")
    print("2 - Verificar elegibilidade de empréstimo")
    print("3 - Exibir dados de um usuário")
    print("4 - Exibir base de usuários")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        nome = input("Informe o nome do usuário para verificar elegibilidade: ")
        verificar_elegibilidade(nome)
    elif opcao == "3":
        nome = input("Informe o nome do usuário para exibir os dados: ")
        exibir_usuario(nome)
    elif opcao == "4":
        exibir_base_usuarios()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("⚠️ Opção inválida. Tente novamente.")
