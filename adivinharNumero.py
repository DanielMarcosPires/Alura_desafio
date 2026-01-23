import random

def jogo(listaDeNumeros ,adivinhe):
    lance = input(f"Advinha um número entre {listaDeNumeros[0]} e {listaDeNumeros[-1]}:\n> ")
    
    lance = int(lance)

    if lance == adivinhe:
        print(f"Acertou! {lance} e {adivinhe}")
        return True 
    elif lance > adivinhe:
        print(f"Muito alto! Tente novamente: {lance}")
        listaDeNumeros[:] = [x for x in listaDeNumeros if x < lance]
    else:
        print(f"Muito baixo! Tente novamente: {lance}")
        listaDeNumeros[:] = [x for x in listaDeNumeros if x > lance]
    


listaDeNumeros = list(range(1, 101))
adivinhe = random.choice(listaDeNumeros)
print(adivinhe)
while True:
    if jogo(listaDeNumeros, adivinhe ):break
