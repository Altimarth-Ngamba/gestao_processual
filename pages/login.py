import streamlit as st


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Login",
    page_icon="🔐",
    layout="centered"
)


# ============================================================
# TÍTULO
# ============================================================

st.title("⚖️ :blue[Proc]Juris") 

st.subheader("Acesso ao sistema")

st.write(
    "Entre com as suas credenciais institucionais para continuar."
)

st.divider()


# ============================================================
# FORMULÁRIO DE LOGIN
# ============================================================

with st.form("formulario_login"):

    usuario = st.text_input(
        "Utilizador",
        placeholder="Digite o seu utilizador"
    )

    senha = st.text_input(
        "Palavra-passe",
        type="password",
        placeholder="Digite a sua palavra-passe"
    )

    entrar = st.form_submit_button(
        "🔐 Entrar",
        use_container_width=True,
        type="primary"
    )


# ============================================================
# PROCESSAMENTO
# ============================================================

if entrar:

    if not usuario or not senha:

        st.warning(
            "Por favor, preencha o utilizador e a palavra-passe."
        )

    else:

        # ----------------------------------------------------
        # TEMPORÁRIO
        # ----------------------------------------------------
        # Esta parte será substituída pela autenticação
        # através do banco de dados.
        #
        # Exemplo:
        #
        # resultado = autenticar_usuario(usuario, senha)
        #
        # ----------------------------------------------------

        if usuario == "admin" and senha == "1234":

            st.session_state["autenticado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["perfil"] = "administrador_geral"

            st.success("Login realizado com sucesso!")

            st.switch_page(
                "pages/dashboard.py"
            )

        else:

            st.error(
                "Utilizador ou palavra-passe incorretos."
            )


# ============================================================
# INFORMAÇÃO
# ============================================================

st.write("")

st.info(
    """
    🔒 **Acesso restrito**

    O acesso ao ProcJuris é destinado exclusivamente
    aos funcionários autorizados do Tribunal.
    """
)


# ============================================================
# VOLTAR
# ============================================================

st.write("")

if st.button(
    "← Voltar para a página inicial",
    use_container_width=True
):

    st.switch_page("app.py")