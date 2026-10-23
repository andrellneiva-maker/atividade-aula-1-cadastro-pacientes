"""Cadastro de pacientes - versão Gradio."""
from datetime import datetime
from pathlib import Path

import gradio as gr
import pandas as pd


ARQUIVO_CSV = Path(__file__).with_name("pacientes.csv")
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]


def ultimos_pacientes() -> pd.DataFrame:
    if not ARQUIVO_CSV.exists():
        return pd.DataFrame(columns=COLUNAS)
    return pd.read_csv(ARQUIVO_CSV).tail(5)


def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):
    nome = (nome or "").strip()
    motivo = (motivo or "").strip()
    if not nome or idade is None or not motivo:
        return "Preencha nome, idade e motivo da consulta.", ultimos_pacientes()
    if not 0 <= idade <= 120:
        return "Informe uma idade entre 0 e 120 anos.", ultimos_pacientes()

    linha = pd.DataFrame([{
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome,
        "idade": int(idade),
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": motivo,
    }])
    linha.to_csv(ARQUIVO_CSV, mode="a", header=not ARQUIVO_CSV.exists(), index=False)
    return "Paciente cadastrado com sucesso.", ultimos_pacientes()


with gr.Blocks(title="Cadastro de Pacientes") as demo:
    gr.Markdown("# Cadastro de Pacientes\nPreencha os dados para registrar o atendimento.")
    nome = gr.Textbox(label="Nome do paciente", placeholder="Ex.: Ana Silva")
    idade = gr.Number(label="Idade", precision=0, minimum=0, maximum=120)
    convenio = gr.Dropdown(
        ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"],
        label="Convênio", value="Particular",
    )
    prioridade = gr.Slider(1, 5, value=3, step=1, label="Prioridade do atendimento (5 = urgente)")
    motivo = gr.Textbox(label="Motivo da consulta / observações", lines=3)
    botao = gr.Button("Cadastrar", variant="primary")
    saida_msg = gr.Textbox(label="Status", interactive=False)
    tabela = gr.Dataframe(value=ultimos_pacientes, label="Últimos pacientes cadastrados", interactive=False)
    botao.click(cadastrar_paciente, [nome, idade, convenio, prioridade, motivo], [saida_msg, tabela])


if __name__ == "__main__":
    demo.launch()
