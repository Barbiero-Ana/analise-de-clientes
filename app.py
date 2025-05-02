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



df = pd.read_csv(csv_file)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
column_names = df.columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

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


def info_arqv():
    st.header('Informações sobre o dataset')
    op = st.sidebar.selectbox('Selecione um opção',[
        'Titulo das colunas',
        'Número de linhas e colunas',
        'Tipo dos dados armazenados no dataset',
        ''
    ], key='inf_option')

    if op == 'Titulo das colunas':
        st.subheader('Colunas do dataset')
        view = st.radio(
            'Escolha o modo de visualização:',
            ['Tabela interativa', 'Cartão interativo'],
            key='view_mode'
        )

# Dados das colunas
    columns_df = pd.DataFrame({
        'Índice': range(1, len(column_names) + 1),
        'Nome da Coluna': column_names,
        'Descrição': [
            'ID de consumidor' if col == 'Customer_ID' else
            'Idade' if col == 'Age' else
            'Gênero' if col == 'Gender' else
            'Nivel de renda' if col == 'Income_Level' else
            'Estado civil' if col == 'Marital_Status' else
            'Nivel de educação' if col == 'Education_Level' else
            'Ocupação' if col == 'Occupation' else
            'Localização' if col == 'Location' else
            'Categoria de compra' if col == 'Purchase_Category' else
            'Montante de compra' if col == 'Purchase_Amount' else
            'Frequência de compra' if col == 'Frequency_of_Purchase' else
            'Canal de compra' if col == 'Purchase_Channel' else
            'Fidelidade a marca' if col == 'Brand_Loyalty' else
            'Feedback do produto' if col == 'Product_Rating' else
            'Tempo gasto em pesquisa de produto' if col == 'Time_Spent_on_Product_Research(hours)' else
            'Influência nas midias sociais' if col == 'Social_Media_Influence' else
            'Sensibilidade ao desconto' if col == 'Discount_Sensitivity' else
            'Taxa de retorno' if col == 'Return_Rate' else
            'Taxa de satisfação do cliente' if col == 'Customer_Satisfaction' else
            'Engajamento com propagandas' if col == 'Engagement_with_Ads' else
            'Dispositivo utilizado para compra' if col == 'Device_Used_for_Shopping' else
            'Método de pagamento' if col == 'Payment_Method' else
            'Tempo de compra' if col == 'Time_of_Purchase' else
            'Desconto utilizado' if col == 'Discount_Used' else
            'Membro do programa de fidelidade do cliente' if col == 'Customer_Loyalty_Program_Member' else
            'Itenção de compra' if col == 'Purchase_Intent' else
            'Preferência de envio' if col == 'Shipping_Preference' else
            'Tempo de decisão' if col == 'Time_to_Decision' else
            'Descrição não disponível'
            for col in column_names
        ]
    })
    



# '''
# -> por na parte de filtro:
#     Quantidade de cada genero 
#     Localizações de compras realizadas
#     Tempo gasto por cliente no produto

# -> por na parte de métricas:
#     Distribuição por nível de escolaridade
#     Distribuição por categoria de compra

# '''