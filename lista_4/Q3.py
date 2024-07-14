import pandas as pd

df = pd.read_csv("fake-classrooms08.csv")
prova_selecionada = input()
moda = df[prova_selecionada].mode()
print('%.2f' % moda)
