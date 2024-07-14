import pandas as pd

df = pd.read_csv('fake-file18.csv')
df_linha = df.values[3][2]
print(df_linha)
