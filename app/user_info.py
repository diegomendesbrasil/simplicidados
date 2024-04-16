import streamlit as st

def render_user_info():
    if st.session_state.get('is_logged_in', False):
        # Layout para nome de usuário e logout
        st.sidebar.markdown("---")  # Linha divisória
        st.sidebar.write(f"👤 **{st.session_state.get('username', 'Usuário')}**")

        if st.sidebar.button('Logout'):
            # Remover o status de logado e limpar o nome do usuário
            st.session_state.is_logged_in = False
            st.session_state.username = ''
            st.session_state.page = 'login'  # Redirecionar para a página de login
            st.experimental_rerun()
