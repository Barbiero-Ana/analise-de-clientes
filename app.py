import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title='Análise de Ecommerce Consumer', layout='wide')

csv_file = 'Ecommerce_Consumer_Behavior_Analysis_Data.csv'
if not os.path.exists(csv_file):
    st.error(f"Arquivo {csv_file} não encontrado. Certifique-se de que o arquivo está no diretório correto.")
    st.stop()

st.title('Análise de dados de um Ecommerce')
st.markdown('Esta análise irá apresentar dados de consumidores e suas comprar em um Ecommerce')

op = st.sidebar.selectbox('Escolha a opção que deseja', [
    'Informações sobre o aquivo',
    'Filtro de busca',
    'Ocorrências',
    'Médias',
    'Métricas avançadas'
])


# CSS personalizado para cartões 
st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #4F1C51 0%, #6B2D6D 100%);
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 10px;
        color: white;
        animation: fadeIn 0.5s ease-in;
    }
    .metric-card h3 {
        margin: 0;
        font-size: 1.2em;
        color: #FFFFFF;
    }
    .metric-card p {
        margin: 5px 0 0;
        font-size: 1.5em;
        font-weight: bold;
    }
    .game-card {
        background: linear-gradient(135deg, #4F1C51 0%, #6B2D6D 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        margin: 10px 0;
        color: white;
        animation: fadeIn 0.5s ease-in;
    }
    .game-card h2 {
        margin: 0 0 10px;
        font-size: 1.8em;
        color: #FFFFFF;
    }
    .game-card p {
        margin: 5px 0;
        font-size: 1.1em;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .counter {
        font-size: 1.5em;
        font-weight: bold;
        color: #FFFFFF;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #4CAF50;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
    <script>
    function animateValue(id, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const value = Math.floor(progress * (end - start) + start);
            document.getElementById(id).innerText = value.toLocaleString();
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
    </script>
""", unsafe_allow_html=True)
