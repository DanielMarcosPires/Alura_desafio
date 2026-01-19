import re


def cpf_input(prompt):
    print("Digite o seu CPF de 11 dígitos: 00000000000")
    value = input(prompt)

    if len(value) == 11:
        return value
    else:
        return f"CPF Inválido: {value} - O CPF deve ter exatamente 11 dígitos"    


def cpf_print(value):
    cpf_formatado = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})',r'\1.\2.\3-\4',value)

    print(cpf_formatado)


print("*"*12)
cpf = cpf_input("> ")

cpf_print(cpf)
print("*"*12)