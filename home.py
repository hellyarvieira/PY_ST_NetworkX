import streamlit as st
import random

# Dados fictícios de texto
textos_aleatorios = [
    "Networking é fundamental para expandir seus contatos e oportunidades de negócios.",
    "Construir relacionamentos sólidos pode abrir portas para parcerias valiosas.",
    "O networking ajuda a aprender com a experiência de outros empreendedores.",
    "Conectar-se com pessoas de diferentes setores pode trazer novas perspectivas e ideias.",
]


# Função para a página principal
def home_page():
    st.title('Bem-vindo à sua área restrita')
    st.header('Gestão Empresarial e a Importância do Networking')

    # Exibe um texto aleatório
    texto_aleatorio = random.choice(textos_aleatorios)
    st.write(texto_aleatorio)
