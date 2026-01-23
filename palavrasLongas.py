from collections import Counter
import re

def maiorPalavra(x):
    if len(x)<10:
        return False
    else:
        return True
        
def identificar_palavras(entrada):
    regex = re.findall(r"(\w+)",entrada)
    return list(filter(maiorPalavra,regex))

texto = input("Digite um texto: \n> ")

resultado=identificar_palavras(texto)

for index,element in enumerate(resultado):
    print(f"{index} - {element} c({len(element)})")
