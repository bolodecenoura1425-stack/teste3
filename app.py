<<<<<<< HEAD


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar dados
df = pd.read_csv("pizzas.csv")
sabores = pd.read_csv("sabores.csv")

# Treinar modelo (só diâmetro x preço_base)
X = df[["diametro"]]
y = df["preco"]
modelo = LinearRegression()
modelo.fit(X, y)

# Interface
st.title("🍕 Calculando o preço da pizza")
st.divider()

diametro = st.number_input("Digite o diâmetro da pizza (cm):", min_value=1, max_value=600, value=30)
sabor = st.selectbox("Escolha o sabor:", sabores["sabor"].tolist())

# Previsão
preco_base = modelo.predict([[diametro]])[0]
adicional = sabores.loc[sabores["sabor"] == sabor, "adicional"].values[0]
preco_final = preco_base + adicional

st.subheader("💰 Previsão de preço")
st.write(f"O preço estimado para uma pizza de **{diametro} cm** sabor **{sabor}** é **R$ {preco_final:.2f}**")
=======


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar dados
df = pd.read_csv("pizzas.csv")
sabores = pd.read_csv("sabores.csv")

# Treinar modelo (só diâmetro x preço_base)
X = df[["diametro"]]
y = df["preco"]
modelo = LinearRegression()
modelo.fit(X, y)

# Interface
st.title("🍕 Calculando o preço da pizza")
st.divider()

diametro = st.number_input("Digite o diâmetro da pizza (cm):", min_value=1, max_value=600, value=30)
sabor = st.selectbox("Escolha o sabor:", sabores["sabor"].tolist())

# Previsão
preco_base = modelo.predict([[diametro]])[0]
adicional = sabores.loc[sabores["sabor"] == sabor, "adicional"].values[0]
preco_final = preco_base + adicional

st.subheader("💰 Previsão de preço")
st.write(f"O preço estimado para uma pizza de **{diametro} cm** sabor **{sabor}** é **R$ {preco_final:.2f}**")
>>>>>>> 3409685232bd46da1851958f4d120e156b4dadb6
