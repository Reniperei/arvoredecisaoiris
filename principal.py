import streamlit as st

st.title('Repositorio IA')
nome = text_input('Digite o seu nome:')
if st.button('clique aqui'):
  st.write('bem vindo',nome,'ao seu primeiro aplicativo')
