import streamlit as st


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Dashboard",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# PROTEÇÃO DA PÁGINA
# ============================================================

if not st.session_state.get("autenticado", False):

    st.warning(
        "É necessário iniciar sessão para acessar esta página."
    )

    if st.button(
        "🔐 Ir para o login",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")

    st.stop()


# ============================================================
# DADOS DO UTILIZADOR
# ============================================================

nome = st.session_state.get(
    "nome",
    st.session_state.get("usuario", "Utilizador")
)

perfil = st.session_state.get(
    "perfil",
    "funcionario"
)


# ============================================================
# CABEÇALHO
# ============================================================

col1, col2 = st.columns([3, 1])

with col1:

    st.title("⚖️ ProcJuris")

    st.write(
        f"Bem-vindo, **{nome}**."
    )


with col2:

    st.write("")

    if st.button(
        "👤 Meu Perfil",
        use_container_width=True
    ):

        st.switch_page(
            "pages/5_Perfil.py"
        )


st.divider()


# ============================================================
# APRESENTAÇÃO
# ============================================================

st.header("Painel de Gestão")

st.write(
    """
    A partir deste painel pode consultar, cadastrar e acompanhar
    os processos, além de acessar relatórios e estatísticas.
    """
)


# ============================================================
# INDICADORES
# ============================================================

st.subheader("Resumo")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Processos em curso",
        "—"
    )

with col2:

    st.metric(
        "Processos julgados",
        "—"
    )

with col3:

    st.metric(
        "Processos pendentes",
        "—"
    )

with col4:

    st.metric(
        "Total de processos",
        "—"
    )


st.divider()


# ============================================================
# GESTÃO DE PROCESSOS
# ============================================================

st.subheader("📁 Gestão de Processos")

col1, col2, col3 = st.columns(3)


with col1:

    st.write("### ➕ Adicionar")

    st.write(
        "Registe um novo processo no sistema."
    )

    if st.button(
        "Adicionar processo",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Adicionar_Processo.py"
        )


with col2:

    st.write("### 📋 Processos em curso")

    st.write(
        "Visualize os processos que estão atualmente em curso."
    )

    if st.button(
        "Ver processos",
        use_container_width=True
    ):

        st.switch_page(
            "pages/2_Processos_Em_Curso.py"
        )


with col3:

    st.write("### ✏️ Actualizar")

    st.write(
        "Pesquise e actualize informações de um processo."
    )

    if st.button(
        "Actualizar processo",
        use_container_width=True
    ):

        st.switch_page(
            "pages/3_Actualizar_Processo.py"
        )


# ============================================================
# CONSULTA
# ============================================================

st.write("")

st.subheader("🔎 Consulta")

col1, col2 = st.columns(2)


with col1:

    st.write("### 🔎 Consultar processo")

    st.write(
        "Encontre um processo através do número, autor ou réu."
    )

    if st.button(
        "Consultar processo",
        use_container_width=True
    ):

        st.switch_page(
            "pages/4_Consultar_Processo.py"
        )


with col2:

    st.write("### 📊 Relatórios e estatísticas")

    st.write(
        "Gere relatórios e consulte mapas estatísticos."
    )

    if st.button(
        "Relatórios e estatísticas",
        use_container_width=True
    ):

        st.switch_page(
            "pages/6_Relatorios_E_Estatisticas.py"
        )


# ============================================================
# ADMINISTRAÇÃO
# ============================================================

if perfil in [
    "administrador_local",
    "administrador_geral"
]:

    st.divider()

    st.subheader("⚙️ Administração")

    st.write(
        "Área disponível de acordo com o nível de acesso."
    )

    if st.button(
        "👥 Gestão de utilizadores",
        use_container_width=True
    ):

        st.info(
            "Módulo de gestão de utilizadores em desenvolvimento."
        )


# ============================================================
# PERFIL
# ============================================================

st.divider()

st.subheader("👤 Conta")

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "Meu perfil",
        use_container_width=True
    ):

        st.switch_page(
            "pages/5_Perfil.py"
        )


with col2:

    if st.button(
        "🚪 Terminar sessão",
        use_container_width=True
    ):

        st.session_state.clear()

        st.switch_page(
            "pages/login.py"
        )