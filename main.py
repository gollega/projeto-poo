
from cinema import *


def painel_bilheteria(filme, sala, sessao):
    while True:

        print("\n=== BILHETERIA ===")
        print("1 - Ver informações do filme")
        print("2 - Ver informações da sala")
        print("3 - Ver informações da sessão")
        print("4 - Comprar ingresso")
        print("5 - Comprar meia-entrada")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                print("\n=== INFORMAÇÕES DO FILME ===")
                print(filme.exibir_info())

            case "2":
                print("\n=== INFORMAÇÕES DA SALA ===")
                print(sala.exibir_info())

            case "3":
                print("\n=== INFORMAÇÕES DA SESSÃO ===")
                print(sessao.exibir_info())

            case "4":
                print("\n=== COMPRA DE INGRESSOS ===")

                try:
                    fileira = input("Fileira (A-E): ")
                    numero = int(input("Número do assento (1-10): "))

                    assento = Assento(fileira, numero)
                    ingresso = Ingresso(filme, sessao, assento)

                    print("\nIngresso comprado com sucesso!")
                    ingresso.exibir_info()

                except Exception as erro:
                    print(f"Erro na compra: {erro}")

            case "5":
                print("\n=== COMPRA DE MEIA-ENTRADA ===")

                try:
                    fileira = input("Fileira (A-E): ")
                    numero = int(input("Número do assento (1-10): "))

                    assento = Assento(fileira, numero)
                    ingresso = IngressoMeia(
                        filme,
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


# FILME, SALA E SESSÃO
filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
sala1 = Sala(1, 50)
sessao1 = Sessao(filme1, sala1, "19:30", 30.00)

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
    print("0 - Encerrar")

    opcao = input("Escolha: ")

    match opcao:

        case "1":
            painel_bilheteria(filme1, sala1, sessao1)

        case "2":
            painel_snackbar(bar, pedido)

        case "0":
            print("Encerrando o sistema...")
            break

        case _:
            print("Opção inválida!")