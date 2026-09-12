import streamlit as st

from backend.pesquisar_processos import pesquisar_processo


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="ProcJuris | Atualizar Processo",
    page_icon="✏️",
    layout="wide"
)


# ============================================================
# LISTAS DE OPÇÕES
# ============================================================

ESTADOS = [
    "Em curso",
    "Julgado",
    "Arquivado",
    "Suspenso",
    "Extinto"
]

LOCALIZACOES = [
    "Sala do Juiz",
    "MºPº",
    "Aguardar prazo",
    "Aguardar Guia",
    "Por notificar",
    "Na conta",
    "Por conclusar",
    "Aguardar ofício",
    "Aguardar carta precatória",
    "Aguardar excedentes",
    "Arquivo",
    "Audiência",
    "Cartório",
    "Secretaria",
    "Outro"
]


# ============================================================
# CABEÇALHO
# ============================================================

st.title("✏️ Atualizar Processo")

st.write(
    "Pesquise um processo e atualize o seu estado ou localização."
)

st.divider()


# ============================================================
# PESQUISA
# ============================================================

st.subheader("🔎 Pesquisar Processo")


criterio = st.selectbox(
    "Pesquisar por",
    [
        "Número do processo",
        "Autor",
        "Réu"
    ]
)


if criterio == "Número do processo":

    criterio_backend = "numero"

    placeholder = "Ex.: 01/2026"

elif criterio == "Autor":

    criterio_backend = "autor"

    placeholder = "Ex.: João Manuel"

else:

    criterio_backend = "reu"

    placeholder = "Ex.: António José"


valor = st.text_input(
    "Digite a informação",
    placeholder=placeholder
)


if st.button(
    "🔎 Pesquisar",
    use_container_width=True,
    type="primary"
):

    if not valor.strip():

        st.warning(
            "Digite uma informação para pesquisar."
        )

    else:

        resultados = pesquisar_processo(
            valor,
            criterio_backend
        )

        st.session_state[
            "resultados_atualizacao"
        ] = resultados

        st.session_state.pop(
            "processo_atualizar",
            None
        )


# ============================================================
# RESULTADOS
# ============================================================

if "resultados_atualizacao" in st.session_state:

    resultados = st.session_state[
        "resultados_atualizacao"
    ]

    st.divider()

    if not resultados:

        st.warning(
            "Nenhum processo encontrado."
        )

    else:

        st.subheader(
            f"📋 {len(resultados)} processo(s) encontrado(s)"
        )

        for indice, processo in enumerate(resultados):

            numero = processo.get(
                "numero",
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

            estado = processo.get(
                "estado",
                "-"
            )

            localizacao = processo.get(
                "localizacao",
                "Não definida"
            )

            col1, col2, col3, col4, col5, col6 = st.columns(
                [1.2, 2, 2, 1.3, 1.8, 1]
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
                st.write(localizacao)

            with col6:

                if st.button(
                    "Selecionar",
                    key=f"selecionar_{indice}",
                    use_container_width=True
                ):

                    st.session_state[
                        "processo_atualizar"
                    ] = processo

            st.divider()


# ============================================================
# PROCESSO SELECIONADO
# ============================================================

if "processo_atualizar" in st.session_state:

    processo = st.session_state[
        "processo_atualizar"
    ]

    st.divider()

    st.subheader("📄 Processo selecionado")


    # ========================================================
    # INFORMAÇÕES DO PROCESSO
    # ========================================================

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
            "**Estado atual:**",
            processo.get("estado", "-")
        )

        st.write(
            "**Localização atual:**",
            processo.get(
                "localizacao",
                "Não definida"
            )
        )


    st.divider()


    # ========================================================
    # ATUALIZAÇÃO
    # ========================================================

    st.subheader("✏️ Atualizar informações")


    estado_atual = processo.get(
        "estado",
        "Em curso"
    )

    localizacao_atual = processo.get(
        "localizacao",
        "Cartório"
    )


    # Garantir que o valor atual exista nas opções
    if estado_atual not in ESTADOS:

        ESTADOS_EXIBIR = [
            estado_atual
        ] + ESTADOS

    else:

        ESTADOS_EXIBIR = ESTADOS


    if localizacao_atual not in LOCALIZACOES:

        LOCALIZACOES_EXIBIR = [
            localizacao_atual
        ] + LOCALIZACOES

    else:

        LOCALIZACOES_EXIBIR = LOCALIZACOES


    with st.form("form_atualizar_processo"):

        novo_estado = st.selectbox(
            "Estado",
            ESTADOS_EXIBIR,
            index=ESTADOS_EXIBIR.index(
                estado_atual
            )
        )

        nova_localizacao = st.selectbox(
            "Localização",
            LOCALIZACOES_EXIBIR,
            index=LOCALIZACOES_EXIBIR.index(
                localizacao_atual
            )
        )


        st.write("")

        atualizar = st.form_submit_button(
            "💾 Guardar alterações",
            use_container_width=True,
            type="primary"
        )


    # ========================================================
    # GUARDAR ALTERAÇÕES
    # ========================================================

    if atualizar:

        processo["estado"] = novo_estado

        processo["localizacao"] = nova_localizacao

        st.success(
            f"Processo {processo.get('numero', '')} "
            "atualizado com sucesso."
        )

        st.info(
            f"Estado: {novo_estado}  |  "
            f"Localização: {nova_localizacao}"
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