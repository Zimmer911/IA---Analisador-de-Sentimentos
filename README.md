# IA-Analisador-de-Sentimentos
Um projeto simples de **Inteligência Artificial** que analisa frases e classifica o sentimento como **positivo**, **negativo** ou **neutro**, utilizando **Python**, **Scikit-learn** e uma interface intuitiva feita com **Streamlit**.

## Tecnologias Utilizadas

- Python 3
- Pandas
- Scikit-learn
- Streamlit
- CountVectorizer
- Naive Bayes

- ## Como funciona

1. O usuário digita uma frase em português.
2. O texto é transformado em vetores numéricos.
3. Um modelo de **Naive Bayes** classifica a frase.
4. O resultado é exibido em tempo real: positivo, negativo ou neutro.

---

## Interface

A aplicação conta com uma interface limpa e responsiva feita com Streamlit.  

## Estrutura do Projeto
analisador_sentimentos/
├── app.py # Código principal com Streamlit
├── modelo_treinado.pkl # Modelo salvo (opcional)
├── sentimentos.csv # Base de dados com frases e rótulos
└── README.md # Este arquivo

## ▶ Como executar localmente
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/analisador-sentimentos.git
   cd analisador-sentimentos
   
Crie um ambiente virtual e ative:
python -m venv venv
venv\Scripts\activate 

Instale as dependências:
pip install -r requirements.txt

Rode o aplicativo:
streamlit run app.py

## Autor
Desenvolvido por Matheus Zimmer.
📫 Contato: matheuszimmer911@gmail.com
