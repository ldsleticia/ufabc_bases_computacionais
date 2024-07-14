import pandas as pd

df = pd.read_csv('fake-file06.csv')
print(df.query("Idade <= 42 & Funcionario <= 10"))
