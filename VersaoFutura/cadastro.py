import streamlit as st
import pandas as pd
import psycopg2
from datetime import date
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# Configuração da página para usar mais espaço
st.set_page_config(layout="wide")

# Funções de conexão ao banco de dados e outras funções como fornecido anteriormente...
def connect_to_db():
    host = 'localhost'
    database = 'postgres'
    username = 'postgres'
    password = 'senha123'
    port = '5432'
    return psycopg2.connect(dbname=database, user=username, password=password, host=host, port=port)

# Função para mostrar o formulário de edição do usuário
def edit_user_form(user_id):
    st.write("Formulário de edição não implementado")

# Função para visualizar e editar usuários
def view_and_edit_users():
    st.title("Visualizar e Editar Usuários")

def fetch_data():
    data = pd.DataFrame(get_all_users(), columns=['ID', 'Name', 'CPF_CNPJ', 'BirthDate', 'Sex', 'Address', 'ZipCode', 'City', 'District', 'Country', 'Phone', 'Company', 'Email', 'Login', 'Password'])
    return data.sort_values(by='Name')

# Função para obter todos os usuários
def get_all_users():
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Users")
            users = cursor.fetchall()
    return users

    # Layout dividido em duas colunas
    col1, col2 = st.columns([2, 1])

    with col1:
        df = fetch_data()

        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(enabled=True)
        gb.configure_side_bar()
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
        gb.configure_grid_options(domLayout='normal')
        gridOptions = gb.build()

        grid_response = AgGrid(
            df,
            gridOptions=gridOptions,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            fit_columns_on_grid_load=True
        )

    with col2:
        st.subheader("Adicionar Novo Usuário")
        with st.form("add_user_form", clear_on_submit=True):
            name = st.text_input("Nome", key="name")
            cpf_cnpj = st.text_input("CPF/CNPJ", key="cpf_cnpj")
            birth_date = st.date_input("Data de Nascimento", min_value=min_date, max_value=max_date, key="birth_date")
            sex = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"], key="sex")
            address = st.text_input("Endereço", key="address")
            zip_code = st.text_input("CEP", key="zip_code")
            city = st.text_input("Cidade", key="city")
            district = st.text_input("Bairro", key="district")
            country = st.text_input("País", key="country")
            phone = st.text_input("Telefone", key="phone")
            company = st.text_input("Empresa", key="company")
            email = st.text_input("Email", key="email")
            login = st.text_input("Login", key="login")
            password = st.text_input("Senha", type="password", key="password")
            submitted = st.form_submit_button("Adicionar")

            if submitted:
                # Aqui você deverá adicionar o usuário no banco de dados
                st.success("Usuário adicionado com sucesso!")

    # Botões de ação
    selected = st.session_state.get('selected_rows', None)
    if selected:
        user_id = selected[0]['ID']  # Assume que a seleção é única
        col3, col4 = st.columns([1, 1])
        with col3:
            if st.button('Editar'):
                edit_user_form(user_id)

        with col4:
            if st.button('Deletar'):
                delete_confirmation = st.checkbox(f"Confirmar exclusão do usuário {user_id}?")
                if delete_confirmation and st.button('Confirmar Deleção'):
                    delete_user(user_id)
                    st.experimental_rerun()

                

# Chamando a função de visualização e edição de usuários
view_and_edit_users()
