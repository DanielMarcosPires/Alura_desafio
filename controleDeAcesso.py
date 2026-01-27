from datetime import datetime

horarioAtual = datetime.now()
hora_formatada = horarioAtual.strftime("%H:%M")

if "8:00"> hora_formatada and hora_formatada < "18:00":
    print("Acesso Liberado!")
else:
    print("Acesso Negado.")

print(hora_formatada)