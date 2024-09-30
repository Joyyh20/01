#Demonstração de acesso a listas

print("Vou montar a marmita com 5 alimentos!")
marmito = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa recomendação", marmito)

resposta = input("Quer montar um marmito diferente (s/n)?")
if resposta == "s":
    for x in range(len(marmito)):
        print(f"Digite o {x+1} item do cardápio:")
        marmito[x] = input()
    print("A marmito montada foi:", marmito)
    print("Os três primeiros itens foram:", marmito[0:3])
    print("O último item do marmito foi:", marmito[-1])
else:
    print("Ok, você decide....")
