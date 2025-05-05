import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# 1. Carregar o arquivo CSV com frases e rótulos
df = pd.read_csv("sentimentos.csv")
df.columns = df.columns.str.lower().str.strip()  # padroniza os nomes das colunas

# 2. Separar dados e rótulos
texts = df["frase"]
labels = df["sentimento"]

# 3. Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42
)

# 4. Criar o pipeline de vetorização + modelo
model = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB())
])

# 5. Treinar o modelo
model.fit(X_train, y_train)

# 6. Avaliar o modelo
y_pred = model.predict(X_test)
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# 7. Salvar o modelo treinado
joblib.dump(model, "modelo_sentimentos.pkl")

# 8. Interação com o usuário no terminal
print("\nDigite frases para analisar o sentimento. Digite 'sair' para encerrar.\n")
while True:
    frase = input("Frase: ").strip()
    if not frase:
        print("Digite algo válido.")
        continue
    if frase.lower() == 'sair':
        break
    pred = model.predict([frase])[0]
    print("Sentimento:", pred)
