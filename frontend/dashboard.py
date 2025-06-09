from streamlit_option_menu import option_menu
import streamlit as st
from frontend.user_info import render_user_info  # Informações do usuário
from frontend.dashboard_content import display_dashboard  # Conteúdo do dashboard
from frontend.expenses import contas_pagar
from frontend.revenues import contas_receber

 
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
        display_dashboard()
    elif selected == "Contas a Pagar":
        contas_pagar()
    elif selected == "Contas a Receber":
        contas_receber()
    elif selected == "Cadastro de Clientes":
        st.write("Página de Cadastro de Clientes")  # Substituir pela função correspondente
    elif selected == "Cadastro de Fornecedores":
        st.write("Página de Cadastro de Fornecedores")  # Substituir pela função correspondente
    elif selected == "Cadastro de Usuário":
        st.write("Cadastro de Usuário")
    # Adicione condições para outras páginas conforme necessário
    # ...
