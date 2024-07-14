import pandas as pd

df = pd.read_csv("fake-classrooms08.csv")
prova_selecionada = input()
variancia = df[prova_selecionada].var()
print('%.2f' % variancia)