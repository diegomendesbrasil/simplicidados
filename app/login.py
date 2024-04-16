import streamlit as st

# Simular a verificação das credenciais
def verificar_credenciais(nome_usuario, senha):
    return nome_usuario == "admin" and senha == "senha123"

def login():
    st.title('Pulsar.Dados - Login')

    nome_usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type='password')

    if st.button('Login'):
        if verificar_credenciais(nome_usuario, senha):
            st.success('Login bem-sucedido!')
            st.session_state['is_logged_in'] = True
            st.session_state['username'] = nome_usuario  # Definir o nome do usuário
            st.session_state['page'] = 'dashboard'  # Redirecionar para o dashboard

            st.experimental_rerun()
        else:
            st.error('Nome de usuário ou senha incorretos!')
