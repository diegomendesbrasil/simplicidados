import streamlit as st
import requests
from datetime import date

API_URL = "http://localhost:8000"

def contas_pagar():
    st.header("Contas a Pagar")
    descricao = st.text_input("Descrição")
    vencimento = st.date_input("Vencimento", value=date.today())
    valor = st.number_input("Valor", min_value=0.0, step=0.01, format="%0.2f")
    if st.button("Salvar"):
        data = {
            "description": descricao,
            "due_date": vencimento.isoformat(),
            "amount": valor,
        }
        resp = requests.post(f"{API_URL}/expenses/", json=data)
        if resp.status_code == 200:
            st.success("Despesa registrada")
        else:
            st.error("Erro ao registrar despesa")

    st.subheader("Lançamentos")
    resp = requests.get(f"{API_URL}/expenses/")
    if resp.status_code == 200:
        items = resp.json()
        if items:
            st.table(items)
        else:
            st.info("Nenhuma despesa cadastrada")
    else:
        st.error("Erro ao carregar despesas")
