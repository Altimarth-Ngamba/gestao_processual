from backend.pesquisar_processos import pesquisar_processo
from backend.exibir_processo import exibir_processo
from backend.cadastrar_processos import adicionar_processo
import streamlit as st


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Gestão Processual",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# CABEÇALHO
# ============================================================

col1, col2 = st.columns([3, 1])

with col1:
    st.title("⚖️ :blue[Proc]Juris") 

with col2:
    st.write("")
    st.caption("Sistema de Gestão Processual")


st.divider()


# ============================================================
# APRESENTAÇÃO PRINCIPAL
# ============================================================

col1, col2 = st.columns([1.2, 1])

with col1:

    st.subheader("Gestão processual mais simples, segura e eficiente.")

    st.write(
        """
        O ProcJuris é uma plataforma institucional desenvolvida
        para apoiar os funcionários do Tribunal na organização,
        acompanhamento e gestão dos processos judiciais.
        """
    )

    st.write("")


with col2:

    st.image(
        "assets/imagens/hero.jpg",
        use_container_width=True
    )

if st.button(
    "🔐 Acessar o sistema",
    use_container_width=True,
    type="primary"
):
        st.switch_page("pages/login.py")

st.write("")
st.divider()
st.write("")


# ============================================================
# SOBRE O PROCJURIS
# ============================================================

st.header("O que é o :blue[Proc]Juris?")

st.image(
    "assets/imagens/sistema.jpg",
    use_container_width=True
)

st.write(
    """
    O ProcJuris é um sistema de gestão processual criado para
    centralizar informações e facilitar o trabalho diário dos
    funcionários do Tribunal.

    A plataforma permite organizar processos, consultar informações,
    acompanhar o andamento processual e futuramente gerar relatórios
    e estatísticas para apoiar a gestão.
    """
)


st.write("")
st.write("")


# ============================================================
# FUNCIONALIDADES
# ============================================================

st.header("O que podemos fazer?")

st.image(
    "assets/imagens/funcionario.jpg",
    use_container_width=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("📁 Processos")

    st.write(
        """
        Cadastre, consulte e acompanhe os processos
        de forma organizada.
        """
    )

    if st.button(
        "Conhecer gestão de processos",
        key="processos",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")


with col2:

    st.subheader("📊 Relatórios")

    st.write(
        """
        Consulte informações e indicadores que ajudam
        no acompanhamento da atividade processual.
        """
    )

    if st.button(
        "Conhecer relatórios",
        key="relatorios",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")


with col3:

    st.subheader("🔐 Segurança")

    st.write(
        """
        O acesso às funcionalidades é controlado de acordo
        com o perfil e as permissões de cada funcionário.
        """
    )

    if st.button(
        "Conhecer segurança",
        key="seguranca",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")


st.write("")
st.divider()
st.write("")


# ============================================================
# COMO FUNCIONA
# ============================================================

st.header("Como funciona?")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.subheader("1️⃣ Login")
    st.write(
        "O funcionário entra no sistema utilizando as suas credenciais."
    )


with col2:
    st.subheader("2️⃣ Perfil")
    st.write(
        "O sistema identifica o perfil e as permissões do funcionário."
    )


with col3:
    st.subheader("3️⃣ Acesso")
    st.write(
        "Cada utilizador visualiza apenas as funcionalidades autorizadas."
    )


with col4:
    st.subheader("4️⃣ Gestão")
    st.write(
        "Os processos podem ser consultados e geridos de forma organizada."
    )


st.write("")
st.divider()
st.write("")


# ============================================================
# BENEFÍCIOS
# ============================================================

st.header("Por que utilizar o ProcJuris?")

col1, col2 = st.columns(2)


with col1:

    st.subheader("📌 Organização")

    st.write(
        """
        Centralização das informações processuais em um
        único sistema.
        """
    )

    st.subheader("⚡ Eficiência")

    st.write(
        """
        Redução de tarefas manuais e maior rapidez na
        consulta das informações.
        """
    )


with col2:

    st.subheader("📈 Informação")

    st.write(
        """
        Informações estruturadas para facilitar o
        acompanhamento da atividade processual.
        """
    )

    st.subheader("🛡️ Controle")

    st.write(
        """
        Acesso controlado de acordo com o perfil e as
        responsabilidades de cada funcionário.
        """
    )


st.write("")
st.write("")


# ============================================================
# ACESSO RESTRITO
# ============================================================

st.info(
    """
    🔒 **Acesso restrito**

    O ProcJuris é uma plataforma de uso institucional.
    As funcionalidades do sistema estão disponíveis exclusivamente
    para funcionários do Tribunal devidamente autorizados.
    """
)


st.write("")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:

    if st.button(
        "🔐 Entrar no ProcJuris",
        use_container_width=True,
        type="primary"
    ):
        st.switch_page("pages/login.py")


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    "⚖️ ProcJuris — Sistema de Gestão Processual"
)

st.caption(
    "Plataforma institucional destinada aos funcionários autorizados do Tribunal."
)