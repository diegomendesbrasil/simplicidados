import streamlit as st
import login
import dashboard
# Importe os outros módulos de página conforme necessário

# Inicializar variáveis de estado de sessão
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ''

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'  # Define a página de login como inicial

# Função principal para controlar o fluxo do aplicativo
def main():
    if st.session_state.get('is_logged_in', False):
        # O usuário está logado; renderizar a página solicitada
        if st.session_state.page == 'dashboard':
            dashboard.dashboard()
        # Adicionar condições semelhantes para outras páginas
        # ...
    else:
        # O usuário não está logado; renderizar a página de login
        login.login()

if __name__ == '__main__':
    main()
