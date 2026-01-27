import re

def controleDeGasto(valor):
    valor = int(valor)
    limite = 3000
    return valor <= limite

valorStr = input("Digite o total de despesas do mês (R$) \n> ")

if controleDeGasto(valorStr):
    valorInt = int(valorStr)
    print(f"Seu valor de R${valorInt:,.2f} do mês está dentro do limite!")
else:
    print("Atenção! Você utrapassou o limite do orçamento")
