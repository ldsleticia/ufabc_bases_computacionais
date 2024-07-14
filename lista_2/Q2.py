import pandas as pd

df = pd.read_csv('fake-file13.csv')
sorted_df = df.sort_values(["Meses", "Salario"], ascending=[True, True])
print(sorted_df[["Idade", "Meses", "Salario"]].values[0])
