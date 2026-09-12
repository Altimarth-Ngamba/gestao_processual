import streamlit as st


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Meu Perfil",
    page_icon="👤",
    layout="wide"
)


# ============================================================
# VERIFICAR AUTENTICAÇÃO
# ============================================================

if not st.session_state.get("autenticado", False):

    st.warning(
        "É necessário iniciar sessão para acessar o seu perfil."
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

usuario = st.session_state.get(
    "usuario",
    "Utilizador"
)

perfil = st.session_state.get(
    "perfil",
    "Funcionário"
)

nome = st.session_state.get(
    "nome",
    usuario
)

email = st.session_state.get(
    "email",
    "Não informado"
)

telefone = st.session_state.get(
    "telefone",
    "Não informado"
)

cargo = st.session_state.get(
    "cargo",
    "Funcionário"
)

seccao = st.session_state.get(
    "seccao",
    "Não definida"
)

estado_conta = st.session_state.get(
    "estado_conta",
    "Ativa"
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("👤 Meu Perfil")

st.write(
    "Consulte as informações associadas à sua conta no ProcJuris."
)

st.divider()


# ============================================================
# IDENTIFICAÇÃO
# ============================================================

col1, col2 = st.columns([1, 2])


with col1:

    st.subheader("👤")

    st.write(f"### {nome}")

    st.caption(
        f"@{usuario}"
    )

    if estado_conta == "Ativa":

        st.success("● Conta ativa")

    else:

        st.warning(
            f"● {estado_conta}"
        )


with col2:

    st.subheader("Informações pessoais")

    col_a, col_b = st.columns(2)

    with col_a:

        st.write("**Nome completo**")
        st.write(nome)

        st.write("**E-mail**")
        st.write(email)

        st.write("**Telefone**")
        st.write(telefone)

    with col_b:

        st.write("**Utilizador**")
        st.write(usuario)

        st.write("**Cargo**")
        st.write(cargo)

        st.write("**Secção**")
        st.write(seccao)


# ============================================================
# ACESSO
# ============================================================

st.divider()

st.subheader("🔐 Acesso ao sistema")

col1, col2, col3 = st.columns(3)


with col1:

    st.write("**Perfil de acesso**")

    if perfil == "administrador_geral":

        st.info("Administrador Geral")

    elif perfil == "administrador_local":

        st.info("Administrador Local")

    else:

        st.info("Funcionário")


with col2:

    st.write("**Estado da conta**")

    st.success(estado_conta)


with col3:

    st.write("**Permissões**")

    if perfil == "administrador_geral":

        st.write("Acesso completo")

    elif perfil == "administrador_local":

        st.write("Gestão da unidade")

    else:

        st.write("Acesso operacional")


# ============================================================
# SEGURANÇA
# ============================================================

st.divider()

st.subheader("🛡️ Segurança")

st.write(
    """
    Por motivos de segurança, as credenciais de acesso não são
    apresentadas nesta página.
    """
)

if st.button(
    "🔑 Alterar palavra-passe",
    use_container_width=True
):

    st.info(
        "A funcionalidade de alteração da palavra-passe "
        "será disponibilizada em breve."
    )


# ============================================================
# NAVEGAÇÃO
# ============================================================

st.divider()

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "← Voltar ao painel",
        use_container_width=True
    ):

        st.switch_page(
            "pages/dashboard.py"
        )


with col2:

    if st.button(
        "🚪 Terminar sessão",
        use_container_width=True
    ):

        # Limpar informações da sessão
        st.session_state.clear()

        st.success(
            "Sessão terminada com sucesso."
        )

        st.switch_page(
            "pages/login.py"
        )