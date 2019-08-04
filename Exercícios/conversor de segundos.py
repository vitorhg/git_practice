segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

minutos = segundos // 60
segundosrestantes = segundos % 60

horas = minutos // 60
minutosrestantes = minutos % 60

dias = horas // 24
horasrestantes = horas % 24

print(f"{dias} dias, {horasrestantes} horas, {minutosrestantes} minutos e {segundosrestantes} segundos.")