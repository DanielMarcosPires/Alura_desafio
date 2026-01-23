def definirTemperatura(value):
    temp = int(value)
    if temp < 25:
        print(f"Temperatura de {temp}°C foi definido")
    else:
        print("Alerta! Temperatura acima do limite permitido.")

temperatura = input("Digite a temperatura atual: ")

definirTemperatura(temperatura)