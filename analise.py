import pandas as pd
import io

df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')
column_names = df.columns
pd.set_option('display.max_rows', None)  # mostra todas as linhas (tira os ... que o pandas resume)
pd.set_option('display.max_columns', None)  # mostra todas as colunas (tira os ... que o pandas resume)
pd.set_option('display.expand_frame_repr', False) # deve mostrar todos os cabecalhos (tira os ... que o pandas resume)

# Qual é o público alvo?

# quantidade de cada gênero -> feito

# print(df['Gender'].value_counts()) -> feito

# porcentagem de cada gênero -> feito

# print(df['Gender'].value_counts(normalize=True) * 100) -> feito

# Quantos solteiros tem?

# Qual é a idade média dos clientes?
# print(f'Idade média dos clientes: {df["Age"].mean()}')

# Qual é a idade média por nível de renda?

# Qual é a idade média por gênero?

# Qual é a proporção de clientes por nível de renda (Baixa, Média, Alta)?

# Qual é a categoria de produto mais comprada?

# Qual é o valor médio gasto por compra?

# Qual é o método de pagamento mais usado?

# Quantas compras foram feitas online vs. em loja física?

# Qual é a avaliação média dos produtos?

# O valor médio de compra é maior para clientes do gênero feminino ou masculino?

# O valor médio de compra pelo marital status



def info_data():
    print('\nDeseja ver que informação da tablea?\n1 - Quantidade de linhas e colunas\n2 - Nome das colunas\n3 - Tipos de dados contidos no arquivo\n4 - Quantidade de cada genero\n5 - thinkingggg.........')

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

    elif op == 4:
        print('Deseja ver em porcentagem?\nS/N')
        op = input('- ')
        if op == 'S'.lower():
            print(df['Gender'].value_counts(normalize=True) * 100)
        elif op == 'N'.lower():
            print(df['Gender'].value_counts())




def main():
    while True:
        print('\nBem vindo ao sistema de análise! O que deseja fazer?\n1 - Informações do arquio\n2 - Filtro de pesquisa\n3 - Ocorrências\n4 - Valores totais e médios\n5 - #pensando ainda...\n')

        op = int(input('- '))

        if op == 1:
            info_data()


main()