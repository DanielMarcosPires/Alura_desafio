import random

def jogada_CPU():
    hand = ("pedra","papel","tesoura")
    decisao = random.choice(hand)
    
    return decisao

def jogada_jogador(escolha):
    hand = ("pedra","papel", "tesoura")
    decisao = hand.index(escolha)

    return hand[decisao]

def resultado(cpu,jogador):
    print(f"CPU: {cpu}")
    print(f"Jogador: {jogador}")
    if jogador == cpu:
        print("O Jogo empatou!")
    elif (
        (jogador =="pedra" and cpu == "tesoura") or 
        (jogador == "papel" and cpu == "pedra") or
        (jogador == "tesoura" and cpu == "papel") 
    ):
        print("Você venceu!")
    else:print("Você perdeu!")


escolha = input("Escolha: pedra,papel ou tesoura?\n> ")

jogada_do_jogador = jogada_jogador(escolha)
jogada_do_cpu = jogada_CPU()
resultado(jogada_do_cpu,jogada_do_jogador)