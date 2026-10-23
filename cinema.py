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
        if len(self.__assentos) < self.__capacidade:
            self.__assentos.append(assento)
            return "Assento adicionado com sucesso!"
        return "A sala atingiu sua capacidade máxima."

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
            f"=== INFORMAÇÕES DA SESSÃO ===\n"
            f"{self.__filme.exibir_info()}\n"
            f"{self.__sala.exibir_info()}\n"
            f"Horário da sessão: {self.__horario}\n"
            f"Preço do ingresso: R$ {self.__preco:.2f}"
        )
