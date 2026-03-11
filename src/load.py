from sqlalchemy import create_engine

def load(df):
    try:
        engine = create_engine('postgresql://postgres.azimreeippevyjdswfrm:Gaman_320790@aws-0-us-west-2.pooler.supabase.com:6543/postgres')
    
        df.to_sql(
            name = 'acidentes_silver',
            con = engine,
            if_exists = 'replace',
            index = False,
            chunksize = 5000
    )   
        print(f"Linhas: {len(df)}")
        print('Dados carregados com sucesso')
    except Exception as e:
        print(f'Erro: {e}')