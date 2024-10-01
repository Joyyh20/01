#Solução da atividade

GABARITO = ["B", "C", "A", "E", "D"]
RESPOSTA = ["","","","",""]
ACERTOS = 0

for x in range(len(GABARITO)):
    print(f"Digite a resposta {x+1}:")
    RESPOSTA[x] = input() 
    if GABARITO[x] == RESPOSTA[x]:
        print("Boa")
        ACERTOS = ACERTOS + 1
    else:
        print("Errou")

print("Total de acertos:", ACERTOS)   