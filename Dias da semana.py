#Dia da semana

print("Digite um dia da semana:")
dia = input()

match dia:
    case "segunda":
        print("Lave o cabelo")
    case "terça":
        print("Desça o lixo")
    case "quarta":
        print("Vá ao mercado")
    case "quinta":
        print("Arrume o armário")
    case "sexta":
        print("Faça cahorro quente")
    case "sabado":
        print("Vá na praça")
    case "domingo":
        print("Durma")

    case _:
        print("Jogue tft")
        
