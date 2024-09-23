#Match case

print("Digite um número referente ao estado da moeda:")
print("a. Flor de cunho")
print("b. Soberba")
print("c. Muito bem conservada")
print("d. Bem conservado")
print("e. Outros estados")

Estado = input()

match Estado:
    case ("a"):
        print("Perfeita! Vou pagar R$ 1.000.000,00")
    case ("b"):
        print("Quase perfeita! Ofereço R$ 250.000,00")
    case ("c"):
        print("Que ótimo! Posso dar uns R$ 100.000,00")
    case ("d"):
        print("Que bom. Aceitaria R$ 30.000,00?")
    case ("e") :
        print("Desculpe. Não aceito nesse estado.")
    case _:
        print("Opção não reconhecida!")
        
