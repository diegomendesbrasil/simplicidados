# dashboard_content.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

fake = Faker()

# Geração de dados financeiros fictícios
def generate_financial_data(num_months=12, num_suppliers=10):
    # Gera datas dos últimos `num_months` meses
    months = pd.date_range(end=pd.to_datetime('now'), periods=num_months, freq='M').strftime('%b %Y')

    # Gera dados financeiros
    financial_data = pd.DataFrame({
        'Month': months,
        'Revenue': np.random.uniform(10000, 20000, size=num_months).round(2),
        'Expenses': np.random.uniform(5000, 15000, size=num_months).round(2)
    })

    # Calcula o faturamento como a diferença entre receita e despesa
    financial_data['Profit'] = financial_data['Revenue'] - financial_data['Expenses']

    # Gera dados para os top 10 fornecedores por despesa e receita
    top_suppliers_by_expense = pd.DataFrame({
        'Supplier': [fake.company() for _ in range(num_suppliers)],
        'Expense': np.random.uniform(2000, 8000, size=num_suppliers).round(2)
    }).nlargest(columns='Expense', n=10)

    top_suppliers_by_revenue = pd.DataFrame({
        'Supplier': [fake.company() for _ in range(num_suppliers)],
        'Revenue': np.random.uniform(2000, 8000, size=num_suppliers).round(2)
    }).nlargest(columns='Revenue', n=10)

    return financial_data, top_suppliers_by_expense, top_suppliers_by_revenue

def display_financial_charts(financial_data, top_suppliers_by_expense, top_suppliers_by_revenue):
    # Configurações do gráfico
    plt.figure(figsize=(10, 6))

    # Gráfico de linha para Receita e Despesas
    plt.plot(financial_data['Month'], financial_data['Revenue'], label='Revenue')
    plt.plot(financial_data['Month'], financial_data['Expenses'], label='Expenses')
    plt.plot(financial_data['Month'], financial_data['Profit'], label='Profit')
    plt.xticks(rotation=45)
    plt.title('Financial Overview')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

    # Reset plot
    plt.clf()

    # Gráfico de barras para Top 10 Despesas por Fornecedor
    fig, ax = plt.subplots()
    top_suppliers_by_expense.plot(kind='barh', x='Supplier', y='Expense', ax=ax, legend=None)
    ax.set_title('Top 10 Expenses by Supplier')
    st.pyplot(fig)

    # Reset plot
    plt.clf()

    # Gráfico de barras para Top 10 Receitas por Fornecedor
    fig, ax = plt.subplots()
    top_suppliers_by_revenue.plot(kind='barh', x='Supplier', y='Revenue', ax=ax, legend=None)
    ax.set_title('Top 10 Revenue by Supplier')
    st.pyplot(fig)

# Função principal para exibir o dashboard
def display_dashboard():
    st.title('Company Financial Dashboard')

    # Gerar dados
    financial_data, top_suppliers_by_expense, top_suppliers_by_revenue = generate_financial_data()

    # Display the financial charts
    display_financial_charts(financial_data, top_suppliers_by_expense, top_suppliers_by_revenue)

# Exibir o dashboard
if __name__ == "__main__":
    display_dashboard()
