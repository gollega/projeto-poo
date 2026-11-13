import tkinter as tk
import json
import os

from cinema import *
from interface import CinemaApp


ARQUIVO_DADOS = "dados_cinema.json"


def criar_dados_iniciais():
    programacao = Programacao()

    filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
    filme2 = Filme("Barbie", 114, "Comédia", 12)

    programacao.cadastrar_filme(filme1)
    programacao.cadastrar_filme(filme2)

    sala1 = Sala(1, 50)
    sala2 = Sala(2, 50)

    programacao.cadastrar_sala(sala1)
    programacao.cadastrar_sala(sala2)

    programacao.cadastrar_sessao(
        Sessao(filme1, sala1, "19:30", 30.00)
    )

    programacao.cadastrar_sessao(
        Sessao(filme2, sala2, "21:30", 30.00)
    )

    bar = SnackBar()

    bar.adicionar_produto(Produto(1, "X-Burguer", 15.0, 10))
    bar.adicionar_produto(Produto(2, "Refrigerante", 6.5, 20))
    bar.adicionar_produto(Produto(3, "Batata Frita", 12.0, 15))
    bar.adicionar_produto(Produto(4, "Pipoca", 10.0, 40))
    bar.adicionar_produto(Produto(5, "Chocolate", 8.0, 15))
    bar.adicionar_produto(Produto(6, "Suco", 6.5, 50))
    bar.adicionar_produto(Produto(7, "Salgadinho", 12.0, 15))
    bar.adicionar_produto(Produto(8, "Bala Fini", 6.0, 30))
    bar.adicionar_produto(Produto(9, "Água", 5.0, 50))
    bar.adicionar_produto(Produto(10, "Pipoca Doce", 12.0, 20))

    pedido = Pedido(bar)
    salvar_dados(programacao, bar, pedido)

    return programacao, bar, pedido


def salvar_dados(programacao, bar, pedido):
    dados = {
        "filmes": [],
        "salas": [],
        "sessoes": [],
        "produtos": [],
        "pedido": []
    }

    for filme in programacao.listar_filmes():
        dados["filmes"].append({
            "titulo": filme.get_titulo(),
            "duracao": filme.get_duracao(),
            "genero": filme.get_genero(),
            "classificacao": filme.get_classificacao()
        })

    for sala in programacao.listar_salas():
        dados["salas"].append({
            "numero": sala.get_numero(),
            "capacidade": sala.get_capacidade()
        })

    for numero_sala, numero_sessao, sessao in programacao.listar_sessoes():
        assentos = []

        for assento in sessao.listar_assentos_vendidos():
            assentos.append({
                "fileira": assento.get_fileira(),
                "numero": assento.get_numero()
            })

        dados["sessoes"].append({
            "sala": numero_sala,
            "titulo_filme": sessao.get_filme().get_titulo(),
            "horario": sessao.get_horario(),
            "preco": sessao.get_preco(),
            "assentos_vendidos": assentos
        })

    for produto in bar.listar_produtos():
        dados["produtos"].append({
            "id": produto.id,
            "nome": produto.nome,
            "preco": produto.preco,
            "estoque": produto.estoque
        })

    for produto, quantidade in pedido.listar_itens():
        dados["pedido"].append({
            "produto_id": produto.id,
            "quantidade": quantidade
        })

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return criar_dados_iniciais()

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        programacao = Programacao()
        filmes = {}

        for item in dados["filmes"]:
            filme = Filme(
                item["titulo"],
                item["duracao"],
                item["genero"],
                item["classificacao"]
            )

            programacao.cadastrar_filme(filme)
            filmes[filme.get_titulo()] = filme

        salas = {}

        for item in dados["salas"]:
            sala = Sala(item["numero"], item["capacidade"])
            programacao.cadastrar_sala(sala)
            salas[item["numero"]] = sala

        for item in dados["sessoes"]:
            sessao = Sessao(
                filmes[item["titulo_filme"]],
                salas[item["sala"]],
                item["horario"],
                item["preco"]
            )

            programacao.cadastrar_sessao(sessao)

            for assento in item["assentos_vendidos"]:
                sessao.vender_assento(
                    Assento(
                        assento["fileira"],
                        assento["numero"]
                    )
                )

        bar = SnackBar()

        for item in dados["produtos"]:
            bar.adicionar_produto(
                Produto(
                    item["id"],
                    item["nome"],
                    item["preco"],
                    item["estoque"]
                )
            )

        pedido = Pedido(bar)

        for item in dados["pedido"]:
            produto = bar.buscar_produto(item["produto_id"])
            pedido.restaurar_item(produto, item["quantidade"])

        return programacao, bar, pedido

    except (KeyError, ValueError, TypeError, json.JSONDecodeError):
        print(
            "Não foi possível carregar os dados salvos. "
            "Criando dados iniciais."
        )
        return criar_dados_iniciais()

if __name__ == "__main__":
    programacao, bar, pedido = carregar_dados()

    root = tk.Tk()

    app = CinemaApp(
        root,
        programacao,
        bar,
        pedido,
        salvar_dados
    )

    root.mainloop()