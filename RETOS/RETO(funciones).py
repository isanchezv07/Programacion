
tiempos_minutos = [45, 30, 50, 60, 25, 40, 55]

promedio_diario = lambda tiempos: sum(tiempos) / len(tiempos) if tiempos else 0

promedio_minutos = promedio_diario(tiempos_minutos)
print(f"El tiempo promedio diario de uso de dispositivos antes de dormir es de {promedio_minutos:.2f} minutos.")

minutos_a_horas = lambda minutos: minutos / 60

promedio_horas = minutos_a_horas(promedio_minutos)
print(f"El tiempo promedio diario de uso de dispositivos antes de dormir es de {promedio_horas:.2f} horas por día.")

minutos_a_segundos = lambda minutos: minutos * 60

promedio_segundos = minutos_a_segundos(promedio_minutos)
print(f"El tiempo promedio diario de uso de dispositivos antes de dormir es de {promedio_segundos:.2f} segundos por día.")

tiempos_horas = list(map(minutos_a_horas, tiempos_minutos))
print(f"Tiempos en horas: {tiempos_horas}")

dias_mas_de_45 = list(filter(lambda x: x > 45, tiempos_minutos))
print(f"Días con más de 45 minutos de uso: {dias_mas_de_45}")
