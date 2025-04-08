import pandas as pd


df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')

def info_data():
    print('\nDeseja ver que informação da tablea?\n1 - Quantidade de linhas e colunas\n2 - Nome das colunas\n3 - Tipos de dados contidos no arquivo\n4 - pensando ainda...')

    op = int(input('- '))
    if op == 1:
        qtd= df.