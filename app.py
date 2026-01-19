
def calculo_da_gorjeta(x,y):
    conta = x
    gorjeta = y

    return conta * gorjeta/100

def total_a_pagar(conta_cliente,gorjeta):
    conta = float(conta_cliente)
    gorjeta = float(gorjeta)
    
    valor_da_gorjeta = calculo_da_gorjeta(conta,gorjeta)
    total = valor_da_gorjeta + conta

    print(f"\nValor da gorjeta: {valor_da_gorjeta}")
    return total

def validate_input(prompt):
    value = input(prompt)
    
    if not value.isdigit():
     print("*"*10+"\nO valor não deve conter letras símbolos e espaços, portanto serão removidos!\n"+"*"*10)

    return "".join(filter(str.isdigit, value)) or "0"

try:
    conta_cliente = validate_input("Digite o valor da conta: ")
    gorjeta = validate_input("Digite a porcentagem da gorjeta: ")

    total_a_pagar = total_a_pagar(conta_cliente,gorjeta)
    print(f"total a pagar: {total_a_pagar}")

except NameError:
    print(NameError)