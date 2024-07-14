import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10 , 13, 1)
y = (3 * x) + -14

plt.plot(x, y)

plt.hlines(((3 * 8) + -14), 0, 8, 'r', linestyles='dashed')

plt.vlines(8, 0, ((3 * 8) + -14), 'r', linestyles='--')

plt.xlim(-1, 8.5)

plt.ylim(-19 , 10.3)

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
plt.scatter([8, ], [(3 * 8) + -14, ], 50, color='red')

print("%d reais" % ((3 * 8) + -14))
# plt.show()
