segunda_temperatura = 55.0
primeira_temperatura = float(input("Insira a primeira temperatura: "))

temp_um_em_fahrenheit = (primeira_temperatura * 9 / 5) + 32
temp_dois_em_fahrenheit = (segunda_temperatura * 9 / 5) + 32

print("%.2f \n%.2f" % (temp_um_em_fahrenheit, temp_dois_em_fahrenheit))