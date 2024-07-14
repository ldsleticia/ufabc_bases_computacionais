import pandas as pd

df = pd.read_csv('fake-file12.csv')
maior_salario = df["Salario"].values.max()
print(maior_salario)
