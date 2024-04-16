import streamlit as st

def contaspagar():
    st.title('Página de Contas a Pagar')
    # Adicione o conteúdo desta página aqui

    # Adicionar o botão de Voltar
    if st.button('Voltar ao Dashboard'):
        st.session_state['page'] = 'dashboard'
        st.experimental_rerun()