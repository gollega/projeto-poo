from cinema import *

if __name__ == "__main__":
    filme1 = Filme("Interestelar", 169, "Ficção científica", 10)
    assento1 = Assento("A", 12)

    print("=== INFORMAÇÕES DO FILME ===")
    print(filme1.exibir_info())

    print("\n=== IDENTIFICAÇÃO DO ASSENTO ===")
    print(assento1.identificarAssento())