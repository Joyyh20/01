#Posição em campo

print("Digite a função do jogador:")
função = input()

if função == "goleiro" or função == "zagueiro" or função == "lateral":
    print("Sua função é de defensor")
elif função == "volante" or função == "meia" or função == "ala":
    print("Sua função é Meio-Campo")
elif função == "ponta" or função == "atacante" or função == "centroavante":
    print("Sua função é de Ataque")
else:
    print("Teimoso")