from cinema import *

if __name__ == "__main__":
    filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
    assento1 = Assento("A", 12)

    sala1 = Sala(1, 50)
    sala1.adicionarAssento(assento1)

    sessao1 = Sessão(filme1, sala1, "19:30", 30.00)

    print("=== INFORMAÇÕES DO FILME ===")
    print(filme1.exibir_info())

    print("\n=== IDENTIFICAÇÃO DO ASSENTO ===")
    print(assento1.identificarAssento())

    print("\n=== INFORMAÇÕES DA SALA ===")
    print(sala1.exibir_info())

    print("\n=== INFORMAÇÕES DA SESSÃO ===")
    print(sessao1.exibir_info())
