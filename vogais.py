from collections import Counter
import re
def leitor_de_vogais(entrada):
    lista = []
    regex = re.findall(r"[aeiouAEIOUáéíóúÁÉÍÓÚâêôÂÊÔãõÃÕ]",entrada.lower())
    print(f"Quantidade de cada vogal {dict(Counter(regex))}")
    print(f"Quantidade total de vogais: {len(regex)}")


texto = input("Digite um texto:\n > ")
qnt_vogais=leitor_de_vogais(texto)