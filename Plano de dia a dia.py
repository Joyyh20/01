# Demonstração de operadores lógicos em condicionais

print("O que você vai fazer amanhã de manhã?")
print("Dormir/ Estudar/ Planejar")
manha = input()
print("O que você vai fazer amanhã a tarde?")
print("Jogar/ Treinar/ Trabalhar")
tarde = input()

if not manha or not tarde:
    print("Você precisa dizer oque vai fazer!")
else:
    if manha == "Dormir" or tarde == "Jogar":
        print("Você esta desperiçando o seu dia!")
    elif manha == "Estudar" or tarde == "Treinar":
        print("Que bom! Você irá se aperfeiçoar!")
    elif manha == "Planejar" and tarde == "Trabalhar":
        print("Para trabalhar melhor devo planejar!")
    else:
        print("Não combinamos estas ações...")

print("Tenha um bom dia!")