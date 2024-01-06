import streamlit as st
from user_auth import login_page, register_user
from home import home_page

st.set_page_config(page_title="Meu Aplicativo")

# Variável global para armazenar o estado de autenticação
authenticated = False

# Página de registro de novos usuários
if not authenticated:
    new_user = st.checkbox("Registrar Novo Usuário")
    if new_user:
        registered = register_user()
        if registered:
            st.success('Cadastro realizado com sucesso! Faça login agora.')
        else:
            st.warning('O registro falhou. Tente novamente com um nome de usuário único.')

# Página de login
if not authenticated:
    authenticated = login_page()

# Página principal após o login
if authenticated:
    home_page()
