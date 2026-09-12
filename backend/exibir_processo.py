import streamlit as st


def exibir_processo(processo):

    st.subheader("📄 Dados do Processo")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Número:**", processo.get("numero", "-"))

        st.write("**Letra:**", processo.get("letra", "-"))

        st.write("**Ação:**", processo.get("accao", "-"))

        st.write("**Autor:**", processo.get("autor", "-"))

        st.write("**Réu:**", processo.get("reu", "-"))

    with col2:

        st.write("**Escrivão:**", processo.get("escrivao", "-"))

        st.write("**Juiz:**", processo.get("juiz", "-"))

        st.write("**Secção:**", processo.get("seccao", "-"))

        st.write("**Estado:**", processo.get("estado", "-"))

        st.write(
            "**Data de entrada:**",
            processo.get("data_entrada", "-")
        )