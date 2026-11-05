class Filme():
    __titulo: str
    __duracao: int
    __genero: str
    __classificacao: int

    def __init__(self, titulo: str, duracao: int, genero: str, classificacao: int):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__genero = genero
        self.__classificacao = classificacao

    def exibir_info(self):
        return (
            f"Título do filme: {self.__titulo}\n"
            f"Duração: {self.__duracao} min\n"
            f"Gênero: {self.__genero}\n"
            f"Classificação indicativa: {self.__classificacao} anos"
        )

class Assento():
    __fileira: str
    __numero: int

    def __init__(self, fileira: str, numero: int):
        if fileira not in ["A", "B", "C", "D", "E"]:
            raise ValueError("Fileira inválida! Escolha entre A-E.")

        if not isinstance(numero, int) or not 1 <= numero <= 10:
            raise ValueError("Número inválido! Escolha entre 1-10.")

        self.__fileira = fileira
        self.__numero = numero

    def identificarAssento(self):
        return f"Seu assento é o {self.__fileira}{self.__numero}"


class Sala():
    __numero: int
    __capacidade: int
    __assentos: list[Assento]

    def __init__(self, numero: int, capacidade: int):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__assentos = []

    def adicionarAssento(self, assento: Assento):
        if len(self.__assentos) >= self.__capacidade:
            raise Exception("A sala atingiu sua capacidade máxima.")

        self.__assentos.append(assento)
        return "Assento adicionado com sucesso!"

    def exibir_info(self):
        return (
            f"Número da sala: {self.__numero}\n"
            f"Capacidade: {self.__capacidade} pessoas\n"
            f"Quantidade de assentos cadastrados: {len(self.__assentos)}"
        )

class Sessao():
    __filme: Filme
    __sala: Sala
    __horario: str
    __preco: float
    __assentos_vendidos: list[Assento]

    def __init__(self, filme: Filme, sala: Sala, horario: str, preco: float):
        self.__filme = filme
        self.__sala = sala
        self.__horario = horario
        self.__preco = preco
        self.__assentos_vendidos = []

    def vender_assento(self, assento: Assento):
        for vendido in self.__assentos_vendidos:
            if (
                vendido.identificarAssento()
                == assento.identificarAssento()
            ):
                raise ValueError("Este assento já foi vendido!")

        self.__assentos_vendidos.append(assento)
        return "Assento vendido com sucesso!"

    def exibir_info(self):
        return (
            f"{self.__filme.exibir_info()}\n"
            f"{self.__sala.exibir_info()}\n"
            f"Horário da sessão: {self.__horario}\n"
            f"Preço do ingresso: R$ {self.__preco:.2f}\n"
            f"Assentos vendidos: {len(self.__assentos_vendidos)}"
        )

    def get_horario(self):
        return self.__horario

    def get_preco(self):
        return self.__preco

class Ingresso:
    def __init__(self, filme: Filme, sessao: Sessao, assento: Assento, preco: float | None = None):
        sessao.vender_assento(assento)

        self.filme = filme
        self.sessao = sessao
        self.assento = assento
        self.preco = sessao.get_preco() if preco is None else preco

    def calcular_preco(self):
        return self.preco

    def exibir_info(self):
        print(self.filme.exibir_info())
        print(f"Horário da Sessão: {self.sessao.get_horario()}")
        print(self.assento.identificarAssento())
        print(f"Valor: R$ {self.calcular_preco():.2f}")

class IngressoMeia(Ingresso):
    def __init__(self, filme: Filme, sessao: Sessao, assento: Assento, comprovante: str, preco: float | None = None):
        super().__init__(filme, sessao, assento, preco)
        self.comprovante = comprovante

    def calcular_preco(self):
        return self.sessao.get_preco() / 2

    def exibir_info(self):
        super().exibir_info()
        print(f"Tipo: Meia-Entrada (Comprovante: {self.comprovante})\n")

class Produto:
    def __init__(self, id: int, nome: str, preco: float, estoque: int):
        self.estoque = estoque
        self.id = id
        self.nome = nome
        self.preco = preco


class SnackBar:
    def __init__(self):
        self.__cardapio: dict[int, Produto] = {} # {id: Produto}

    def adicionar_produto(self, produto: Produto):
        self.__cardapio[produto.id] = produto

    def buscar_produto(self, id: int):
        if id not in self.__cardapio:
            raise Exception(f"O ID '{id}' não existe no cardápio.")
        return self.__cardapio[id]

    def remover_produto(self, id: int):
        if id in self.__cardapio:
            del self.__cardapio[id]
        else:
            raise Exception(f"O ID '{id}' não existe no cardápio.")

    def exibir_cardapio(self):
        if not self.__cardapio:
            return "O cardápio está vazio."
            
        menu = "=== CARDÁPIO ===\n"
        for produto in self.__cardapio.values():
            if produto.estoque > 0:
                menu += f"[{produto.id}] {produto.nome} - R$ {produto.preco:.2f} (Estoque: {produto.estoque})\n"
            else:
                menu += f"[{produto.id}] {produto.nome} - R$ {produto.preco:.2f} *** ESGOTADO ***\n"
                
        return menu


class Pedido:
    def __init__(self, snackbar: SnackBar):
        self.__snackbar = snackbar  # ligação com o cardápio
        self.__itens = {}  # {Produto: quantidade} 
        self.__valor_total = 0.0

    def adicionar_item(self, id: int, quantidade: int = 1):
        if quantidade <= 0:
            raise Exception("A quantidade deve ser maior que zero.")

        produto = self.__snackbar.buscar_produto(id)
        
        if produto.estoque <= 0:
            raise Exception(f"O produto '{produto.nome}' está totalmente esgotado.")

        # Tratamento de erro: se pedir mais do que tem, adiciona o limite e avisa
        if quantidade > produto.estoque:
            print(f"AVISO: Só temos {produto.estoque} unidade(s) de '{produto.nome}' disponível(is). Adicionando o limite ao pedido.")
            quantidade_adicionada = produto.estoque
        else:
            quantidade_adicionada = quantidade

        # 1. Baixa o estoque NA HORA para o cardápio atualizar na mesma hora
        produto.estoque -= quantidade_adicionada

        # 2. Adiciona ao carrinho temporário
        if produto in self.__itens:
            self.__itens[produto] += quantidade_adicionada
        else:
            self.__itens[produto] = quantidade_adicionada
            
        self.__valor_total += produto.preco * quantidade_adicionada

    def remover_item(self, id: int, quantidade: int = 1):
        if quantidade <= 0:
            raise Exception("A quantidade a ser removida deve ser maior que zero.")

        produto_remover = None
        for produto in self.__itens.keys():
            if produto.id == id:
                produto_remover = produto
                break
                
        if not produto_remover:
            raise Exception(f"O ID '{id}' não está no pedido.")
            
        quantidade_atual = self.__itens[produto_remover]
        
        # Se pedir para remover tudo ou mais do que tem, cancela o item todo do carrinho
        if quantidade >= quantidade_atual:
            quantidade_a_remover = quantidade_atual
            del self.__itens[produto_remover]
        else:
            # Subtrai apenas a quantidade desejada
            quantidade_a_remover = quantidade
            self.__itens[produto_remover] -= quantidade_a_remover
            
        self.__valor_total -= produto_remover.preco * quantidade_a_remover
        
        # 3. Devolve a quantidade removida para o estoque real do cardápio
        produto_remover.estoque += quantidade_a_remover

    def exibir_pedido(self):
        if not self.__itens:
            return "O pedido está vazio."
            
        recibo = "\n=== RESUMO DO PEDIDO ===\n"
        for produto, quantidade in self.__itens.items():
            subtotal = produto.preco * quantidade
            recibo += f"{quantidade}x {produto.nome} ....... R$ {subtotal:.2f}\n"
            
        recibo += "------------------------\n"
        recibo += f"Valor total: R$ {self.__valor_total:.2f}"
        
        return recibo
        
    def finalizar_pedido(self):
        if not self.__itens:
            raise Exception("O pedido está vazio. Não há o que finalizar.")
            
        # Salva o recibo antes de esvaziar o carrinho
        recibo = self.exibir_pedido()
        
        # Limpa o carrinho (preparando para o próximo cliente)
        self.__itens.clear()
        self.__valor_total = 0.0
        
        return f"\nPedido finalizado com sucesso!\n{recibo}"