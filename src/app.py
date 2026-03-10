import pandas as pd
import numpy as np

#leitura do banco de dados
df = pd.read_csv("./data/acidentes_brasil.csv", sep=";", encoding="latin1")

#padronizar nome das colunas
df = df.rename(columns = {'ï»¿id': 'id'}, inplace=False)
df.columns = (df.columns.str.strip().str.lower().str.replace(' ', '_'))

#tipificando colunas
df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce', dayfirst=True)
df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S', errors='coerce')
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

print(df.info())

