

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x,y)

# Interface
st.title("🍕 Prevendo o preço da pizza")
st.divider()


# Entrada do usuário
diametro = st.number_input("Digite o diâmetro da pizza (cm):", min_value=1, max_value=600, value=30)

# Fazer previsão
previsao = modelo.predict([[diametro]])[0][0]

st.subheader("🔮 Previsão")
st.write(f"O preço estimado para uma pizza de **{diametro} cm** é **R$ {previsao:.2f}**")