import tkinter as tk
from tkinter import ttk, messagebox

from cinema import (
    Filme, Sala, Sessao, Assento,
    Ingresso, IngressoMeia
)


class CinemaApp:

    def __init__(self, root, programacao, bar, pedido, salvar_callback):

        self.root = root
        self.programacao = programacao
        self.bar = bar
        self.pedido = pedido
        self.salvar_callback = salvar_callback

        self.cor_vinho = "#641E2B"
        self.cor_vermelho = "#9E2633"
        self.cor_hover = "#E2D6C4"
        self.cor_fundo = "#F2EEE5"
        self.cor_branco = "#FFFFFF"
        self.cor_texto = "#252D30"
        self.cor_verde = "#386641"
        self.cor_ocupado = "#641E2B"
        self.cor_disponivel = "#E8E2D8"

        self.sessao_selecionada = None
        self.assento_selecionado = None
        self.botoes_assentos = {}

        self.root.title("CINEPOO - Sistema de Cinema")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.configure(bg=self.cor_fundo)

        self.criar_layout()
        self.mostrar_inicio()

    def salvar(self):
        self.salvar_callback(
            self.programacao,
            self.bar,
            self.pedido
        )

    # ==========================================
    # ESTRUTURA PRINCIPAL
    # ==========================================

    def criar_layout(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=self.cor_vinho,
            width=230
        )

        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="CINEPOO",
            font=("Arial", 23, "bold"),
            bg=self.cor_vinho,
            fg=self.cor_fundo
        ).pack(pady=(35, 5))

        tk.Label(
            self.sidebar,
            text="SISTEMA DE CINEMA",
            font=("Arial", 9),
            bg=self.cor_vinho,
            fg=self.cor_fundo
        ).pack(pady=(0, 40))

        self.criar_botao_menu("Início", self.mostrar_inicio)
        self.criar_botao_menu("Programação", self.mostrar_programacao)
        self.criar_botao_menu("Bilheteria", self.mostrar_bilheteria)
        self.criar_botao_menu("Snack Bar", self.mostrar_snackbar)

        self.area_principal = tk.Frame(
            self.root,
            bg=self.cor_fundo
        )

        self.area_principal.pack(
            side="right",
            fill="both",
            expand=True
        )

    def criar_botao_menu(self, texto, comando):

        botao = tk.Frame(
            self.sidebar,
            bg=self.cor_fundo,
            cursor="hand2"
        )

        botao.pack(fill="x", padx=15, pady=6)

        label = tk.Label(
            botao,
            text=texto,
            font=("Arial", 12, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_vinho,
            anchor="w",
            padx=25,
            pady=15,
            cursor="hand2"
        )

        label.pack(fill="both")

        def entrar(event):
            botao.configure(bg=self.cor_hover)
            label.configure(bg=self.cor_hover)

        def sair(event):
            botao.configure(bg=self.cor_fundo)
            label.configure(bg=self.cor_fundo)

        def clicar(event):
            comando()

        for widget in (botao, label):
            widget.bind("<Enter>", entrar)
            widget.bind("<Leave>", sair)
            widget.bind("<Button-1>", clicar)

    def limpar_area(self):

        for widget in self.area_principal.winfo_children():
            widget.destroy()

    def criar_titulo(self, titulo, descricao):

        tk.Label(
            self.area_principal,
            text=titulo,
            font=("Arial", 24, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_vinho
        ).pack(anchor="w", padx=35, pady=(35, 5))

        tk.Label(
            self.area_principal,
            text=descricao,
            font=("Arial", 11),
            bg=self.cor_fundo,
            fg=self.cor_texto
        ).pack(anchor="w", padx=35, pady=(0, 25))

    def criar_botao(self, pai, texto, comando):

        botao = tk.Label(
            pai,
            text=texto,
            font=("Arial", 10, "bold"),
            bg=self.cor_vinho,
            fg=self.cor_branco,
            padx=15,
            pady=10,
            cursor="hand2"
        )

        botao.pack(side="left", padx=5)

        botao.bind("<Button-1>", lambda event: comando())

        botao.bind(
            "<Enter>",
            lambda event: botao.configure(bg=self.cor_vermelho)
        )

        botao.bind(
            "<Leave>",
            lambda event: botao.configure(bg=self.cor_vinho)
        )

        return botao

    def criar_card(self, pai):

        return tk.Frame(
            pai,
            bg=self.cor_branco,
            highlightbackground="#D8CFC3",
            highlightthickness=1,
            padx=15,
            pady=15
        )

    def criar_campo(self, pai, texto):

        tk.Label(
            pai,
            text=texto,
            font=("Arial", 10, "bold"),
            bg=self.cor_branco,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(8, 3))

        campo = tk.Entry(
            pai,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        campo.pack(fill="x", ipady=6)

        return campo

    def criar_combo(self, pai, texto, valores):

        tk.Label(
            pai,
            text=texto,
            font=("Arial", 10, "bold"),
            bg=self.cor_branco,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(8, 3))

        combo = ttk.Combobox(
            pai,
            values=valores,
            state="readonly",
            font=("Arial", 10)
        )

        combo.pack(fill="x", ipady=4)

        return combo

    def criar_area_texto(self, pai, altura=10):

        texto = tk.Text(
            pai,
            height=altura,
            font=("Arial", 10),
            bg=self.cor_branco,
            fg=self.cor_texto,
            relief="flat",
            wrap="word",
            padx=10,
            pady=10
        )

        texto.pack(fill="both", expand=True)

        return texto

    def criar_janela_formulario(self, titulo, largura, altura):

        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry(f"{largura}x{altura}")
        janela.configure(bg=self.cor_branco)
        janela.resizable(False, False)
        janela.transient(self.root)
        janela.grab_set()

        container = tk.Frame(
            janela,
            bg=self.cor_branco,
            padx=25,
            pady=20
        )

        container.pack(fill="both", expand=True)

        tk.Label(
            container,
            text=titulo,
            font=("Arial", 17, "bold"),
            bg=self.cor_branco,
            fg=self.cor_vinho
        ).pack(anchor="w", pady=(0, 12))

        return container, janela

    # ==========================================
    # INÍCIO
    # ==========================================

    def mostrar_inicio(self):

        self.limpar_area()

        self.criar_titulo(
            "Bem-vindo ao CINEPOO!",
            "Gerencie as atividades do cinema."
        )

        container = tk.Frame(
            self.area_principal,
            bg=self.cor_fundo
        )

        container.pack(fill="both", expand=True, padx=35)

        areas = [
            ("FILMES E SESSÕES", "Gerencie a programação"),
            ("BILHETERIA", "Realize vendas de ingressos"),
            ("SNACK BAR", "Gerencie produtos e pedidos")
        ]

        comandos = [
            self.mostrar_programacao,
            self.mostrar_bilheteria,
            self.mostrar_snackbar
        ]

        for (titulo, descricao), comando in zip(areas, comandos):

            card = self.criar_card(container)
            card.pack(fill="x", pady=10)

            tk.Label(
                card,
                text=titulo,
                font=("Arial", 14, "bold"),
                bg=self.cor_branco,
                fg=self.cor_vermelho
            ).pack(anchor="w")

            tk.Label(
                card,
                text=descricao,
                font=("Arial", 11),
                bg=self.cor_branco,
                fg=self.cor_texto
            ).pack(anchor="w", pady=5)

            self.criar_botao(card, "Acessar", comando)

    # ==========================================
    # PROGRAMAÇÃO
    # ==========================================

    def obter_salas(self):
        return self.programacao.listar_salas()

    def obter_sessoes(self):
        return self.programacao.listar_sessoes()

    def mostrar_programacao(self):

        self.limpar_area()

        self.criar_titulo(
            "Programação",
            "Consulte e gerencie filmes, salas e sessões."
        )

        botoes = tk.Frame(
            self.area_principal,
            bg=self.cor_fundo
        )

        botoes.pack(fill="x", padx=35, pady=(0, 15))

        self.criar_botao(botoes, "Cadastrar filme", self.formulario_filme)
        self.criar_botao(botoes, "Cadastrar sala", self.formulario_sala)
        self.criar_botao(botoes, "Cadastrar sessão", self.formulario_sessao)

        container = tk.Frame(
            self.area_principal,
            bg=self.cor_fundo
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 25)
        )

        quadro = self.criar_card(container)
        quadro.pack(fill="both", expand=True)

        tk.Label(
            quadro,
            text="FILMES CADASTRADOS",
            font=("Arial", 13, "bold"),
            bg=self.cor_branco,
            fg=self.cor_vinho
        ).pack(anchor="w", pady=(0, 8))

        for filme in self.programacao.listar_filmes():

            tk.Label(
                quadro,
                text=filme.exibir_info(),
                font=("Arial", 10),
                bg=self.cor_branco,
                fg=self.cor_texto,
                justify="left"
            ).pack(anchor="w", pady=5)

            ttk.Separator(
                quadro,
                orient="horizontal"
            ).pack(fill="x", pady=5)

        tk.Label(
            quadro,
            text="PROGRAMAÇÃO DAS SESSÕES",
            font=("Arial", 13, "bold"),
            bg=self.cor_branco,
            fg=self.cor_vinho
        ).pack(anchor="w", pady=(15, 8))

        texto = self.criar_area_texto(quadro, 8)
        texto.insert("1.0", self.programacao.exibir_programacao())
        texto.configure(state="disabled")

    def formulario_filme(self):

        janela, popup = self.criar_janela_formulario(
            "Cadastrar filme", 400, 440
        )

        titulo = self.criar_campo(janela, "Nome do filme")
        duracao = self.criar_campo(janela, "Duração em minutos")
        genero = self.criar_campo(janela, "Gênero")
        classificacao = self.criar_campo(
            janela, "Classificação indicativa"
        )

        def salvar():

            try:
                filme = Filme(
                    titulo.get().strip(),
                    int(duracao.get()),
                    genero.get().strip(),
                    int(classificacao.get())
                )

                resultado = self.programacao.cadastrar_filme(filme)
                self.salvar()

                messagebox.showinfo("Sucesso", resultado)
                popup.destroy()
                self.mostrar_programacao()

            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        self.criar_botao(janela, "Salvar filme", salvar)

    def formulario_sala(self):

        janela, popup = self.criar_janela_formulario(
            "Cadastrar sala", 400, 300
        )

        numero = self.criar_campo(janela, "Número da sala")
        capacidade = self.criar_campo(janela, "Capacidade")

        def salvar():

            try:
                sala = Sala(
                    int(numero.get()),
                    int(capacidade.get())
                )

                resultado = self.programacao.cadastrar_sala(sala)
                self.salvar()

                messagebox.showinfo("Sucesso", resultado)
                popup.destroy()
                self.mostrar_programacao()

            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        self.criar_botao(janela, "Salvar sala", salvar)

    def formulario_sessao(self):

        filmes = self.programacao.listar_filmes()
        salas = self.obter_salas()

        if not filmes:
            messagebox.showwarning(
                "Atenção",
                "Cadastre um filme antes de cadastrar uma sessão."
            )
            return

        if not salas:
            messagebox.showwarning(
                "Atenção",
                "Cadastre uma sala antes de cadastrar uma sessão."
            )
            return

        janela, popup = self.criar_janela_formulario(
            "Cadastrar sessão", 420, 440
        )

        mapa_filmes = {
            filme.get_titulo(): filme for filme in filmes
        }

        mapa_salas = {
            str(sala.get_numero()): sala for sala in salas
        }

        filme = self.criar_combo(
            janela, "Filme", list(mapa_filmes.keys())
        )

        sala = self.criar_combo(
            janela, "Sala", list(mapa_salas.keys())
        )

        horario = self.criar_campo(janela, "Horário (HH:MM)")
        preco = self.criar_campo(janela, "Preço do ingresso")

        def salvar():

            try:
                filme_escolhido = mapa_filmes[filme.get()]
                sala_escolhida = mapa_salas[sala.get()]

                sessao = Sessao(
                    filme_escolhido,
                    sala_escolhida,
                    horario.get().strip(),
                    float(preco.get().replace(",", "."))
                )

                resultado = self.programacao.cadastrar_sessao(sessao)
                self.salvar()

                messagebox.showinfo("Sucesso", resultado)
                popup.destroy()
                self.mostrar_programacao()

            except (ValueError, KeyError) as erro:
                messagebox.showerror("Erro", str(erro))

        self.criar_botao(janela, "Salvar sessão", salvar)

    # ==========================================
    # BILHETERIA
    # ==========================================

    def mostrar_bilheteria(self):

        self.limpar_area()

        self.criar_titulo(
            "Bilheteria",
            "Escolha uma sessão e selecione seu assento."
        )

        container = tk.Frame(
            self.area_principal,
            bg=self.cor_fundo
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 25)
        )

        quadro = self.criar_card(container)
        quadro.pack(fill="x", pady=(0, 15))

        sessoes = self.obter_sessoes()

        if not sessoes:
            tk.Label(
                quadro,
                text="Não existem sessões cadastradas.",
                bg=self.cor_branco,
                fg=self.cor_texto
            ).pack(anchor="w")
            return

        opcoes = [
            f"Sala {numero_sala} - Sessão {numero_sessao} - "
            f"{sessao.get_filme().get_titulo()} - {sessao.get_horario()}"
            for numero_sala, numero_sessao, sessao in sessoes
        ]

        self.mapa_sessoes = {
            opcao: item for opcao, item in zip(opcoes, sessoes)
        }

        self.combo_sessoes = self.criar_combo(
            quadro, "Selecione a sessão", opcoes
        )

        self.combo_sessoes.bind(
            "<<ComboboxSelected>>",
            self.selecionar_sessao
        )

        self.quadro_assentos = self.criar_card(container)
        self.quadro_assentos.pack(fill="both", expand=True)

        tk.Label(
            self.quadro_assentos,
            text="SELECIONE SEU ASSENTO",
            font=("Arial", 13, "bold"),
            bg=self.cor_branco,
            fg=self.cor_vinho
        ).pack(pady=10)

        self.label_assento = tk.Label(
            self.quadro_assentos,
            text="Escolha uma sessão primeiro.",
            bg=self.cor_branco,
            fg=self.cor_texto
        )

        self.label_assento.pack(pady=5)

        self.grade_assentos = tk.Frame(
            self.quadro_assentos,
            bg=self.cor_branco
        )

        self.grade_assentos.pack(pady=10)

        legenda = tk.Frame(
            self.quadro_assentos,
            bg=self.cor_branco
        )

        legenda.pack(pady=5)

        tk.Label(
            legenda,
            text="  Disponível  ",
            bg=self.cor_disponivel,
            fg=self.cor_texto,
            padx=5
        ).pack(side="left", padx=5)

        tk.Label(
            legenda,
            text="  Selecionado  ",
            bg=self.cor_vermelho,
            fg=self.cor_branco,
            padx=5
        ).pack(side="left", padx=5)

        tk.Label(
            legenda,
            text="  Ocupado  ",
            bg=self.cor_ocupado,
            fg=self.cor_branco,
            padx=5
        ).pack(side="left", padx=5)

        self.tipo_ingresso = tk.StringVar(value="Inteira")

        tk.Label(
            self.quadro_assentos,
            text="Tipo de ingresso:",
            bg=self.cor_branco,
            fg=self.cor_texto
        ).pack(pady=(10, 3))

        combo_tipo = ttk.Combobox(
            self.quadro_assentos,
            textvariable=self.tipo_ingresso,
            values=["Inteira", "Meia-entrada"],
            state="readonly"
        )

        combo_tipo.pack()
        combo_tipo.bind("<<ComboboxSelected>>", self.alterar_tipo_ingresso)

        self.area_comprovante = tk.Frame(
            self.quadro_assentos,
            bg=self.cor_branco
        )

        self.label_comprovante = tk.Label(
            self.area_comprovante,
            text="Tipo de comprovante:",
            bg=self.cor_branco,
            fg=self.cor_texto
        )

        self.campo_comprovante = tk.Entry(
            self.area_comprovante,
            font=("Arial", 10),
            width=35
        )

        self.criar_botao(
            self.quadro_assentos,
            "Comprar ingresso",
            self.comprar_ingresso
        )

    def selecionar_sessao(self, event=None):

        opcao = self.combo_sessoes.get()

        if opcao not in self.mapa_sessoes:
            return

        _, _, sessao = self.mapa_sessoes[opcao]

        self.sessao_selecionada = sessao
        self.assento_selecionado = None

        self.label_assento.configure(
            text=(
                f"{sessao.get_filme().get_titulo()} | "
                f"{sessao.get_horario()} | "
                f"R$ {sessao.get_preco():.2f}"
            )
        )

        for widget in self.grade_assentos.winfo_children():
            widget.destroy()

        tk.Label(
            self.grade_assentos,
            text="TELA",
            bg=self.cor_vinho,
            fg=self.cor_branco,
            font=("Arial", 10, "bold"),
            width=50,
            pady=5
        ).grid(row=0, column=0, columnspan=11, pady=(0, 15))

        self.botoes_assentos = {}

        ocupados = {
            assento.identificarAssento().replace("Seu assento é o ", "")
            for assento in sessao.listar_assentos_vendidos()
        }

        for indice, fileira in enumerate("ABCDE", 1):

            tk.Label(
                self.grade_assentos,
                text=fileira,
                bg=self.cor_branco,
                fg=self.cor_vinho,
                font=("Arial", 10, "bold")
            ).grid(row=indice, column=0, padx=5)

            for numero in range(1, 11):

                identificador = f"{fileira}{numero}"
                esta_ocupado = identificador in ocupados

                botao = tk.Label(
                    self.grade_assentos,
                    text=str(numero),
                    bg=(
                        self.cor_ocupado
                        if esta_ocupado
                        else self.cor_disponivel
                    ),
                    fg=(
                        self.cor_branco
                        if esta_ocupado
                        else self.cor_texto
                    ),
                    width=3,
                    pady=6,
                    cursor="arrow" if esta_ocupado else "hand2"
                )

                botao.grid(
                    row=indice,
                    column=numero,
                    padx=3,
                    pady=3
                )

                if not esta_ocupado:
                    botao.bind(
                        "<Button-1>",
                        lambda event, a=identificador: self.escolher_assento(a)
                    )

                self.botoes_assentos[identificador] = botao

        self.area_comprovante.pack_forget()

        if self.tipo_ingresso.get() == "Meia-entrada":
            self.area_comprovante.pack(pady=5)
            self.label_comprovante.pack(anchor="w")
            self.campo_comprovante.pack(pady=4)

    def escolher_assento(self, assento):

        if self.assento_selecionado:
            botao_anterior = self.botoes_assentos[
                self.assento_selecionado
            ]

            botao_anterior.configure(
                bg=self.cor_disponivel,
                fg=self.cor_texto
            )

        self.assento_selecionado = assento

        self.botoes_assentos[assento].configure(
            bg=self.cor_vermelho,
            fg=self.cor_branco
        )

        self.label_assento.configure(
            text=f"Assento selecionado: {assento}"
        )

    def alterar_tipo_ingresso(self, event=None):

        if self.tipo_ingresso.get() == "Meia-entrada":
            self.area_comprovante.pack(pady=5)
            self.label_comprovante.pack(anchor="w")
            self.campo_comprovante.pack(pady=4)
        else:
            self.area_comprovante.pack_forget()

    def comprar_ingresso(self):

        if not self.sessao_selecionada:
            messagebox.showwarning(
                "Atenção", "Selecione uma sessão."
            )
            return

        if not self.assento_selecionado:
            messagebox.showwarning(
                "Atenção", "Selecione um assento."
            )
            return

        try:
            fileira = self.assento_selecionado[0]
            numero = int(self.assento_selecionado[1:])

            assento = Assento(fileira, numero)

            comprovante = ""

            if self.tipo_ingresso.get() == "Meia-entrada":

                comprovante = self.campo_comprovante.get().strip()

                if not comprovante:
                    raise ValueError(
                        "Informe o tipo de comprovante da meia-entrada."
                    )

                ingresso = IngressoMeia(
                    self.sessao_selecionada,
                    assento,
                    comprovante
                )

            else:
                ingresso = Ingresso(
                    self.sessao_selecionada,
                    assento
                )

            valor = ingresso.calcular_preco()

            self.salvar()

            detalhes = (
                f"Compra realizada com sucesso!\n\n"
                f"Filme: {self.sessao_selecionada.get_filme().get_titulo()}\n"
                f"Sessão: {self.sessao_selecionada.get_horario()}\n"
                f"Assento: {self.assento_selecionado}\n"
                f"Tipo: {self.tipo_ingresso.get()}\n"
            )

            if comprovante:
                detalhes += f"Comprovante: {comprovante}\n"

            detalhes += f"Valor: R$ {valor:.2f}"

            messagebox.showinfo("Ingresso comprado!", detalhes)

            self.selecionar_sessao()

        except Exception as erro:
            messagebox.showerror("Erro na compra", str(erro))

    # ==========================================
    # SNACK BAR
    # ==========================================

    def obter_produtos(self):
        return self.bar.listar_produtos()

    def mostrar_snackbar(self):

        self.limpar_area()

        self.criar_titulo(
            "Snack Bar",
            "Consulte o cardápio e gerencie seu pedido."
        )

        container = tk.Frame(
            self.area_principal,
            bg=self.cor_fundo
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 25)
        )

        esquerda = tk.Frame(container, bg=self.cor_fundo)
        esquerda.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        direita = tk.Frame(container, bg=self.cor_fundo)
        direita.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        card_cardapio = self.criar_card(esquerda)
        card_cardapio.pack(fill="both", expand=True)

        tk.Label(
            card_cardapio,
            text="CARDÁPIO",
            font=("Arial", 14, "bold"),
            bg=self.cor_branco,
            fg=self.cor_vinho
        ).pack(anchor="w", pady=(0, 10))

        self.lista_produtos = tk.Listbox(
            card_cardapio,
            font=("Arial", 10),
            bg=self.cor_branco,
            fg=self.cor_texto,
            selectbackground=self.cor_vinho,
            height=10
        )

        self.lista_produtos.pack(fill="both", expand=True)

        self.produtos_exibidos = self.obter_produtos()

        for produto in self.produtos_exibidos:

            status = (
                f"Estoque: {produto.estoque}"
                if produto.estoque > 0
                else "ESGOTADO"
            )

            self.lista_produtos.insert(
                tk.END,
                f"{produto.id} - {produto.nome} | "
                f"R$ {produto.preco:.2f} | {status}"
            )

        tk.Label(
            card_cardapio,
            text="Quantidade:",
            bg=self.cor_branco,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(10, 3))

        self.quantidade_produto = tk.Entry(
            card_cardapio,
            font=("Arial", 11)
        )

        self.quantidade_produto.insert(0, "1")
        self.quantidade_produto.pack(fill="x", ipady=5)

        self.criar_botao(
            card_cardapio,
            "Adicionar ao pedido",
            self.adicionar_ao_pedido
        )

        card_pedido = self.criar_card(direita)
        card_pedido.pack(fill="both", expand=True)

        tk.Label(
            card_pedido,
            text="SEU PEDIDO",
            font=("Arial", 14, "bold"),
            bg=self.cor_branco,
            fg=self.cor_vinho
        ).pack(anchor="w", pady=(0, 10))

        self.texto_pedido = self.criar_area_texto(card_pedido, 12)
        self.atualizar_pedido()

        tk.Label(
            card_pedido,
            text="ID do produto para remover:",
            bg=self.cor_branco,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(10, 3))

        self.id_remover = tk.Entry(card_pedido, font=("Arial", 11))
        self.id_remover.pack(fill="x", ipady=5)

        tk.Label(
            card_pedido,
            text="Quantidade:",
            bg=self.cor_branco,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(8, 3))

        self.quantidade_remover = tk.Entry(
            card_pedido,
            font=("Arial", 11)
        )

        self.quantidade_remover.insert(0, "1")
        self.quantidade_remover.pack(fill="x", ipady=5)

        botoes = tk.Frame(card_pedido, bg=self.cor_branco)
        botoes.pack(fill="x", pady=10)

        self.criar_botao(
            botoes,
            "Remover item",
            self.remover_do_pedido
        )

        self.criar_botao(
            botoes,
            "Finalizar pedido",
            self.finalizar_pedido
        )

    def adicionar_ao_pedido(self):

        try:
            selecao = self.lista_produtos.curselection()

            if not selecao:
                raise ValueError("Selecione um produto.")

            produto = self.produtos_exibidos[selecao[0]]
            quantidade = int(self.quantidade_produto.get())

            self.pedido.adicionar_item(produto.id, quantidade)
            self.salvar()

            messagebox.showinfo(
                "Sucesso",
                "Produto adicionado ao pedido!"
            )

            self.mostrar_snackbar()

        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def remover_do_pedido(self):

        try:
            identificador = int(self.id_remover.get())
            quantidade = int(self.quantidade_remover.get())

            self.pedido.remover_item(identificador, quantidade)
            self.salvar()

            messagebox.showinfo(
                "Sucesso",
                "Produto removido do pedido!"
            )

            self.mostrar_snackbar()

        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def atualizar_pedido(self):

        self.texto_pedido.configure(state="normal")
        self.texto_pedido.delete("1.0", tk.END)

        self.texto_pedido.insert(
            "1.0",
            self.pedido.exibir_pedido()
        )

        self.texto_pedido.configure(state="disabled")

    def finalizar_pedido(self):

        try:
            resultado = self.pedido.finalizar_pedido()
            self.salvar()

            messagebox.showinfo(
                "Pedido finalizado",
                resultado
            )

            self.mostrar_snackbar()

        except Exception as erro:
            messagebox.showerror("Erro", str(erro))