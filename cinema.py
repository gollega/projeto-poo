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
        if not fileira:
            raise Exception("A fileira do assento não pode estar vazia.")

        if numero < 1:
            raise Exception("O número do assento deve ser maior que zero.")

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

    def __init__(self, filme: Filme, sala: Sala, horario: str, preco: float):
        self.__filme = filme
        self.__sala = sala
        self.__horario = horario
        self.__preco = preco

    def exibir_info(self):
        return (
            f"{self.__filme.exibir_info()}\n"
            f"{self.__sala.exibir_info()}\n"
            f"Horário da sessão: {self.__horario}\n"
            f"Preço do ingresso: R$ {self.__preco:.2f}"
        )

    def get_horario(self):
        return self.__horario

    def get_preco(self):
        return self.__preco

class Ingresso:
    def __init__(self, filme: Filme, sessao: Sessao, assento: Assento, preco: float | None = None):
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
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
 
 
class SnackBar:
    def __init__(self):
        self.__cardapio = {}  # {nome: Produto}
 
    def adicionar_produto(self, produto: Produto):
        self.__cardapio[produto.nome] = produto
 
    def buscar_produto(self, nome: str):
        if nome not in self.__cardapio:
            raise Exception(f"'{nome}' não existe no cardápio.")
        return self.__cardapio[nome]
 
    def remover_produto(self, nome: str):
        if nome in self.__cardapio:
            del self.__cardapio[nome]
        else:
            raise Exception(f"'{nome}'não existe no cárdapio.")
 
    def exibir_cardapio(self):
        return self.__cardapio
 
 
class Pedido:
    def __init__(self, snackbar: SnackBar):
        self.__snackbar = snackbar  # ligação com o cardápio
        self.__itens = {}  # {nome: quantidade}
        self.__valor_total = 0.0
 
    def adicionar_item(self, nome: str, quantidade: int = 1):
        produto = self.__snackbar.buscar_produto(nome)
        if quantidade <= 0:
            raise Exception("A quantidade deve ser maior que zero.")

        if nome in self.__itens: # inicia vazio
            self.__itens[nome] += quantidade # caso nao seja o primeiro pedido adicionar o restante
        else:
            self.__itens[nome] = quantidade # caso seja o primeiro pedido, adiciona a quantidade inicial
        self.__valor_total += produto.preco * quantidade
 
    def remover_item(self, nome: str):
        if nome not in self.__itens:
            raise Exception(f"'{nome}' não está no pedido.")
        produto = self.__snackbar.buscar_produto(nome)
        self.__valor_total -= produto.preco * self.__itens[nome]
        del self.__itens[nome]
 
    def exibir_pedido(self):
        return (
            f"Itens: {self.__itens}\n"
            f"Valor total: R$ {self.__valor_total:.2f}"
        )



