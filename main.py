
from cinema import *


def escolher_sessao(programacao):
    print(programacao.exibir_programacao())

    numero_sala = int(input("\nNúmero da sala: "))
    numero_sessao = int(input("Número da sessão: "))

    return programacao.buscar_sessao(numero_sala, numero_sessao)


def painel_bilheteria(programacao):
    while True:

        print("\n=== BILHETERIA ===")
        print("1 - Ver programação")
        print("2 - Ver informações da sessão")
        print("3 - Comprar ingresso")
        print("4 - Comprar meia-entrada")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                print(programacao.exibir_programacao())

            case "2":
                try:
                    sessao = escolher_sessao(programacao)

                    print("\n=== INFORMAÇÕES DA SESSÃO ===")
                    print(sessao.exibir_info())

                except Exception as erro:
                    print(f"Erro: {erro}")

            case "3":
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

            case "4":
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


def painel_programacao(programacao):
    while True:

        print("\n=== PROGRAMAÇÃO ===")
        print("1 - Ver programação")
        print("2 - Cadastrar sala")
        print("3 - Cadastrar sessão")
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
                    titulo = input("Nome do filme: ")
                    duracao = int(input("Duração do filme em minutos: "))
                    genero = input("Gênero do filme: ")
                    classificacao = int(input("Classificação indicativa: "))

                    numero_sala = int(input("Número da sala: "))
                    sala = programacao.buscar_sala(numero_sala)

                    horario = input("Horário da sessão (HH:MM): ")
                    preco = float(input("Preço do ingresso: "))

                    filme = Filme(titulo, duracao, genero, classificacao)
                    sessao = Sessao(filme, sala, horario, preco)

                    print(programacao.cadastrar_sessao(sessao))

                except Exception as erro:
                    print(f"Erro: {erro}")

            case "0":
                print("Voltando ao painel principal...")
                break

            case _:
                print("Opção inválida!")


# FILME, SALA E SESSÃO INICIAIS
filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
sala1 = Sala(1, 50)
sessao1 = Sessao(filme1, sala1, "19:30", 30.00)

# PROGRAMAÇÃO
programacao = Programacao()
programacao.cadastrar_sala(sala1)
programacao.cadastrar_sessao(sessao1)

# SNACK BAR
bar = SnackBar()

bar.adicionar_produto(Produto(1, "X-Burguer", 15.0, 10))
bar.adicionar_produto(Produto(2, "Refrigerante", 6.5, 20))
bar.adicionar_produto(Produto(3, "Batata Frita", 12.0, 15))
bar.adicionar_produto(Produto(4, "Pipoca", 8.0, 25))

pedido = Pedido(bar)

# PAINEL PRINCIPAL
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