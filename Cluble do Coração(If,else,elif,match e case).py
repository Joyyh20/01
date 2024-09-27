#Principais clubes do Brasil

estado = input(("Rio, São Paulo e Minas (RJ/SP/MG)?"))

match estado:
    case"RJ":
        clube = input(("Flamengo, Fluminense, Vasco ou Botafogo?"))
        if clube == "Flamego":
            print() 