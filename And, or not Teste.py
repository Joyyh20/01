#Teset And or Not

print("Digite um time:")
time = input()
print("Digite a posição do time na tabela")
posição = int(input())


if posição == 1:
    print("Campeão")
elif posição > 1 and posição <= 6:
    print("Libertadores!")
elif posição > 7 and posição <= 12:
    print("Sul-Americana")
elif posição >= 17:
    print("Rebaixado")
else:
    print("Não sei dizer")
    