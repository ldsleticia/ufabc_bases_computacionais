import pandas as pd

df = pd.read_csv("fake-classrooms17.csv")
prova_selecionada = input()
desvio_padrao = df[prova_selecionada].std()
print('%.2f' % desvio_padrao)
