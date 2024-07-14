import math

a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = 2

delta = b**2 - 4 * a * c
primeira_raiz = (-b + math.sqrt(delta)) / 2 * a
segunda_raiz = (-b - math.sqrt(delta)) / 2 * a

print("%.2f \n%.2f" % (primeira_raiz, segunda_raiz))
