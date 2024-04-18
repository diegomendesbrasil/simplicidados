from streamlit_option_menu import option_menu
import streamlit as st
from user_info import render_user_info  # Importação da função de informações do usuário
from dashboard_content import display_dashboard  # Importação da função de conteúdo do dashboard
from cadastro import user_registration_form  # Importação da função de conteúdo do dashboard
 
def dashboard():
    with st.sidebar:
        st.sidebar.title('Menu Principal')

        # Criar um menu de navegação vertical na sidebar
        selected = option_menu(None, 
                               ["Dashboard", "Contas a Pagar", "Contas a Receber", "Cadastro de Clientes", "Cadastro de Fornecedores","Cadastro de Usuário"], 
                               icons=['house', 'file-earmark-bar-graph', "receipt", 'person', 'shop','person'], 
                               menu_icon="cast", default_index=0)

    # Chamar a função de renderização das informações do usuário
    render_user_info()

    # Definir a página com base na seleção
    if selected == "Dashboard":
        display_dashboard()  # Carrega o conteúdo do Dashboard
    elif selected == "Contas a Pagar":
        st.write("Página de Contas a Pagar")  # Substituir pela função correspondente
    elif selected == "Contas a Receber":
        st.write("Página de Contas a Receber")  # Substituir pela função correspondente
    elif selected == "Cadastro de Clientes":
        st.write("Página de Cadastro de Clientes")  # Substituir pela função correspondente
    elif selected == "Cadastro de Fornecedores":
        st.write("Página de Cadastro de Fornecedores")  # Substituir pela função correspondente
    elif selected == "Cadastro de Usuário":
        user_registration_form() # Substituir pela função correspondente
    # Adicione condições para outras páginas conforme necessário
    # ...
