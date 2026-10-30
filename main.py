from cinema import *

if __name__ == "__main__":
    filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
    try:
        assento1 = Assento("A", 12)
        print(assento1.identificarAssento())

        sala1 = Sala(1, 50)

        try:
            print(sala1.adicionarAssento(assento1))
        except Exception as erro:
            print(f"Erro ao adicionar assento: {erro}")

        sessao1 = Sessao(filme1, sala1, "19:30", 30.00)

        print("=== INFORMAÇÕES DO FILME ===")
        print(filme1.exibir_info())

        print("\n=== IDENTIFICAÇÃO DO ASSENTO ===")
        print(assento1.identificarAssento())

        print("\n=== INFORMAÇÕES DA SALA ===")
        print(sala1.exibir_info())

        print("\n=== INFORMAÇÕES DA SESSÃO ===")
        print(sessao1.exibir_info())

    except Exception as erro:
        print(f"Erro ao criar assento: {erro}")

          # snackbar
    bar = SnackBar()
    bar.adicionar_produto(Produto("X-Burguer", 15.0))
    bar.adicionar_produto(Produto("Refrigerante", 6.5))
    bar.adicionar_produto(Produto("Batata Frita", 12.0))
 
    pedido = Pedido(bar)
    
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
                    for produto in bar.exibir_cardapio().values():
                        print(f"{produto.nome} - R$ {produto.preco:.2f}")
                case "2":
                    nome = input("Nome do produto: ")
                    quantidade = int(input("Quantidade: "))
                    pedido.adicionar_item(nome, quantidade)
                    print("Item adicionado!")
                case "3":
                    nome = input("Nome do produto: ")
                    pedido.remover_item(nome)
                    print("Item removido!") 
                case "4":
                    print(pedido.exibir_pedido())
                case "0":
                    print("Encerrando.")
                    break
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("Digite apenas números.")
        except Exception as erro:
            print(erro)

