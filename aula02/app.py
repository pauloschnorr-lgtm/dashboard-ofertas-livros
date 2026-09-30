"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

# Cotação usada para mostrar os preços em reais.
# É uma decisão de apresentação, por isso fica aqui no app,
# e não dentro do dados.py.
COTACAO_LIBRA_REAL = 6.90


def nota_em_estrelas(nota):
    """Transforma a nota em estrelas: '★★★★☆'."""
    numero = dados.converter_nota(nota)
    return "★" * numero + "☆" * (5 - numero)


def montar_tabela(livros):
    """Monta a lista que vai para a tabela, com a nota em estrelas."""
    linhas = []
    for livro in livros:
        linhas.append({
            "titulo": livro["titulo"],
            "preco": livro["preco"],
            "nota": nota_em_estrelas(livro["nota"]),
            "categoria": livro["categoria"],
            "url": livro["url"],
        })
    return linhas


def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    livros = dados.ler_livros()

    col1, col2, col3, col4 = st.columns(4)

    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")
    col2.caption(f"≈ R$ {dados.converter_preco(f'£{preco_medio:.2f}', COTACAO_LIBRA_REAL):.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", mais_caro["preco"])
    col4.caption(f"{mais_caro['titulo']} · ≈ R$ {dados.converter_preco(mais_caro['preco'], COTACAO_LIBRA_REAL):.2f}")

    st.dataframe(montar_tabela(livros))


if __name__ == "__main__":
    main()
