"""Leitura dos arquivos CSV do projeto.
"""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

# Tradução da nota em texto para número.
NOTAS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
}


def ler_livros():
    """Lê o CSV de livros e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros


def converter_preco(preco_texto, cotacao=1.0):
    """Converte o preço em texto ("£51.77") para número (51.77).

    A cotação é opcional: sem ela, devolve o valor em libras.
    """
    valor = float(preco_texto.replace("£", ""))
    return valor * cotacao


def converter_nota(nota_texto):
    """Converte a nota em texto ("Five") para número (5)."""
    return NOTAS.get(nota_texto.lower().strip(), 0)


def calcular_preco_medio(livros):
    """Soma os preços de todos os livros e divide pelo total."""
    soma = 0.0
    for livro in livros:
        soma = soma + converter_preco(livro["preco"])
    return soma / len(livros)


def contar_cinco_estrelas(livros):
    """Conta quantos livros têm nota 5."""
    contador = 0
    for livro in livros:
        if converter_nota(livro["nota"]) == 5:
            contador += 1
    return contador


def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço."""
    mais_caro = livros[0]
    for livro in livros:
        if converter_preco(livro["preco"]) > converter_preco(mais_caro["preco"]):
            mais_caro = livro
    return mais_caro


if __name__ == "__main__":
    livros = ler_livros()
    print(f"Li {len(livros)} livros.")
    print("Primeiro livro:", livros[0])
