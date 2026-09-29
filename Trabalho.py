usuarios = []
alimentos = []


def cadastrar_usuario():
    print("Cadastro de usuário")
    email = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    usuario = {
        "email": email,
        "senha": senha
    }

    usuarios.append(usuario)


def login():
    print("Entrando no sistema de login!")
    tentativas = 3

    while tentativas > 0:
        email = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        for usuario in usuarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                print("Login realizado com sucesso!")
                return

        tentativas = tentativas - 1
        print("Usuário ou senha incorretos.")
        print("Tentativas restantes:", tentativas)

    print("Número de tentativas esgotado!")


def alimento():
    titulo = input("Digite o título do alimento: ")

    while len(titulo) < 2:
        print("O nome precisa ter no mínimo 2 caracteres.")
        titulo = input("Digite o nome do alimento: ")

    preco = float(input("Digite o preço: "))

    descricao = input("Digite a descrição: ")

    while len(descricao) < 5:
        print("A descrição precisa ter no mínimo 5 caracteres.")
        descricao = input("Digite a descrição: ")

    comida = {
        "titulo": titulo,
        "preco": preco,
        "descricao": descricao
    }

    alimentos.append(comida)


cadastrar_usuario()
login()
alimento()
