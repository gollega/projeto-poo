
from cinema import *

if __name__ == "__main__":

    # FILME
    filme1 = Filme("Interestelar", 169, "Ficção científica", 10)

    # SALA
    sala1 = Sala(1, 50)

    # SESSÃO
    sessao1 = Sessao(filme1, sala1, "19:30", 30.00)

    print("=== INFORMAÇÕES DO FILME ===")
    print(filme1.exibir_info())

    print("\n=== INFORMAÇÕES DA SALA ===")
    print(sala1.exibir_info())

    print("\n=== INFORMAÇÕES DA SESSÃO ===")
    print(sessao1.exibir_info())

    # COMPRA DE INGRESSOS

    print("\n=== COMPRA DE INGRESSOS ===")

    try:
        assento1 = Assento("A", 10)
        ingresso1 = Ingresso(filme1, sessao1, assento1)

        print("\nIngresso comprado com sucesso!")
        ingresso1.exibir_info()

    except Exception as erro:
        print(f"Erro na compra: {erro}")

    # TESTE DE ASSENTO DUPLICADO

    print("\n=== TESTE DE ASSENTO DUPLICADO ===")

    try:
        assento2 = Assento("A", 10)
        ingresso2 = Ingresso(filme1, sessao1, assento2)

        print("Ingresso comprado com sucesso!")

    except Exception as erro:
        print(f"Erro na compra: {erro}")

    # TESTE DE MEIA-ENTRADA

    print("\n=== COMPRA DE MEIA-ENTRADA ===")

    try:
        assento3 = Assento("B", 5)
        ingresso3 = IngressoMeia(
            filme1,
            sessao1,
            assento3,
            "Carteirinha de estudante"
        )

        print("\nIngresso comprado com sucesso!")
        ingresso3.exibir_info()

    except Exception as erro:
        print(f"Erro na compra: {erro}")

    # SNACK BAR

    bar = SnackBar()

    bar.adicionar_produto(Produto("X-Burguer", 15.0))
    bar.adicionar_produto(Produto("Refrigerante", 6.5))
    bar.adicionar_produto(Produto("Batata Frita", 12.0))

    pedido = Pedido(bar)

    # MENU SNACK BAR

    while True:

        print("\n=== SNACK BAR ===")
        print("1 - Ver cardápio")
        print("2 - Adicionar item ao pedido")
        print("3 - Remover item do pedido")
        print("4 - Ver pedido")
        print("0 - Sair")

        opcao = input("Escolha: ")

        try:

            match opcao:

                case "1":
                    print("\n=== CARDÁPIO ===")

                    for produto in bar.exibir_cardapio().values():
                        print(f"{produto.nome} - R$ {produto.preco:.2f}")

                case "2":
                    nome = input("Nome do produto: ")
                    quantidade = int(input("Quantidade: "))

                    pedido.adicionar_item(nome, quantidade)

                    print("Item adicionado com sucesso!")

                case "3":
                    nome = input("Nome do produto: ")

                    pedido.remover_item(nome)

                    print("Item removido com sucesso!")

                case "4":
                    print("\n=== SEU PEDIDO ===")
                    print(pedido.exibir_pedido())

                case "0":
                    print("Encerrando o sistema...")
                    break

                case _:
                    print("Opção inválida!")

        except ValueError:
            print("Digite uma quantidade válida.")

        except Exception as erro:
            print(f"Erro: {erro}")
