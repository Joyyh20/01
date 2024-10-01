

jogadores = []
numeros = []

for x in range(0,11):
    nome = input("Digite o nome do jogador:")
    jogadores.append(nome)
    camisa = input("Digite o número da camisa:")
    numeros.append(camisa)
print("Lista de jogadores cadastrados:")
for y in range(0,11):
    print(f"{numeros[y]}. {jogadores[y]}")


troca = input("Você quer fazer substituição(S/N)?")
if troca == "S":
    for x in range(0,3):
        nome = input("Digie o nome do jogador substituído:")
        camisa = input("Digite o seu respectivo número:")
        jogadores.remove(nome)
        numeros.remove(camisa)
        nome = input("Digite o nome do jogador substituído:")
        camisa = input("Digite o seu respectivo número:")
        jogadores.remove(nome)
        numeros.remove(camisa)
    print("Lista dos jogadores atualizada:")
    for y in range(0,11):
        print(f"{numeros[y]}. {jogadores[y]}")