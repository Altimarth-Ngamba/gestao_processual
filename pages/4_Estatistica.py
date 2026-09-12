import streamlit as st


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Relatórios e Estatísticas",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("📊 Relatórios e Estatísticas")

st.write(
    """
    Consulte informações estatísticas e gere relatórios
    relacionados à atividade processual.
    """
)

st.divider()


# ============================================================
# OPÇÕES PRINCIPAIS
# ============================================================

st.subheader("Escolha uma opção")


col1, col2 = st.columns(2)


# ============================================================
# GERAR RELATÓRIO
# ============================================================

with col1:

    st.subheader("📄 Gerar Relatório")

    st.write(
        """
        Gere relatórios com informações detalhadas sobre
        os processos e a atividade processual.
        """
    )

    if st.button(
        "📄 Gerar relatório",
        use_container_width=True,
        type="primary"
    ):

        st.session_state["relatorio_aberto"] = True
        st.session_state["mapas_abertos"] = False


# ============================================================
# MAPAS ESTATÍSTICOS
# ============================================================

with col2:

    st.subheader("📈 Mapas Estatísticos")

    st.write(
        """
        Consulte mapas estatísticos da atividade processual
        por trimestre ou semestre.
        """
    )

    if st.button(
        "📈 Abrir mapas estatísticos",
        use_container_width=True,
        type="primary"
    ):

        st.session_state["mapas_abertos"] = True
        st.session_state["relatorio_aberto"] = False


# ============================================================
# GERAR RELATÓRIO
# ============================================================

if st.session_state.get("relatorio_aberto", False):

    st.divider()

    st.header("📄 Gerar Relatório")

    st.write(
        "Selecione os critérios para gerar o relatório."
    )

    col1, col2 = st.columns(2)

    with col1:

        tipo_relatorio = st.selectbox(
            "Tipo de relatório",
            [
                "Todos os processos",
                "Processos em curso",
                "Processos julgados",
                "Processos arquivados"
            ]
        )

    with col2:

        ano = st.selectbox(
            "Ano",
            [
                2026,
                2025,
                2024,
                2023
            ]
        )

    st.write("")

    if st.button(
        "Gerar relatório",
        use_container_width=True
    ):

        st.info(
            "Módulo de geração de relatórios em desenvolvimento."
        )


# ============================================================
# MAPAS ESTATÍSTICOS
# ============================================================

if st.session_state.get("mapas_abertos", False):

    st.divider()

    st.header("📈 Mapas Estatísticos")

    st.write(
        "Escolha o período que deseja analisar."
    )

    periodo = st.radio(
        "Período",
        [
            "Trimestral",
            "Semestral"
        ],
        horizontal=True
    )


    # ========================================================
    # TRIMESTRAL
    # ========================================================

    if periodo == "Trimestral":

        st.subheader("📅 Mapa Trimestral")

        col1, col2 = st.columns(2)

        with col1:

            ano = st.selectbox(
                "Ano",
                [
                    2026,
                    2025,
                    2024,
                    2023
                ],
                key="ano_trimestral"
            )

        with col2:

            trimestre = st.selectbox(
                "Trimestre",
                [
                    "1.º Trimestre — Janeiro a Março",
                    "2.º Trimestre — Abril a Junho",
                    "3.º Trimestre — Julho a Setembro",
                    "4.º Trimestre — Outubro a Dezembro"
                ]
            )

        st.write("")

        if st.button(
            "📊 Gerar mapa trimestral",
            use_container_width=True
        ):

            st.info(
                f"Mapa do {trimestre} de {ano} "
                "em desenvolvimento."
            )


    # ========================================================
    # SEMESTRAL
    # ========================================================

    else:

        st.subheader("📅 Mapa Semestral")

        col1, col2 = st.columns(2)

        with col1:

            ano = st.selectbox(
                "Ano",
                [
                    2026,
                    2025,
                    2024,
                    2023
                ],
                key="ano_semestral"
            )

        with col2:

            semestre = st.selectbox(
                "Semestre",
                [
                    "1.º Semestre — Janeiro a Junho",
                    "2.º Semestre — Julho a Dezembro"
                ]
            )

        st.write("")

        if st.button(
            "📊 Gerar mapa semestral",
            use_container_width=True
        ):

            st.info(
                f"Mapa do {semestre} de {ano} "
                "em desenvolvimento."
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
        "📋 Processos em curso",
        use_container_width=True
    ):

        st.switch_page(
            "pages/2_Processos_Em_Curso.py"
        )


with col3:

    if st.button(
        "🔎 Consultar processo",
        use_container_width=True
    ):

        st.switch_page(
            "pages/4_Consultar_Processo.py"
        )