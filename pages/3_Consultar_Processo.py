import streamlit as st

from backend.pesquisar_processos import pesquisar_processo
from backend.exibir_processo import exibir_processo


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Consultar Processo",
    page_icon="🔎",
    layout="wide"
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🔎 Consultar Processo")

st.write(
    "Pesquise processos por número, autor ou réu."
)

st.divider()


# ============================================================
# CRITÉRIO DE PESQUISA
# ============================================================

st.subheader("Pesquisar Processo")

criterio = st.selectbox(
    "Pesquisar por",
    [
        "Número do processo",
        "Autor",
        "Réu"
    ]
)


# ============================================================
# CONVERTER CRITÉRIO
# ============================================================

if criterio == "Número do processo":

    criterio_backend = "numero"

    placeholder = "Ex.: 01/2026"

elif criterio == "Autor":

    criterio_backend = "autor"

    placeholder = "Ex.: João Manuel"

else:

    criterio_backend = "reu"

    placeholder = "Ex.: António José"


# ============================================================
# CAMPO DE PESQUISA
# ============================================================

valor = st.text_input(
    "Digite a informação",
    placeholder=placeholder
)


# ============================================================
# PESQUISA
# ============================================================

if st.button(
    "🔎 Pesquisar",
    use_container_width=True,
    type="primary"
):

    if not valor.strip():

        st.warning(
            "Digite uma informação para realizar a pesquisa."
        )

    else:

        resultados = pesquisar_processo(
            valor,
            criterio_backend
        )

        # Guardamos os resultados na sessão
        st.session_state["resultados_pesquisa"] = resultados

        # Limpamos processo selecionado anteriormente
        st.session_state.pop(
            "processo_selecionado",
            None
        )


# ============================================================
# RESULTADOS
# ============================================================

if "resultados_pesquisa" in st.session_state:

    resultados = st.session_state["resultados_pesquisa"]

    st.divider()

    if not resultados:

        st.warning(
            "Nenhum processo encontrado."
        )

    else:

        quantidade = len(resultados)

        st.subheader(
            f"📋 {quantidade} processo(s) encontrado(s)"
        )


        # ====================================================
        # LISTA DE RESULTADOS
        # ====================================================

        for indice, processo in enumerate(resultados):

            numero = processo.get(
                "numero",
                "Sem número"
            )

            autor = processo.get(
                "autor",
                "-"
            )

            reu = processo.get(
                "reu",
                "-"
            )

            estado = processo.get(
                "estado",
                "-"
            )

            col1, col2, col3, col4, col5 = st.columns(
                [1.2, 2, 2, 1.5, 1]
            )

            with col1:

                st.write(f"**{numero}**")

            with col2:

                st.write(autor)

            with col3:

                st.write(reu)

            with col4:

                st.write(estado)

            with col5:

                if st.button(
                    "Abrir",
                    key=f"abrir_{indice}",
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

    st.divider()

    exibir_processo(processo)


# ============================================================
# NAVEGAÇÃO
# ============================================================

st.divider()

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "← Voltar ao início",
        use_container_width=True
    ):

        st.switch_page("app.py")


with col2:

    if st.button(
        "➕ Adicionar processo",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Adicionar_Processo.py"
        )