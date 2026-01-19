import re

def leitor_de_vogais(entrada):
    regex = re.findall(r"[aeiouAEIOUáéíóúÁÉÍÓÚâêôÂÊÔãõÃÕ]",entrada)

    

    return regex

texto = input("Escreva um texto:\n> ")
vogais = leitor_de_vogais(texto)
qnt_vogais = len(vogais)

print(f"{texto}\n")
print(f"Todos os vogais:\n{vogais}")
print(f"Quantidade de vogais: {qnt_vogais}")