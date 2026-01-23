import re
def calculo_IMC(peso, altura):
    x = float(peso)
    y = float(altura)
    valor = x/(y ** 2)
    return valor

def input_number(prompt):
    data = input(prompt)
    validate = re.match("(\d+.\d+)|\d+",data)
    if validate:
        return validate.string
    else:
        print("Valor incorreto: Deve inserir números! ")


print("(IMC) - Índice de Massa Corporal")

peso = input_number("Digite seu peso (kg): ")
altura = input_number("Digite sua altura (m): ")

imc = calculo_IMC(peso,altura)

if imc < 18.5:
    print(f"Você está abaixo do peso. {imc}")
elif 18.5 <= imc < 25:
    print(f"Peso normal. {imc}")
else:
    print(f"Você está acima do peso.")