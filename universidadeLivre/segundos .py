segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segundos = int(segundos_str)

dias = total_segundos // 86400
segundos_restantes = total_segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")