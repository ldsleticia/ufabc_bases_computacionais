import pandas as pd

df = pd.read_csv("fake-classrooms03.csv")
prova_selecionada = input()
# qtd_valores = df[prova_selecionada].value_counts()
print(str(df[prova_selecionada].value_counts()))