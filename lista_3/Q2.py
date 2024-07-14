import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10 , 14, 1)
y = (-3 * (x * x)) + ( 10 * x) + 17

plt.plot(x, y)

plt.hlines(((-3 * (9 * 9)) + ( 10 * 9) + 17), 0, 9, 'r', linestyles='dashed')

plt.vlines(9, 0, ((-3 * (9 * 9)) + ( 10 * 9) + 17), 'r', linestyles='--')

plt.xlim(-3, 10)

plt.ylim(-175 , 25)

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
plt.scatter([9, ], [(-3 * (9 * 9)) + ( 10 * 9) + 17, ], 50, color='red')

print("%d reais" % ((-3 * (9 * 9)) + ( 10 * 9) + 17))
# plt.show()
