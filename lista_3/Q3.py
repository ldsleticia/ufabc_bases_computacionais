import matplotlib.pyplot as plt
import numpy as np

numero_de_dias = int(input("Quantos dias voceê deseja calcular? "))

x = np.arange(-10, 31, 1)
y = (1 * (x * x)) + (-17 * x) + (-17)

plt.plot(x, y)

plt.hlines(((1 * (numero_de_dias * numero_de_dias)) + (-17 *
           numero_de_dias) + (-17)), 0, numero_de_dias, 'r', linestyles='dashed')

plt.vlines(numero_de_dias, 0, ((1 * (numero_de_dias * numero_de_dias)
                                ) + (-17 * numero_de_dias) + (-17)), 'r', linestyles='--')

plt.xlim(-3, 29)

plt.ylim(-100, 220)

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
plt.scatter([numero_de_dias, ], [(1 * (numero_de_dias * numero_de_dias)
                                  ) + (-17 * numero_de_dias) + (-17), ], 40, color='red')

print("%d reais" % ((1 * (numero_de_dias * numero_de_dias)) +
      (-17 * numero_de_dias) + (-17)))
# plt.show()
