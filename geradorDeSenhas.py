import random
import string

def gerarSenha():
    caracteres = string.ascii_letters+string.octdigits+string.punctuation
    letra = random.choices(caracteres,k=12)

    return "".join(letra)


while True:
    entrada = input("Aperte Enter para gerar a Senha, digite 'sair' para parar \n")
    senha = gerarSenha()

    if entrada == "sair":break

    print(f"Senha gerada: {senha}\n")


