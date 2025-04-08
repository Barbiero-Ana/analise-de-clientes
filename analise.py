import pandas as pd
import io

df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')
column_names = df.columns
pd.set_option('display.max_rows', None)  # mostra todas as linhas (tira os ... que o pandas resume)
pd.set_option('display.max_columns', None)  # mostra todas as colunas (tira os ... que o pandas resume)
pd.set_option('display.expand_frame_repr', False) # deve mostrar todos os cabecalhos (tira os ... que o pandas resume)

def info_data():
    print('\nDeseja ver que informação da tablea?\n1 - Quantidade de linhas e colunas\n2 - Nome das colunas\n3 - Tipos de dados contidos no arquivo\n4 - pensando ainda...')

    op = int(input('- '))
    if op == 1:
        print(f'\nNúmero de linhas: {df.shape[0]} | Número de colunas: {df.shape[1]}\n')
    elif op == 2:
        print(f'\nColunas disponiveis no arquivo:\n')
        for i, col in enumerate(column_names, start= 1):
            print(f'{i}. {col}')
    elif op == 3:
        buffer = io.StringIO()
        df.info(buf=buffer)
        info = buffer.getvalue()
        print(f'\n{info}\n')











def main():

    print('Bem vindo ao sistema de análise! O que deseja fazer?\n1 - Informações do arquio\n2 - Filtro de pesquisa\n3 - Ocorrências\n4 - Valores totais e médios\n5 - #pensando ainda...\n')

    op = int(input('- '))

    if op == 1:
        info_data()