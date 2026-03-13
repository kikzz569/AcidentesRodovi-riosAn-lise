from sqlalchemy import create_engine

def load(df):
    try:
        engine = create_engine('postgresql+psycopg2://postgres:Gaman569@localhost:5432/acidentes_brasil')
    
        df.to_sql(
            name = 'acidentes_silver',
            con = engine,
            schema = 'silver',
            if_exists = 'replace',
            index = False,
            chunksize = 5000
    )   
        print(f"Linhas: {len(df)}")
        print('Dados carregados com sucesso')
    except Exception as e:
        print(f'Erro: {e}')