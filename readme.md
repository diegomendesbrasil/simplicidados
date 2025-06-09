# 📌 Estratégia do Projeto

## 🏗️ Estrutura

O projeto está organizado em dois diretórios principais:

* `backend` &ndash; API desenvolvida em **FastAPI** e integrada ao **PostgreSQL** via SQLAlchemy.
* `frontend` &ndash; Interface feita com **Streamlit** que consome a API para gerenciar contas a pagar e a receber.

As principais entidades do sistema são:
* Usuário
* Despesas
* Receitas
* Cliente
* Fornecedor

## 🔐 Criação da Tela de Login

A tela de login será desenvolvida seguindo a estrutura definida na conversa do WhatsApp. Após o login, o usuário será redirecionado para um **dashboard** personalizado.

### 🖥️ Etapas
1. **Criação da Tela de Login**
2. **Implementação do Dashboard Pós-Login**
   - Seguir o layout definido na conversa do WhatsApp

### 🚀 Execução

1. Inicie a API:
   ```bash
   uvicorn backend.main:app --reload
   ```
2. Em outro terminal, rode a interface:
   ```bash
   streamlit run frontend/app.py
   ```

---   
       
               
