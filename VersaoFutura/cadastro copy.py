import streamlit as st
import pandas as pd
from datetime import datetime,date
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import psycopg2

min_date = date(1920, 1, 1)
max_date = date.today()

# Configuração da página para usar mais espaço
st.set_page_config(layout="wide")


# Função para conectar ao banco de dados
def connect_to_db():
    host = 'localhost'
    database = 'postgres'
    username = 'postgres'
    password = 'senha123'
    port = '5432'
    return psycopg2.connect(dbname=database, user=username, password=password, host=host, port=port)


# Interface de cadastro de usuários
def user_registration_form():
    st.title("Cadastro de Usuários")
    
    with st.form("user_form"):
        # Primeira linha com Nome, CPF/CNPJ, Data de Nascimento e Sexo
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nome")
        with col2:
            cpf_cnpj = st.text_input("CPF/CNPJ")

        col1, col2 = st.columns(2)
        with col1:
            birth_date = st.date_input("Data de Nascimento", min_value=min_date, max_value=max_date)
        with col2:
            sex = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])

        # Segunda linha com Endereço, CEP, Cidade e Bairro
        col1, col2 = st.columns(2)
        with col1:
            address = st.text_input("Endereço")
        with col2:
            zip_code = st.text_input("CEP")
        
        col1, col2 = st.columns(2)
        with col1:
            city = st.text_input("Cidade")
        with col2:
            district = st.text_input("Bairro")

        # Terceira linha com País, Telefone, Empresa e Email
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            country = st.text_input("País")
        with col2:
            phone = st.text_input("Telefone")
        with col3:
            company = st.text_input("Empresa")
        with col4:
            email = st.text_input("Email")

        # Quarta linha com Login e Senha, ajuste conforme necessário
        col1, col2 = st.columns(2)
        with col1:
            login = st.text_input("Login")
        with col2:
            password = st.text_input("Senha", type="password")

        submitted = st.form_submit_button("Salvar")
        if submitted:
            with connect_to_db() as conn:
                with conn.cursor() as cursor:
                        insert_query = """
                        INSERT INTO Users (Name, CPF_CNPJ, BirthDate, Sex, Address, ZipCode, City, District, Country, Phone, Company, Email, Login, Password) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(insert_query, (name, cpf_cnpj, birth_date, sex, address, zip_code, city, district, country, phone, company, email, login, password))
                        conn.commit()
            st.success("Usuário cadastrado com sucesso!")


# Função para obter todos os usuários
def get_all_users():
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Users")
            users = cursor.fetchall()
    return users


# Função para atualizar os dados do usuário
def update_user(user_id, updated_info):
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            update_query = """
            UPDATE public.users SET Name=%s, CPF_CNPJ=%s, BirthDate=%s, Sex=%s, Address=%s, 
            ZipCode=%s, City=%s, District=%s, Country=%s, Phone=%s, Company=%s, 
            Email=%s, Login=%s, Password=%s WHERE ID=%s
            """
            cursor.execute(update_query, (
                updated_info['Name'], updated_info['CPF_CNPJ'], updated_info['BirthDate'], updated_info['Sex'],
                updated_info['Address'], updated_info['ZipCode'], updated_info['City'], updated_info['District'],
                updated_info['Country'], updated_info['Phone'], updated_info['Company'], updated_info['Email'],
                updated_info['Login'], updated_info['Password'], user_id
            ))
            conn.commit()

# Função para deletar um usuário
def delete_user(user_id):
    try:
        with connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Users WHERE ID=%s", (user_id,))
                conn.commit()
                return True
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        return False

def view_and_edit_users():
    st.title("Visualizar e Editar Usuários")

    def fetch_data():
        data = pd.DataFrame(get_all_users(), columns=['ID', 'Name', 'CPF_CNPJ', 'BirthDate', 'Sex', 'Address', 'ZipCode', 'City', 'District', 'Country', 'Phone', 'Company', 'Email', 'Login', 'Password'])
        return data.sort_values(by='Name')

    df = fetch_data()

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(enabled=True)
    gb.configure_side_bar()
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
    gb.configure_grid_options(domLayout='normal')

    # Add row selection and actions for editing and deleting
    gb.configure_selection('single')
    gb.configure_selection_params(use_checkbox=True)
    gb.configure_grid_options(defaultColDef={'filter': True, 'resizable': True, 'sortable': True})

    grid_response = AgGrid(
        df,
        gridOptions=gb.build(),
        update_mode=GridUpdateMode.MODEL_CHANGED,
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=True  # Enable row actions
    )

    selected_rows = grid_response['selected_rows']

    if selected_rows:
        selected_row = selected_rows[0]  # Assuming single selection
        selected_user_id = selected_row['ID']

        col1, col2 = st.columns(2)

        with col1:
            if st.button('Editar Usuário'):
                edit_user_form(selected_user_id)

        with col2:
            if st.button('Deletar Usuário'):
                if delete_user(selected_user_id):
                    st.success(f'Usuário com ID {selected_user_id} deletado com sucesso!')
                    df = fetch_data()
                    grid_response = AgGrid(df, gridOptions=gb.build(), update_mode=GridUpdateMode.MODEL_CHANGED, fit_columns_on_grid_load=True)
                else:
                    st.error(f"Erro ao tentar deletar o usuário com ID {selected_user_id}")

# Chamando a função de visualização e edição de usuários
user_registration_form()
view_and_edit_users()

