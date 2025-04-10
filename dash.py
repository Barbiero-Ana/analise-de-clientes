import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')

# Título da aplicação
st.title("📊 Análise de Comportamento do Consumidor em E-commerce")

# Menu lateral para seleção da análise
op = st.sidebar.selectbox("Selecione uma análise:", [
    "Faixa etária mais comum",
    "Gênero mais comum",
    "Renda mais comum",
    "Profissão mais comum",
    "Idade média por nível de renda",
    "Idade média por gênero",
    "Proporção por nível de renda",
    "Valor médio por compra",
    "Compras online vs loja física",
    "Valor médio por gênero",
    "Valor médio por estado civil"
])

# Condições de análise
if op == "Faixa etária mais comum":
    idade_comum = df['Age'].value_counts().idxmax()
    st.subheader("🔹 Faixa etária mais comum")
    st.write(f"A faixa etária mais comum é: {idade_comum}")

elif op == "Gênero mais comum":
    genero_comum = df['Gender'].value_counts().idxmax()
    st.subheader("🔹 Gênero mais comum")
    st.write(f"O gênero mais comum é: {genero_comum}")

elif op == "Renda mais comum":
    renda_comum = df['Income_Level'].value_counts().idxmax()
    st.subheader("🔹 Nível de renda mais comum")
    st.write(f"O nível de renda mais comum é: {renda_comum}")

elif op == "Profissão mais comum":
    profissao_comum = df['Occupation'].value_counts().idxmax()
    st.subheader("🔹 Profissão mais comum")
    st.write(f"A profissão mais comum é: {profissao_comum}")

elif op == "Idade média por nível de renda":
    st.subheader("🔹 Idade média por nível de renda")
    idade_media_renda = df.groupby('Income_Level')['Age'].mean().sort_values()
    st.dataframe(idade_media_renda)

elif op == "Idade média por gênero":
    st.subheader("🔹 Idade média por gênero")
    idade_media_genero = df.groupby('Gender')['Age'].mean()
    st.dataframe(idade_media_genero)

elif op == "Proporção por nível de renda":
    st.subheader("🔹 Proporção de consumidores por nível de renda")
    proporcao = df['Income_Level'].value_counts(normalize=True) * 100
    st.bar_chart(proporcao)

elif op == "Valor médio por compra":
    media_compra = df['Purchase_Amount(USD)'].mean()
    st.subheader("🔹 Valor médio por compra")
    st.write(f"O valor médio gasto por compra é de ${media_compra:.2f} USD")

elif op == "Compras online vs loja física":
    origem = df['Purchase_Origin'].value_counts()
    st.subheader("🔹 Origem das compras")
    st.bar_chart(origem)

elif op == "Valor médio por gênero":
    st.subheader("🔹 Valor médio gasto por gênero")
    media_genero = df.groupby('Gender')['Purchase_Amount(USD)'].mean()
    st.dataframe(media_genero)

elif op == "Valor médio por estado civil":
    st.subheader("🔹 Valor médio gasto por estado civil")
    media_estado = df.groupby('Marital_Status')['Purchase_Amount(USD)'].mean()
    st.dataframe(media_estado)
