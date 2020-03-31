segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

minutos = segundos // 60
segundosrestantes = segundos % 60

horas = minutos // 60
minutosrestantes = minutos % 60

dias = horas // 24
horasrestantes = horas % 24

print(f"{dias} dias, {horasrestantes} horas, {minutosrestantes} minutos e {segundosrestantes} segundos.")anos = dias // 365
diascalculo = dias % 365

meses = diascalculo // 30
diasrestantes = diascalculo % 30

print(f"{segundos} segundos são equivalentes à: {anos} anos, {meses} meses, {diasrestantes} dias, {horasrestantes} horas, {minutosrestantes} minutos e {segundosrestantes} segundos.")

