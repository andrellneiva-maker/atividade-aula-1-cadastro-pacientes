# Atividade Aula 1 - Cadastro de Pacientes

O projeto possui duas versões da mesma aplicação: uma feita com Gradio e outra com Streamlit. As duas usam os campos solicitados no enunciado e permitem salvar os dados em CSV. A versão Streamlit mantém os registros da sessão e disponibiliza o download do arquivo CSV, pois o armazenamento do Streamlit Community Cloud é temporário.

## Como executar

1. Crie e ative um ambiente virtual Python.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Para executar a versão Gradio, use `python gradio_app/app.py`.
4. Para executar a versão Streamlit, use `streamlit run streamlit_app/app.py`.

## Publicação no Streamlit Community Cloud

Para publicar, envie esta pasta a um repositório público no GitHub. No Streamlit Community Cloud, crie um novo aplicativo apontando para `streamlit_app/app.py`. Após o build, teste o formulário no computador e no celular e registre o link público gerado.

## Arquivo de exemplo

O arquivo `pacientes_exemplo.csv` contém registros fictícios criados apenas para teste da interface.
