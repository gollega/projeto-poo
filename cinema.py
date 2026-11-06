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

    def get_titulo(self):
        return self.__titulo

    def get_duracao(self):
        return self.__duracao


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
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

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

    def get_numero(self):
        return self.__numero

    def get_capacidade(self):
        return self.__capacidade


class Sessao():
    __filme: Filme
    __sala: Sala
    __horario: str
    __preco: float
    __assentos_vendidos: list[Assento]

    def __init__(self, filme: Filme, sala: Sala, horario: str, preco: float):
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")

        self.__filme = filme
        self.__sala = sala
        self.__horario = horario
        self.__preco = preco
        self.__assentos_vendidos = []

    def vender_assento(self, assento: Assento):
        if len(self.__assentos_vendidos) >= self.__sala.get_capacidade():
            raise Exception("A sessão está lotada.")

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

    def get_sala(self):
        return self.__sala

    def get_filme(self):
        return self.__filme

    def get_duracao(self):
        return self.__filme.get_duracao()


class Programacao():
    __salas: dict[int, Sala]
    __sessoes: dict[int, list[Sessao]]
    __limite_salas: int
    __limite_sessoes: int

    def __init__(self):
        self.__salas = {}
        self.__sessoes = {}
        self.__limite_salas = 5
        self.__limite_sessoes = 5

    def cadastrar_sala(self, sala: Sala):
        numero = sala.get_numero()

        if len(self.__salas) >= self.__limite_salas:
            raise ValueError("O cinema atingiu o limite de 5 salas.")

        if numero in self.__salas:
            raise ValueError("Essa sala já está cadastrada.")

        self.__salas[numero] = sala
        self.__sessoes[numero] = []

        return "Sala cadastrada com sucesso!"

    def buscar_sala(self, numero: int):
        if numero not in self.__salas:
            raise ValueError("Sala não encontrada.")

        return self.__salas[numero]

    def buscar_sessao(self, numero_sala: int, numero_sessao: int):
        if numero_sala not in self.__sessoes:
            raise ValueError("Sala não encontrada.")

        if numero_sessao < 1 or numero_sessao > len(self.__sessoes[numero_sala]):
            raise ValueError("Sessão não encontrada.")

        return self.__sessoes[numero_sala][numero_sessao - 1]

    def cadastrar_sessao(self, sessao: Sessao):
        sala = sessao.get_sala()
        numero = sala.get_numero()

        if numero not in self.__salas:
            raise ValueError("Cadastre a sala antes de cadastrar uma sessão.")

        if self.__salas[numero] is not sala:
            raise ValueError("A sessão não pertence à sala cadastrada.")

        if len(self.__sessoes[numero]) >= self.__limite_sessoes:
            raise ValueError("Essa sala já possui 5 sessões cadastradas.")

        try:
            partes = sessao.get_horario().split(":")
            horas = int(partes[0])
            minutos = int(partes[1])

            if len(partes) != 2 or horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                raise ValueError

        except (ValueError, IndexError):
            raise ValueError("Horário inválido! Utilize o formato HH:MM.")

        inicio_novo = horas * 60 + minutos
        duracao_nova = sessao.get_duracao()

        if duracao_nova <= 0 or duracao_nova > 1440:
            raise ValueError("A duração do filme deve ser maior que zero e até 24 horas.")

        fim_novo = inicio_novo + duracao_nova

        for sessao_existente in self.__sessoes[numero]:
            partes_existente = sessao_existente.get_horario().split(":")
            inicio_existente = int(partes_existente[0]) * 60 + int(partes_existente[1])
            fim_existente = inicio_existente + sessao_existente.get_duracao()

            # Verifica também sessões que passam da meia-noite.
            for deslocamento in [-1440, 0, 1440]:
                inicio_comparado = inicio_existente + deslocamento
                fim_comparado = fim_existente + deslocamento

                if inicio_novo < fim_comparado and inicio_comparado < fim_novo:
                    raise ValueError(
                        "Conflito de horário! Já existe uma sessão nesse período na mesma sala."
                    )

        self.__sessoes[numero].append(sessao)
        return "Sessão cadastrada com sucesso!"

    def exibir_programacao(self):
        texto = "\n========== PROGRAMAÇÃO DO CINEMA =========="

        if not self.__salas:
            return texto + "\nNenhuma sala cadastrada."

        for numero in self.__salas:
            texto += f"\n\nSala {numero}"
            texto += f"\nSessões cadastradas: {len(self.__sessoes[numero])}"

            if not self.__sessoes[numero]:
                texto += "\nNenhuma sessão cadastrada."
                continue

            for posicao, sessao in enumerate(self.__sessoes[numero], 1):
                texto += (
                    f"\n  Sessão {posicao} - "
                    f"Filme: {sessao.get_filme().get_titulo()} | "
                    f"Horário: {sessao.get_horario()} | "
                    f"Duração: {sessao.get_duracao()} min"
                )

        return texto


class Ingresso:
    def __init__(self, sessao: Sessao, assento: Assento):
        sessao.vender_assento(assento)

        self.sessao = sessao
        self.assento = assento
        self.preco = sessao.get_preco()

    def calcular_preco(self):
        return self.preco

    def exibir_info(self):
        print(self.sessao.get_filme().exibir_info())
        print(f"Horário da Sessão: {self.sessao.get_horario()}")
        print(self.assento.identificarAssento())
        print(f"Valor: R$ {self.calcular_preco():.2f}")


class IngressoMeia(Ingresso):
    def __init__(self, sessao: Sessao, assento: Assento, comprovante: str):
        super().__init__(sessao, assento)
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