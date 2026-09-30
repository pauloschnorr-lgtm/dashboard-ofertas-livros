"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

from dados import ler_livros


def calcular_preco_medio(livros):
    """Devolve o preço médio dos livros."""
    soma = 0.0
    for livro in livros:
        soma = soma + float(livro["preco"].replace("£", ""))
    return soma / len(livros)


def contar_cinco_estrelas(livros):
    """Conta quantos livros têm nota cinco."""
    total = 0
    for livro in livros:
        if livro["nota"] == "Five":
            total = total + 1
    return total


def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço."""
    mais_caro = livros[0]
    for livro in livros:
        preco = float(livro["preco"].replace("£", ""))
        preco_do_mais_caro = float(mais_caro["preco"].replace("£", ""))
        if preco > preco_do_mais_caro:
            mais_caro = livro
    return mais_caro


st.title("📚 Dashboard de Livros")

livros = ler_livros()
mais_caro = encontrar_mais_caro(livros)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de livros", len(livros))
col2.metric("Preço médio", f"£{calcular_preco_medio(livros):.2f}")
col3.metric("Livros com 5 estrelas", contar_cinco_estrelas(livros))
col4.metric("Livro mais caro", mais_caro["preco"])
col4.caption(mais_caro["titulo"])

st.dataframe(livros)
