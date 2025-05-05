import streamlit as st
import joblib

# Carrega o modelo treinado
modelo = joblib.load("modelo_sentimentos.pkl")

# Interface
st.set_page_config(page_title="Analisador de Sentimentos", layout="centered")
st.title("🧠 Analisador de Sentimentos")
st.markdown("Digite uma frase e veja se ela é positiva, negativa ou neutra!")

# Entrada do usuário
frase = st.text_input("Frase para análise:")

if frase:
    sentimento = modelo.predict([frase])[0]
    if sentimento == "positivo":
        st.success(f"Sentimento: **{sentimento.capitalize()}** 😊")
    elif sentimento == "negativo":
        st.error(f"Sentimento: **{sentimento.capitalize()}** 😠")
    else:
        st.info(f"Sentimento: **{sentimento.capitalize()}** 😐")
