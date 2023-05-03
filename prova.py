
# Inicializa um dicionário vazio para armazenar os livros cadastrados e disponiveis
livro = {}

def livros():
    while True:
        print("\n==== MENU ====")
        print("1. Listar livros")
        print("2. Cadastrar livro")
        print("3. Alterar livro")
        print("4. Excluir livro")
        print("0. Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            cadastrar_livro()
        elif opcao == "3":
            alterar_livro()
        elif opcao == "4":
            excluir_livro()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Função de listar os livros cadastrados
def listar_livros():

    # Se o tamanho da arrays de 'livros' for == 0
    if len(livro) == 0:
        print("Não há livros cadastrados.")
    else:
        print("Livros cadastrados:")
        for id, titulo in livro.items():
            print(f"{id}: {titulo}")

# Função de cadastrar livro
def cadastrar_livro():
    id = input("Digite o ID do livro: ")
    titulo = input("Digite o título do livro: ")
    livro[id] = titulo
    print(f"O livro '{titulo}' foi cadastrado com sucesso!")

# Função de alterar o livro
def alterar_livro():
    id = input("Digite o ID do livro a ser alterado: ")

    #Se não tiver id em livro
    if id not in livro:
        print("Livro não encontrado.")
    else:
        novo_titulo = input(f"Digite o novo título para o livro '{livro[id]}': ")
        livro[id] = novo_titulo
        print("Livro alterado com sucesso!")

def excluir_livro():
    id = input("Digite o ID do livro a ser excluído: ")
    if id not in livro:
        print("Livro não encontrado.")
    else:
        titulo = livro[id]
        del livro[id]
        print(f"O livro '{titulo}' foi excluído com sucesso!")

# Inicializa um dicionário vazio para armazenar os clientes
cliente = {}

def clientes():
    while True:
        print("\n==== MENU ====")
        print("1. Listar clientes")
        print("2. Cadastrar cliente")
        print("3. Alterar cliente")
        print("4. Excluir cliente")
        print("0. Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Função de listar os clientes cadastrados
def listar_clientes():

    # Se o tamanho da arrays de 'clientes' for == 0
    if len(cliente) == 0:
        print("Não há clientes cadastrados.")
    else:
        print("Clientes cadastrados:")
        for id, nome in cliente.items():
            print(f"{id}: {nome}")

# Função de cadastrar cliente
def cadastrar_cliente():
    id = input("Digite o ID do cliente: ")
    nome = input("Digite o nome do cliente: ")
    cliente[id] = nome
    print(f"O cliente '{nome}' foi cadastrado com sucesso!")

# Função de alterar o cliente
def alterar_cliente():
    id = input("Digite o ID do cliente a ser alterado: ")

    #Se não tiver id em cliente
    if id not in cliente:
        print("Cliente não encontrado.")
    else:
        novo_nome = input(f"Digite o novo nome para o cliente '{cliente[id]}': ")
        cliente[id] = novo_nome
        print("Clientes alterado com sucesso!")

# Função de excluir o cliente
def excluir_cliente():
    id = input("Digite o ID do cliente a ser excluído: ")
    if id not in cliente:
        print("Cliente não encontrado.")
    else:
        nome = cliente[id]
        del cliente[id]
        print(f"O cliente '{nome}' foi excluído com sucesso!")

# Função de alocar os livros
def locacao():
    while True:
        print("\n==== MENU ====")
        print("1. Listar livros")
        print("2. Alocar livro")
        print("3. Devolver livro")
        print("0. Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            locar_livro()
        elif opcao == "3":
            devolver_livro()
            break
        else:
            print("Opção inválida!")

# Função de listar os livros disponiveis
def listar_livros():

    # Se o tamanho da arrays de 'livros' for == 0
    if len(livro) == 0:
        print("Não há livros cadastrados.")
    else:
        print("Livros cadastrados:")
        for id, titulo in livro.items():
            print(f"{id}: {titulo}")

# Função de cadastrar cliente
def locar_livro():
    id = input("Digite o ID do livro escolhido: ")
    titulo = input("Digite o nome do livro escolhido: ")
    livro[id] = titulo
    print(f"O livro '{titulo}' foi alocado com sucesso!")

def devolver_livro():
    id = input("Digite o ID do livro a ser devolvido: ")
    if id not in livro:
        print("Livro não encontrado.")
    else:
        titulo = livro[id]
        del livro[id]
        print(f"O livro '{titulo}' foi devolvido com sucesso!")


# Função de alocar os livros
def gerencial():
    while True:
        print("\n==== MENU ====")
        print("1. Consultar livro")
        print("2. Consultar por cliente")
        print("0. Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            consultar_livros()
        elif opcao == "2":
            consultar_clientes()
        else:
            print("Opção inválida!")

# Função de listar os livros disponiveis
def consultar_livros():

    # Se o tamanho da arrays de 'livros' for == 0
    if len(livro) == 0:
        print("Não há livros cadastrados.")
    else:
        print("Livros cadastrados:")
        for id, titulo in livro.items():
            print(f"{id}: {titulo}")

# Função de listar os clientes cadastrados
def consultar_clientes():

    # Se o tamanho da arrays de 'clientes' for == 0
    if len(cliente) == 0:
        print("Não há clientes cadastrados.")
    else:
        print("Clientes cadastrados:")
        for id, nome in cliente.items():
            print(f"{id}: {nome}")

def menu():
    while True:
        print("\n==== MENU ====")
        print("1. Livros")
        print("2. Clientes")
        print("3. Locacao")
        print("4. Gerencial")
        print("0. Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            livros()
        elif opcao == "2":
            clientes()
        elif opcao == "3":
            locacao()
        elif opcao == "4":
            gerencial()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Executar menu
menu()
