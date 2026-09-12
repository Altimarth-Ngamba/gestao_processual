from backend.cadastrar_processos import adicionar_processo
import streamlit as st

from backend.cadastrar_processos import adicionar_processo


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Adicionar Processo",
    page_icon="📁",
    layout="wide"
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("📁 Adicionar Processo")

st.write(
    "Registe um novo processo no sistema de gestão processual."
)

st.divider()


# ============================================================
# INFORMAÇÕES DO PROCESSO
# ============================================================

st.subheader("📋 Identificação do Processo")

with st.form("form_adicionar_processo"):

    col1, col2 = st.columns(2)

    # --------------------------------------------------------
    # COLUNA 1
    # --------------------------------------------------------

    with col1:

        numero = st.text_input(
            "Número do Processo *",
            placeholder="Ex.: 01/2026"
        )

        letra = st.text_input(
            "Letra",
            placeholder="Ex.: A"
        )

        accao = st.selectbox(
            "Tipo de Ação *",
            [
                "Selecione uma ação",
                "Declarativa",
                "Executiva",
                "Conflito Laboral",
                "Família",
                "Comercial",
                "Administrativa",
                "Outra"
            ]
        )

        autor = st.text_input(
            "Autor *",
            placeholder="Nome completo do autor"
        )

        reu = st.text_input(
            "Réu *",
            placeholder="Nome completo do réu"
        )

    # --------------------------------------------------------
    # COLUNA 2
    # --------------------------------------------------------

    with col2:

        escrivao = st.text_input(
            "Escrivão *",
            placeholder="Nome do escrivão"
        )

        juiz = st.text_input(
            "Juiz *",
            placeholder="Nome do juiz"
        )

        seccao = st.text_input(
            "Secção *",
            placeholder="Ex.: 1ª Secção"
        )

        data_entrada = st.date_input(
            "Data de Entrada *"
        )

        st.selectbox(
            "Estado Inicial",
            ["Em curso"],
            disabled=True
        )

    st.divider()

    # ========================================================
    # CONFIRMAÇÃO
    # ========================================================

    st.subheader("🔎 Confirmação")

    st.caption(
        "Confirme os dados antes de adicionar o processo."
    )

    adicionar = st.form_submit_button(
        "➕ Adicionar Processo",
        use_container_width=True,
        type="primary"
    )


# ============================================================
# PROCESSAMENTO
# ============================================================

if adicionar:

    # --------------------------------------------------------
    # VALIDAÇÃO
    # --------------------------------------------------------

    erros = []

    if not numero.strip():
        erros.append("Informe o número do processo.")

    if accao == "Selecione uma ação":
        erros.append("Selecione o tipo de ação.")

    if not autor.strip():
        erros.append("Informe o autor.")

    if not reu.strip():
        erros.append("Informe o réu.")

    if not escrivao.strip():
        erros.append("Informe o escrivão.")

    if not juiz.strip():
        erros.append("Informe o juiz.")

    if not seccao.strip():
        erros.append("Informe a secção.")

    # --------------------------------------------------------
    # MOSTRAR ERROS
    # --------------------------------------------------------

    if erros:

        for erro in erros:
            st.error(erro)

    # --------------------------------------------------------
    # ADICIONAR PROCESSO
    # --------------------------------------------------------

    else:

        estado = "Em curso"

        try:

            adicionar_processo(
                numero,
                letra,
                accao,
                autor,
                reu,
                escrivao,
                juiz,
                seccao,
                estado,
                data_entrada
            )

            st.success(
                f"Processo {numero} adicionado com sucesso!"
            )

            st.info(
                "O processo foi registado com o estado inicial "
                "'Em curso'."
            )

        except Exception as erro:

            st.error(
                f"Não foi possível adicionar o processo: {erro}"
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
        "🔎 Consultar processos",
        use_container_width=True
    ):
        st.switch_page("pages/4_Consultar_Processo.py")


with col3:

    if st.button(
        "📊 Relatórios",
        use_container_width=True
    ):
        st.info("Módulo de relatórios em desenvolvimento.")