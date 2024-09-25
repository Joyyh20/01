#Programa com três valores

x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y:"))
z = int(input("Digite o valor de z:"))

if x < y and y < z:
    print("Em ordem crescente!")
elif x > y and y > z:
    print("Em ordem decrescente!")
else:
    print("Todos misturados!")