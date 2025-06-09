import streamlit as st
import requests
from datetime import date

API_URL = "http://localhost:8000"

def contas_receber():
    st.header("Contas a Receber")
    descricao = st.text_input("Descrição")
    vencimento = st.date_input("Vencimento", value=date.today())
    valor = st.number_input("Valor", min_value=0.0, step=0.01, format="%0.2f")
    if st.button("Salvar"):
        data = {
            "description": descricao,
            "due_date": vencimento.isoformat(),
            "amount": valor,
        }
        resp = requests.post(f"{API_URL}/revenues/", json=data)
        if resp.status_code == 200:
            st.success("Receita registrada")
        else:
            st.error("Erro ao registrar receita")

    st.subheader("Lançamentos")
    resp = requests.get(f"{API_URL}/revenues/")
    if resp.status_code == 200:
        items = resp.json()
        if items:
            st.table(items)
        else:
            st.info("Nenhuma receita cadastrada")
    else:
        st.error("Erro ao carregar receitas")
