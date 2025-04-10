import pandas as pd
import io


df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')
column_names = df.columns
pd.set_option('display.max_rows', None)  # mostra todas as linhas (tira os ... que o pandas resume)
pd.set_option('display.max_columns', None)  # mostra todas as colunas (tira os ... que o pandas resume)
pd.set_option('display.expand_frame_repr', False) # deve mostrar todos os cabecalhos (tira os ... que o pandas resume)




# Qual é o público alvo?


# Qual é a idade média por nível de renda?

# Qual é a idade média por gênero?

# Qual é a proporção de clientes por nível de renda (Baixa, Média, Alta)?

# Qual é o valor médio gasto por compra?

# Quantas compras foram feitas online vs. em loja física?

# O valor médio de compra é maior para clientes do gênero feminino ou masculino?

# O valor médio de compra pelo marital status



def info_data():
    print('\nDeseja ver que informação da tablea?\n1 - Quantidade de linhas e colunas\n2 - Nome das colunas\n3 - Tipos de dados contidos no arquivo\n4 - Quantidade de cada genero\n5 - Distribuição por nível de escolaridade\n6 - Distribuição por categoria de compra\n7 - Localizações de compras realizadas\n8 - Tempo gasto por cliente no produto\n9 - Avaliação do produto por categoria\n10 - ')

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

    elif op == 5:
        print('Deseja ver em porcentagem?\nS/N')
        op = input('- ')
        if op == 'S'.lower():
            print(df['Education_Level'].value_counts(normalize=True) * 100)
        elif op == 'N'.lower():
            print(df['Education_Level'].value_counts())

    elif op == 6:
        print('Deseja ver em porcentagem?\nS/N')
        op = input('- ')
        if op == 'S'.lower():
            print(df['Purchase_Category'].value_counts(normalize= True) * 100)
        elif op == 'N'.lower():
            print(df['Purchase_Category'].value_counts())
        

    elif op == 7:
        print('Deseja ver em porcentagem?\nS/N')
        op = input('- ')
        if op == 'S'.lower():
            print(df['Location'].value_counts(normalize= True) * 100)
        elif op == 'N'.lower():
            print(df['Location'])


    elif op == 8:
        print(df['Time_Spent_on_Product_Research(hours)'])

    elif op == 9:
        print('Deseja ver:\n1 - todos\n2 - Quantidade em especifico\n3 - Avaliação média dos produtos')
        op = int(input('- '))
        if op == 1:
            print('\nAvaliação dos produtos\n')
            for i, row in df.iterrows():
                print(f'- Cliente id: {row['Customer_ID']} | Categoria: {row['Purchase_Category']} | Avaliação: {row['Product_Rating']}')
        elif op == 2:
            n = int(input('Digite a quantidade que deseja ver: '))
            print(f'\n{n} top avaliações:\n')
            top = df.sort_values(by='Product_Rating', ascending= False).head(n)
            for i, row in top.iterrows():
                print(f'{i+1}° - Cliente ID: {row['Customer_ID']} | Categoria: {row["Purchase_Category"]} | Avaliação: {row["Product_Rating"]}')
        elif op == 3:
            media = df['Product_Rating'].mean()
            print(f'A média das avaliações é igual a -> {media}')

def membership():
    membro = df[df['Customer_Loyalty_Program_Member']]
    print(f'{membro[['Customer_ID', 'Age', 'Customer_Loyalty_Program_Member']]}')

def filtro_busca():
    # na opcao 2 - > inserir opcao do usuario poder escolher entre buscar por: solteiro, casado (ou outro estado social)/ genero ou tipo de renda
    print('Deseja filtrar como?\n1 - Qual o método de pagamento mais utilizado\n2 - Quantidade por filtro\n3 - Categoria de produtos mais comprada\n4 - pensando ainda')
    op = int(input('- '))
    if op == 1:
        print('\nDeseja ver:\n1 - Quantia em especifico\n2 - O método que de fato mais aparece')
        op = int(input('- '))
        if op == 1:
            n = int(input('Digite a quantidade de métodos que deseja ver: '))
            freq = df['Payment_Method'].value_counts().head(n)
            qtd = df['Payment_Method'].value_counts().max()
            for i, (Payment_Method, qtd) in enumerate(freq.items(), start= 1):
                print(f'\n{i}° {Payment_Method} | Apareceu {qtd} vezes')

        elif op == 2:
            freq = df['Payment_Method'].value_counts().idxmax()
            qtd = df['Payment_Method'].value_counts().max()
            print(f'\nO método de pagamento mais utilizado foi: {freq} | Utilizado {qtd} vezes')

    elif op == 2:
        print('Deseja ver:\n1 - Ver estados cívis\n2 - Ver  profissão dos usuários\n3 - Ver niveis de escolaridade no documento\n4 - Filtrar por usuários que fazem parte do programa de membro')
        op = int(input('- '))
        if op == 1:
            filtro_status_marital()
        elif op == 2:
            filtro_profissao()
        elif op == 3:
            escolaridade()
        elif op == 4:
            membership()
    elif op == 3:
        freq = df['Purchase_Category'].value_counts().idxmax()
        qtd = df['Purchase_Category'].value_counts().max()
        print(f'\nA categoria de venda que mais teve vendas foi: {freq} | Sendo comprado(a): {qtd} vezes')

def escolaridade():
    print('Deseja ver:\n1 - Todas as escolaridades contidas no documento\n2 - Filtrar por escolaridade em especifico')
    op = int(input('- '))

    if op == 1:
        estud = df['Education_Level'].value_counts()
        print(f'\n{estud}')

    elif op == 2:
        print('\n1 - Ensino médio\n2 - Bacharelado\n3 - Mestre')
        op = int(input('- '))
        if op == 1:
            escola = 'High School'
            status = df[df['Education_Level'].str.strip().str.lower() == escola.lower()]
            print(f'\nUsuários com escolaridade de nível: {escola}')
            print(status[['Customer_ID', 'Education_Level']])

        elif op == 2:
            escola = "Bachelor's"
            status = df[df['Education_Level'].str.strip().str.lower() == escola.lower()]
            print(f'\nUsuários com escolaridade de nível: {escola}')
            print(status[['Customer_ID', 'Education_Level']])

        elif op == 3:
            escola = "Master's"
            status = df[df['Education_Level'].str.strip().str.lower() == escola.lower()]
            print(f'\nUsuários com escolaridade de nível: {escola}')
            print(status[['Customer_ID', 'Education_Level']])
        else:
            print('Entrada inválida, tente novamente...')

def filtro_profissao():
    print('Deseja ver:\n1 - Todas as profissoes contidas no documento')
    op = int(input('- '))
    if op == 1:
        prof = df['Occupation'].value_counts()
        print(prof)

def filtro_status_marital():
    print('Buscar por:\n1 - estado civil em especifico\n2 - Ver todos')
    op = int(input('- '))

    if op == 1:
        print('Buscar por:\n1 - Viúvos\n2 - Casados\n3 - Divorciados\n4 - Solteiros')
        op = int(input('- '))
        if op == 1:
            status = 'Widowed'
            print('Deseja ver:\n1 - todos com ID de usuários\n2 - Apenas a quantidade total')
            op = int(input('- '))
            if op == 1:
                print('\nUsuários Viúvos\n')
                marital = df[df['Marital_Status'] == status]
                if marital.empty:
                    print('Erro, nenhum usuário com este status civil...')
                else:
                    print(f'\nUsuário de status civil igual a: {status}/ Viuvo\n')
                    for i, row in marital.iterrows():
                        print(f'- Cliente ID: {row['Customer_ID']} | Estado civil: {row['Marital_Status']}')
            elif op == 2:
                val = df['Marital_Status'].value_counts().get(status, 0)
                print(f'\nTotal de usuários Viuvos: {val}')

        elif op == 2:
            status = 'Married'
            print('Deseja ver:\n1 - todos com ID de usuários\n2 - Apenas a quantidade total')
            op = int(input('- '))
            if op == 1:
                print('\nUsuários Casados\n')
                marital = df[df['Marital_Status'] == status]
                if marital.empty:
                    print('Erro, nenhum usuário com este status civil...')
                else:
                    print(f'\nUsuário de status civil igual a: {status}/ Casados\n')
                    for i, row in marital.iterrows():
                        print(f'- Cliente ID: {row['Customer_ID']} | Estado civil: {row['Marital_Status']}')
            elif op == 2:
                val = df['Marital_Status'].value_counts().get(status, 0)
                print(f'\nTotal de usuários Casados: {val}')

        elif op == 3:
            status = 'Divorced'
            print('Deseja ver:\n1 - todos com ID de usuários\n2 - Apenas a quantidade total')
            op = int(input('- '))
            if op == 1:
                print('\nUsuários Divorciados\n')
                marital = df[df['Marital_Status'] == status]
                if marital.empty:
                    print('Erro, nenhum usuário com este status civil...')
                else:
                    print(f'\nUsuário de status civil igual a: {status}/ Divorciados\n')
                    for i, row in marital.iterrows():
                        print(f'- Cliente ID: {row['Customer_ID']} | Estado civil: {row['Marital_Status']}')
            elif op == 2:
                val = df['Marital_Status'].value_counts().get(status, 0)
                print(f'\nTotal de usuários Divorciados: {val}')

        elif op == 4:
            status = 'Single'
            print('Deseja ver:\n1 - todos com ID de usuários\n2 - Apenas a quantidade total')
            op = int(input('- '))
            if op == 1:
                print('\nUsuários Solteiros\n')
                marital = df[df['Marital_Status'] == status]
                if marital.empty:
                    print('Erro, nenhum usuário com este status civil...')
                else:
                    print(f'\nUsuário de status civil igual a: {status}/ Solteiros\n')
                    for i, row in marital.iterrows():
                        print(f'- Cliente ID: {row['Customer_ID']} | Estado civil: {row['Marital_Status']}')
            elif op == 2:
                val = df['Marital_Status'].value_counts().get(status, 0)
                print(f'\nTotal de usuários solteiros: {val}')
        
                
    elif op == 2:
        print(f'{df['Marital_Status'].value_counts()}')

def ocorrencias():
    print('\nDeseja ver que tipo de ocorrência?\n1 - Qual a proporção de clientes por nível de renda\n3 - ')


def media_total():

    # na op 4 -> incluir filtrar ou demonstrar se o genero masculino ou feminino apresentam uma média de compra maior (no caso apresentar quem tem a maior média de compra)

    print('\n1 - Média da idade dos clientes\n2 - Média da idade dos clientes dividido por nivel de renda\n3 - Média dos clientes por genero\n4 - Valor médio gasto por compra\n5 - Compras em loja fisica vs loja digital\n6 - Valor médio de compra por estado civil')
    op = int(input('- '))

    if op == 1:
        print(f'Idade média dos clientes: {df["Age"].mean()}')
    elif op == 2:
        print()


def main():
    while True:
        print('\nBem vindo ao sistema de análise! O que deseja fazer?\n1 - Informações do arquivo\n2 - Filtro de pesquisa\n3 - Ocorrências\n4 - Valores totais e médios\n5 - Público alvo\n')

        op = int(input('- '))

        if op == 1:
            info_data()
        elif op == 2:
            filtro_busca()
        elif op == 3:
            ocorrencias()


main()