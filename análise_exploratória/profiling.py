import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("../data/acidentes_brasil.csv", sep=";", encoding="latin1")

profile = ProfileReport(
    df,
    title = "Análise exploratória",
)
profile.to_file("output.html")