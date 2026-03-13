import pandas as pd
import numpy as np

def extract():
    #leitura do banco de dados
    df = pd.read_csv("../data/acidentes_brasil.csv", sep=";", encoding="utf-8-sig", low_memory = False)

    #limpeza de duplicatas
    df = df.drop_duplicates()

    #padronizar nome das colunas
    df.columns = (df.columns.str.strip().str.lower().str.replace(' ', '_', regex=True))

    #corrigindo latitude e longitude
    df['latitude'] = (df['latitude'].astype(str).str.replace(',', '.', regex=False)
    )
    df['longitude'] = (df['longitude'].astype(str).str.replace(',', '.', regex=False)
    )

    #tipificando colunas
    df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce', dayfirst=True).dt.date
    df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S', errors='coerce').dt.time
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

    #padronizando colunas de texto
    cols_texto = ['uf', 'municipio', 'causa_acidente', 'tipo_acidente', 'classificacao_acidente']
    for col in cols_texto:
        if col in df.columns:
            df[col] = df[col].str.strip().str.upper()

    #Correção inconsistencia coluna "pessoas"
    df["pessoas_corrigido"] = (
    df["mortos"]
    + df["feridos_graves"]
    + df["feridos_leves"]
    + df["ilesos"]
    + df["ignorados"]
)
    inconsistentes = df[df["pessoas"] != df["pessoas_corrigido"]]

    df["pessoas"] = df["pessoas_corrigido"]
    df.drop(columns="pessoas_corrigido", inplace=True)

    print('Base de dados extraido e limpo com sucesso')

    return df