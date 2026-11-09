from cinema import *


def escolher_sessao(programacao):

    print(programacao.exibir_programacao())

    numero_sala = int(input("\nNúmero da sala: "))
    numero_sessao = int(input("Número da sessão: "))

    return programacao.buscar_sessao(numero_sala, numero_sessao)


def painel_bilheteria(programacao):

    while True:

        print("\n=== BILHETERIA ===")
        print("1 - Ver informações da sessão")
        print("2 - Comprar ingresso")
        print("3 - Comprar meia-entrada")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                try:
                    sessao = escolher_sessao(programacao)

                    print("\n=== INFORMAÇÕES DA SESSÃO ===")
                    print(sessao.exibir_info())

                except Exception as erro:
                    print(f"Erro: {erro}")

            case "2":
                print("\n=== COMPRA DE INGRESSOS ===")

                try:
                    sessao = escolher_sessao(programacao)

                    fileira = input("Fileira (A-E): ")
                    numero = int(input("Número do assento (1-10): "))

                    assento = Assento(fileira, numero)
                    ingresso = Ingresso(sessao, assento)

                    print("\nIngresso comprado com sucesso!")
                    ingresso.exibir_info()

                except Exception as erro:
                    print(f"Erro na compra: {erro}")

            case "3":
                print("\n=== COMPRA DE MEIA-ENTRADA ===")

                try:
                    sessao = escolher_sessao(programacao)

                    fileira = input("Fileira (A-E): ")
                    numero = int(input("Número do assento (1-10): "))

                    assento = Assento(fileira, numero)

                    ingresso = IngressoMeia(
                        sessao,
                        assento,
                        "Carteirinha de estudante"
                    )

                    print("\nIngresso comprado com sucesso!")
                    ingresso.exibir_info()

                except Exception as erro:
                    print(f"Erro na compra: {erro}")

            case "0":
                print("Voltando ao painel principal...")
                break

            case _:
                print("Opção inválida!")


def painel_snackbar(bar, pedido):

    while True:

        print("\n=== SNACK BAR ===")
        print("1 - Ver cardápio")
        print("2 - Adicionar item ao pedido")
        print("3 - Remover item do pedido")
        print("4 - Ver pedido")
        print("5 - Finalizar pedido")
        print("0 - Sair")

        opcao = input("Escolha: ")

        try:

            match opcao:

                case "1":
                    print(bar.exibir_cardapio())

                case "2":
                    id = int(input("ID do produto: "))
                    quantidade = int(input("Quantidade: "))

                    pedido.adicionar_item(id, quantidade)

                    print("Item adicionado com sucesso!")

                case "3":
                    id = int(input("ID do produto: "))
                    quantidade = int(input("Quantidade para remover: "))

                    pedido.remover_item(id, quantidade)

                    print("Item(s) removido(s) com sucesso!")

                case "4":
                    print("\n=== SEU PEDIDO ===")
                    print(pedido.exibir_pedido())

                case "5":
                    print("\n=== FINALIZANDO PEDIDO ===")
                    print(pedido.finalizar_pedido())

                case "0":
                    print("Voltando ao painel principal...")
                    break

                case _:
                    print("Opção inválida!")

        except ValueError:
            print("Digite uma quantidade válida.")

        except Exception as erro:
            print(f"Erro: {erro}")


def cadastrar_filme(programacao):

    print("\n=== CADASTRAR FILME ===")

    try:
        titulo = input("Nome do filme: ")
        duracao = int(input("Duração em minutos: "))
        genero = input("Gênero: ")
        classificacao = int(input("Classificação indicativa: "))

        filme = Filme(titulo, duracao, genero, classificacao)

        print(programacao.cadastrar_filme(filme))

    except Exception as erro:
        print(f"Erro ao cadastrar filme: {erro}")


def escolher_filme(programacao):

    filmes = programacao.listar_filmes()

    if not filmes:
        raise ValueError("Nenhum filme cadastrado. Cadastre um filme primeiro.")

    print("\n=== FILMES CADASTRADOS ===")

    for numero, filme in enumerate(filmes, 1):
        print(f"{numero} - {filme.get_titulo()}")

    escolha = int(input("\nEscolha o número do filme: "))

    if escolha < 1 or escolha > len(filmes):
        raise ValueError("Opção de filme inválida.")

    return filmes[escolha - 1]


def painel_programacao(programacao):

    while True:

        print("\n=== PROGRAMAÇÃO ===")
        print("1 - Ver programação")
        print("2 - Cadastrar sala")
        print("3 - Cadastrar sessão")
        print("4 - Cadastrar filme")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                print(programacao.exibir_programacao())

            case "2":
                try:
                    numero = int(input("Número da sala: "))
                    capacidade = int(input("Capacidade da sala: "))

                    sala = Sala(numero, capacidade)

                    print(programacao.cadastrar_sala(sala))

                except Exception as erro:
                    print(f"Erro: {erro}")

            case "3":
                try:
                    print("\n=== CADASTRAR SESSÃO ===")

                    filme = escolher_filme(programacao)

                    numero_sala = int(input("\nNúmero da sala: "))
                    sala = programacao.buscar_sala(numero_sala)

                    horario = input("Horário da sessão (HH:MM): ")
                    preco = float(input("Preço do ingresso: "))

                    sessao = Sessao(filme, sala, horario, preco)

                    print(programacao.cadastrar_sessao(sessao))

                except Exception as erro:
                    print(f"Erro: {erro}")

            case "4":
                cadastrar_filme(programacao)

            case "0":
                print("Voltando ao painel principal...")
                break

            case _:
                print("Opção inválida!")


filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
filme2 = Filme("Barbie", 114, "Comédia", 12)

programacao = Programacao()

programacao.cadastrar_filme(filme1)
programacao.cadastrar_filme(filme2)

sala1 = Sala(1, 50)
sala2 = Sala(2, 50)

programacao.cadastrar_sala(sala1)
programacao.cadastrar_sala(sala2)

sessao1 = Sessao(filme1, sala1, "19:30", 30.00)
sessao2 = Sessao(filme2, sala2, "21:30", 30.00)

programacao.cadastrar_sessao(sessao1)
programacao.cadastrar_sessao(sessao2)

bar = SnackBar()

bar.adicionar_produto(Produto(1, "X-Burguer", 15.0, 10))
bar.adicionar_produto(Produto(2, "Refrigerante", 6.5, 20))
bar.adicionar_produto(Produto(3, "Batata Frita", 12.0, 15))
bar.adicionar_produto(Produto(4, "Pipoca", 8.0, 25))

pedido = Pedido(bar)

while True:

    print("\n=== CINEMA - PAINEL DE ATENDIMENTO ===")
    print("1 - Bilheteria")
    print("2 - Snack Bar")
    print("3 - Programação")
    print("0 - Encerrar")

    opcao = input("Escolha: ")

    match opcao:

        case "1":
            painel_bilheteria(programacao)

        case "2":
            painel_snackbar(bar, pedido)

        case "3":
            painel_programacao(programacao)

        case "0":
            print("Encerrando o sistema...")
            break

        case _:
            print("Opção inválida!")