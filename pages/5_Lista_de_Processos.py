import streamlit as st

from database.processosdb import processos


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Processos em Curso",
    page_icon="📋",
    layout="wide"
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("📋 Processos em Curso")

st.write(
    "Lista de todos os processos que se encontram atualmente "
    "em curso no sistema."
)

st.divider()


# ============================================================
# FILTRAR PROCESSOS EM CURSO
# ============================================================

processos_em_curso = [
    processo
    for processo in processos
    if processo.get("estado") == "Em curso"
]


# ============================================================
# RESUMO
# ============================================================

total = len(processos_em_curso)

st.metric(
    "Processos em curso",
    total
)

st.divider()


# ============================================================
# VERIFICAR SE EXISTEM PROCESSOS
# ============================================================

if not processos_em_curso:

    st.info(
        "Não existem processos em curso neste momento."
    )

else:

    st.subheader(
        f"📁 {total} processo(s) em curso"
    )

    st.write("")


    # ========================================================
    # CABEÇALHO DA TABELA
    # ========================================================

    col1, col2, col3, col4, col5, col6 = st.columns(
        [1.2, 1, 2, 2, 1.5, 1]
    )

    with col1:
        st.write("**Processo**")

    with col2:
        st.write("**Letra**")

    with col3:
        st.write("**Autor**")

    with col4:
        st.write("**Réu**")

    with col5:
        st.write("**Secção**")

    with col6:
        st.write("**Ação**")


    st.divider()


    # ========================================================
    # LISTA DE PROCESSOS
    # ========================================================

    for indice, processo in enumerate(processos_em_curso):

        numero = processo.get(
            "numero",
            "-"
        )

        letra = processo.get(
            "letra",
            "-"
        )

        autor = processo.get(
            "autor",
            "-"
        )

        reu = processo.get(
            "reu",
            "-"
        )

        seccao = processo.get(
            "seccao",
            "-"
        )

        accao = processo.get(
            "accao",
            "-"
        )


        col1, col2, col3, col4, col5, col6 = st.columns(
            [1.2, 1, 2, 2, 1.5, 1]
        )

        with col1:
            st.write(numero)

        with col2:
            st.write(letra)

        with col3:
            st.write(autor)

        with col4:
            st.write(reu)

        with col5:
            st.write(seccao)

        with col6:

            if st.button(
                "Ver",
                key=f"ver_processo_{indice}",
                use_container_width=True
            ):

                st.session_state[
                    "processo_selecionado"
                ] = processo

        st.divider()


# ============================================================
# PROCESSO SELECIONADO
# ============================================================

if "processo_selecionado" in st.session_state:

    processo = st.session_state[
        "processo_selecionado"
    ]

    st.subheader("📄 Detalhes do Processo")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            "**Número:**",
            processo.get("numero", "-")
        )

        st.write(
            "**Letra:**",
            processo.get("letra", "-")
        )

        st.write(
            "**Ação:**",
            processo.get("accao", "-")
        )

        st.write(
            "**Autor:**",
            processo.get("autor", "-")
        )

        st.write(
            "**Réu:**",
            processo.get("reu", "-")
        )

    with col2:

        st.write(
            "**Escrivão:**",
            processo.get("escrivao", "-")
        )

        st.write(
            "**Juiz:**",
            processo.get("juiz", "-")
        )

        st.write(
            "**Secção:**",
            processo.get("seccao", "-")
        )

        st.write(
            "**Estado:**",
            processo.get("estado", "-")
        )

        st.write(
            "**Data de entrada:**",
            processo.get("data_entrada", "-")
        )


# ============================================================
# NAVEGAÇÃO
# ============================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "← Voltar ao início",
        use_container_width=True
    ):
        st.switch_page("app.py")


with col2:

    if st.button(
        "🔎 Consultar processo",
        use_container_width=True
    ):
        st.switch_page(
            "pages/4_Consultar_Processo.py"
        )


with col3:

    if st.button(
        "➕ Adicionar processo",
        use_container_width=True
    ):
        st.switch_page(
            "pages/1_Adicionar_Processo.py"
        )