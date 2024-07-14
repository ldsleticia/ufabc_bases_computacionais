import pandas as pd

df = pd.read_csv("fake-classrooms19.csv")
prova_selecionada = input()
mediana = df[prova_selecionada].median()
print('%.2f' % mediana)