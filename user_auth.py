import streamlit as st
import pandas as pd
import re


# Função para autenticar o usuário
def login_page():
    st.title('Login')
    username = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')

    if st.button('Entrar'):
        user_data = pd.read_csv("user_data.csv")
        if (user_data['Username'] == username).any() and (user_data['Password'] == password).any():
            st.success('Login bem-sucedido!')
            return True
        else:
            st.error('Credenciais inválidas. Tente novamente.')
    return False


# Função para validar um endereço de e-mail
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


# Função para validar um número de telefone no formato DDD + Telefone
def is_valid_phone(phone):
    # Expressão regular para validar DDD + Telefone com ou sem espaço no DDD
    pattern = r'^(\d{2,3})?\s?(\d{8,9})$'
    return bool(re.match(pattern, phone))


# Função para registrar um novo usuário com informações adicionais
def register_user():
    st.title('Registro de Novo Usuário')
    new_username = st.text_input('Novo Usuário')
    new_password = st.text_input('Nova Senha', type='password')
    new_email = st.text_input('E-mail')
    new_phone = st.text_input('Telefone (DDD + Telefone)')

    if st.button('Registrar'):
        user_data = pd.read_csv("user_data.csv")
        if (user_data['Username'] == new_username).any():
            st.warning('Nome de usuário já existe. Escolha outro.')
        elif not is_valid_email(new_email):
            st.warning('E-mail inválido. Insira um e-mail válido.')
        elif not is_valid_phone(new_phone):
            st.warning(
                'Telefone inválido. Insira um telefone válido no formato DDD + Telefone (com ou sem espaços no DDD).')
        else:
            new_user_data = pd.DataFrame({
                'Username': [new_username],
                'Password': [new_password],
                'Email': [new_email],
                'Telefone': [new_phone]
            })
            user_data = pd.concat([user_data, new_user_data], ignore_index=True)
            user_data.to_csv("user_data.csv", index=False)
            return True
    return False
