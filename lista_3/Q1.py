import matplotlib.pyplot as plt
import numpy as np

from matplotlib.testing.decorators import compare_images

pathGrafico = 'figBCCgrafico07.png'
pathGrafico1 = 'figBCCgrafico071.png'

x = np.arange(-1, 10, 1)
y = (-8 * x) + 14

plt.plot(x, y, 'b')

plt.hlines(((-8 * 9) + 14), 0, 9, linewidth=0.5,
           color='r', linestyles='dashed')

plt.vlines(9, 0, ((-8 * 9) + 14), linewidth=0.5, color='r', linestyles='--')

plt.xlim(-1.5, 9.5)

plt.ylim(-62, 26)

# 1) Obter as informações gráfico
ax = plt.gca()  # gca significa 'get current axis'

# 2) Retirar a linha da DIREITA (color = none)
ax.spines['right'].set_color('none')

# 3) Retirar a linha de CIMA (color = none)
ax.spines['top'].set_color('none')

# 4) Posicionar a linha de BAIXO, exatamente no "y=0"
ax.spines['bottom'].set_position(('data', 0))

# 5) Posicionar a linha da ESQUERDA, exatamente no "x=0"
ax.spines['left'].set_position(('data', 0))

# 6) Marcar um ponto de coord (x,y) com espessura 50 e cor vermelha
plt.scatter([9, ], [(-8 * 9) + 14, ], 50, color='red')

print("%d reais" % ((-8 * 9) + 14))
# plt.show()

# plt.savefig(pathGrafico)
# pathGraficoCompare = 'figBCCgrafico01(a-8)(b14).png'
# print(compare_images(pathGrafico, pathGraficoCompare, 0.5))
