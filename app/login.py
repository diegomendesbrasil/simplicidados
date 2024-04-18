import streamlit as st
import bcrypt
import psycopg2

# Função para conectar ao banco de dados
def conectar_bd():
    conexao = psycopg2.connect(
        host='localhost',
        database='NomeDoBanco',
        user='usuario',
        password='senha'
    )
    return conexao

# Verificar credenciais no banco de dados
def verificar_credenciais(nome_usuario, senha):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT senha FROM dmb.user WHERE nome_usuario = %s", (nome_usuario,))
    senha_hash = cursor.fetchone()
    cursor.close()
    conexao.close()
    if senha_hash:
        return bcrypt.checkpw(senha.encode('utf-8'), senha_hash[0].encode('utf-8'))
    return False

def login():
    st.title('Pulsar.Dados - Login')

    nome_usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type='password')

    if st.button('Login'):
        if verificar_credenciais(nome_usuario, senha):
            st.success('Login bem-sucedido!')
            st.session_state['is_logged_in'] = True
            st.session_state['username'] = nome_usuario
            st.session_state['page'] = 'dashboard'

            st.experimental_rerun()
        else:
            st.error('Nome de usuário ou senha incorretos!')

# Verifique se o módulo não foi importado e execute o login
if __name__ == "__main__":
    login()
