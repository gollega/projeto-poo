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