import streamlit as st
from authentication import authenticate_user, login_page
from authentication import home_page

st.set_page_config(page_title="Meu Projeto")

# Variável global para armazenar o estado de autenticação
authenticated = False

# Página de login
if not authenticated:
    authenticated = authenticate_user()

# Se o login for bem-sucedido, obtenha o nome de usuário
if authenticated:
    username = st.session_state.get('username', None)

# Página principal após o login
if authenticated:
    st.sidebar.write("Menu de Navegação")
    pages = {
        "Página Inicial": home_page,
        # Outras páginas podem ser adicionadas aqui
    }

    selected_page = st.sidebar.selectbox("Selecione uma página:", list(pages.keys()))
    pages[selected_page](username)
