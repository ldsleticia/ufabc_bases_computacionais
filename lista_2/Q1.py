import pandas as pd

df = pd.read_csv('fake-file01.csv')

print(df[df["Meses"] < 33])
