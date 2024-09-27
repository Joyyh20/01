#Conversor de temperaturas

grau = int(input("Digite a temperatura: "))
sistema = input("Celsius/ Kelvin/ Fahre?")

if sistema == "Celsius":
    #Criar as 2 fórmulas para converter em Kelvin e Fahre
    print("O valor em Celsius:", grau)
    print("A conversão para Kelvin:", Kelvin)
    print("A conversão para Fahre:", Fahre)
elif sistema == "Kelvin":
    #Criar as 2 fórmulas para converter em Celsius e Fahre
    print("O valor em Kelvin:", grau)
    print("A conversão para Celsius:", Celsius)
    print("A conversão para Fahre:", Fahre)
elif sistema == "Fahre":
    #Criar as 2 fórmulas para converter em Celsius e Kelvin
    print("O valor em Fahre:", grau)
    print("A conversão para Celsius:",Fahre)
    print("A conversão para Kelvin:",Kelvin)
else:
    print("Sitema inexistente")
