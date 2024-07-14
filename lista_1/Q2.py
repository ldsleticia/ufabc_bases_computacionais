data_nascimeto_maria = 26
data_nascimeto_joao = int(input("Insira a data de nascimento do João: "))

calc_segundos_joao = data_nascimeto_joao * 365 * 24 * 60 * 60
calc_segundos_maria = data_nascimeto_maria * 365 * 24 * 60 * 60

print("%d \n%d" %
      (calc_segundos_maria, calc_segundos_joao))
