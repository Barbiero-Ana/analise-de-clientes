import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os
import csv

# Configuração da página do Streamlit
st.set_page_config(page_title='Análise de Ecommerce Consumer', layout='wide')

# Inicializa o estado da sessão para rastrear o cartão clicado
if 'selected_column' not in st.session_state:
    st.session_state.selected_column = None

# Caminho do arquivo CSV
csv_file = 'Ecommerce_Consumer_Behavior_Analysis_Data.csv'

# Verifica se o arquivo existe
if not os.path.exists(csv_file):
    st.error(f"Arquivo {csv_file} não encontrado. Certifique-se de que o arquivo está no diretório correto.")
    st.stop()

# Tenta ler o arquivo CSV com tratamento de erros
try:
    df = pd.read_csv(csv_file, quoting=csv.QUOTE_ALL, encoding='latin1', engine='python', on_bad_lines='skip')
    st.warning("Algumas linhas foram puladas devido a erros de formatação (ex.: linha 24). Verifique o arquivo CSV para corrigir.")
    
    # Extrai o ano de Time_of_Purchase
    df['Year'] = pd.to_datetime(df['Time_of_Purchase'], errors='coerce', format='%m/%d/%Y').dt.year.astype('Int64')
    
    # Configurações do Pandas
    column_names = df.columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    # Interface do Streamlit
    st.title('Análise de dados de um Ecommerce')
    st.markdown('Esta análise irá apresentar dados de consumidores e suas compras em um Ecommerce')

    # Menu lateral
    op = st.sidebar.selectbox('Escolha a opção que deseja', [
        'Informações sobre o aquivo',
        'Filtro de busca',
        'Ocorrências',
        'Médias',
        'Métricas avançadas'
    ])

    # Função para exibir informações do dataset
    def info_arqv(column_names):
        st.header('Informações sobre o dataset')
        op = st.sidebar.selectbox('Selecione uma opção', [
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
                    'Nível de renda' if col == 'Income_Level' else
                    'Estado civil' if col == 'Marital_Status' else
                    'Nível de educação' if col == 'Education_Level' else
                    'Ocupação' if col == 'Occupation' else
                    'Localização' if col == 'Location' else
                    'Categoria de compra' if col == 'Purchase_Category' else
                    'Montante de compra' if col == 'Purchase_Amount' else
                    'Frequência de compra' if col == 'Frequency_of_Purchase' else
                    'Canal de compra' if col == 'Purchase_Channel' else
                    'Fidelidade à marca' if col == 'Brand_Loyalty' else
                    'Feedback do produto' if col == 'Product_Rating' else
                    'Tempo gasto em pesquisa de produto' if col == 'Time_Spent_on_Product_Research(hours)' else
                    'Influência nas mídias sociais' if col == 'Social_Media_Influence' else
                    'Sensibilidade ao desconto' if col == 'Discount_Sensitivity' else
                    'Taxa de retorno' if col == 'Return_Rate' else
                    'Taxa de satisfação do cliente' if col == 'Customer_Satisfaction' else
                    'Engajamento com propagandas' if col == 'Engagement_with_Ads' else
                    'Dispositivo utilizado para compra' if col == 'Device_Used_for_Shopping' else
                    'Método de pagamento' if col == 'Payment_Method' else
                    'Tempo de compra' if col == 'Time_of_Purchase' else
                    'Desconto utilizado' if col == 'Discount_Used' else
                    'Membro do programa de fidelidade do cliente' if col == 'Customer_Loyalty_Program_Member' else
                    'Intenção de compra' if col == 'Purchase_Intent' else
                    'Preferência de envio' if col == 'Shipping_Preference' else
                    'Tempo de decisão' if col == 'Time_to_Decision' else
                    'Descrição não disponível'
                    for col in column_names
                ]
            })

            if view == 'Tabela interativa':
                st.dataframe(columns_df)
            else:
                st.write("Clique em um cartão para ver detalhes da coluna:")
                # Organiza cartões em uma grade
                num_cols = 3
                rows = [columns_df[i:i + num_cols] for i in range(0, len(columns_df), num_cols)]
                for row in rows:
                    cols = st.columns(num_cols)
                    for idx, (_, col_data) in enumerate(row.iterrows()):
                        with cols[idx]:
                            col_name = col_data['Nome da Coluna']
                            if st.button(f"**{col_name}**", key=f"btn_{col_name}"):
                                st.session_state.selected_column = col_name
                            # Exibe detalhes se o cartão foi clicado
                            if st.session_state.selected_column == col_name:
                                num_rows = df[col_name].count()
                                data_type = str(df[col_name].dtype)
                                most_common = df[col_name].mode().iloc[0] if not df[col_name].mode().empty else "N/A"
                                st.markdown(f"""
                                    <div class='metric-card'>
                                        <h3>{col_name}</h3>
                                        <p>
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" style="vertical-align: middle; margin-right: 8px;">
                                                <path d="M4 6h16M4 12h16M4 18h16"/>
                                            </svg>
                                            <strong>Descrição:</strong> {col_data['Descrição']}
                                        </p>
                                        <p>
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" style="vertical-align: middle; margin-right: 8px;">
                                                <path d="M12 4v16m8-8H4"/>
                                            </svg>
                                            <strong>Número de linhas:</strong> {num_rows}
                                        </p>
                                        <p>
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" style="vertical-align: middle; margin-right: 8px;">
                                                <path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                                            </svg>
                                            <strong>Tipo de dado:</strong> {data_type}
                                        </p>
                                        <p>
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" style="vertical-align: middle; margin-right: 8px;">
                                                <path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.783-.57-.38-1.81.588-1.81h4.915a1 1 0 00.95-.69l1.519-4.674z"/>
                                            </svg>
                                            <strong>Valor mais frequente:</strong> {most_common}
                                        </p>
                                    </div>
                                """, unsafe_allow_html=True)

        elif op == 'Número de linhas e colunas':
            st.subheader('Dimensões do dataset')
            st.write(f"Número de linhas: {df.shape[0]}")
            st.write(f"Número de colunas: {df.shape[1]}")

        elif op == 'Tipo dos dados armazenados no dataset':
            st.subheader('Tipos de dados das colunas')
            st.dataframe(df.dtypes)

    # Lógica do menu principal
    if op == 'Informações sobre o aquivo':
        info_arqv(column_names)

except pd.errors.ParserError as e:
    st.error(f"Erro ao ler o arquivo CSV: {e}")
    try:
        with open(csv_file, 'r', encoding='latin1') as file:
            lines = file.readlines()
            header = lines[0].strip()
            line_24 = lines[23].strip()  # Linha 24 é índice 23 (0-based, contando cabeçalho)
            st.write("**Cabeçalho:**", header)
            st.write("**Linha 24:**", line_24)
            with open('csv_error_log.txt', 'w', encoding='utf-8') as log_file:
                log_file.write(f"Cabeçalho:\n{header}\n\nLinha 24:\n{line_24}\n")
            st.write("Linha 24 salva em 'csv_error_log.txt' no diretório do aplicativo.")
            st.info("Para corrigir, abra o arquivo CSV em um editor de texto, vá até a linha 24, e verifique se há vírgulas extras. Campos como 'Location' ou 'Purchase_Category' devem estar entre aspas se contiverem vírgulas.")
    except Exception as e2:
        st.error(f"Erro ao ler o arquivo para depuração: {e2}")
        try:
            with open(csv_file, 'r', encoding='latin1') as file:
                for i, line in enumerate(file, 1):
                    if i == 24:
                        st.write("**Linha 24 (leitura direta):**", line.strip())
                        with open('csv_error_log.txt', 'a', encoding='utf-8') as log_file:
                            log_file.write(f"\nLinha 24 (leitura direta):\n{line.strip()}\n")
                        break
        except Exception as e3:
            st.error(f"Erro ao ler a linha 24 diretamente: {e3}")
    st.stop()
except Exception as e:
    st.error(f"Erro inesperado ao ler o arquivo CSV: {e}")
    st.stop()

# CSS personalizado
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    .metric-card {
        background: linear-gradient(145deg, #6B46C1 0%, #9988DD 100%);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        color: #FFFFFF;
        font-family: 'Roboto', sans-serif;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        opacity: 0.97;
    }
    .metric-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
        opacity: 1;
    }
    .metric-card h3 {
        margin: 0 0 12px;
        font-size: 1.6em;
        font-weight: 700;
        color: #FFFFFF;
    }
    .metric-card p {
        margin: 8px 0;
        font-size: 1.1em;
        line-height: 1.6;
        display: flex;
        align-items: center;
    }
    .metric-card p svg {
        margin-right: 8px;
    }
    .stButton>button {
        background: linear-gradient(145deg, #6B46C1 0%, #9988DD 100%);
        color: #FFFFFF;
        border: none;
        border-radius: 12px;
        padding: 14px;
        width: 100%;
        text-align: left;
        font-size: 1.2em;
        font-weight: 500;
        font-family: 'Roboto', sans-serif;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:active {
        transform: scale(0.98);
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)