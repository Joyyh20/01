#pedr,papel e tesoura 
jogador1 = input("Jogador 1:")
jogador2 = input("Jogaodr 2:")

if jogador1 == jogador2:
    print("O resultado deu empate")
elif jogador1 == "tesoura" and jogador2 == "papel":
    print("Jogaodr 1 venceu")
elif jogador1 == "papel" and jogador2 == "pedra":
    print("Jogador 1 venceu")
elif jogador1 == "pedra" and jogador2 == "tesoura":
    print("Jogador 1 venceu")
else:
    print("Jogaodr 2 venceu")