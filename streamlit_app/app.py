"""Cadastro de pacientes - versão Streamlit."""
from datetime import datetime

import pandas as pd
import streamlit as st


COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]
st.set_page_config(page_title="Cadastro de Pacientes", layout="centered")
st.title("Cadastro de Pacientes")
st.caption("Registro rápido de atendimentos da recepção.")

if "pacientes" not in st.session_state:
    st.session_state.pacientes = pd.DataFrame(columns=COLUNAS)

with st.form("cadastro", clear_on_submit=True):
    nome = st.text_input("Nome do paciente", placeholder="Ex.: Ana Silva")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    convenio = st.selectbox("Convênio", ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"])
    prioridade = st.slider("Prioridade do atendimento (5 = urgente)", 1, 5, 3)
    motivo = st.text_area("Motivo da consulta / observações")
    enviado = st.form_submit_button("Cadastrar")

if enviado:
    if not nome.strip() or not motivo.strip():
        st.error("Preencha nome e motivo da consulta.")
    else:
        nova_linha = pd.DataFrame([{
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome": nome.strip(), "idade": idade, "convenio": convenio,
            "prioridade": prioridade, "motivo": motivo.strip(),
        }])
        st.session_state.pacientes = pd.concat([st.session_state.pacientes, nova_linha], ignore_index=True)
        st.success("Paciente cadastrado com sucesso.")

st.subheader("Últimos pacientes cadastrados")
st.dataframe(st.session_state.pacientes.tail(5), use_container_width=True, hide_index=True)
csv = st.session_state.pacientes.to_csv(index=False).encode("utf-8")
st.download_button("Baixar CSV da sessão", csv, "pacientes.csv", "text/csv")
