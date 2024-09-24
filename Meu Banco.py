# Demonstracao de uso de diferentes operadores 

print("Qual e o saldo atual da sua conta bancaria?")
print("obs.: utilize ponto para representar os centavos...")
saldo = float(input())


if saldo < 0:
    print("Putz! Voce esta devendo ao banco!")
elif saldo == 0:
    print("Impossivel! Deve ter alguns centavos...")
elif saldo < 1:
    print("Putz! So miseros centavinhos na conta ?")
elif saldo <= 9:
    print("Opa! Ja da para comprar umas balinhas...")
elif saldo >= 1000000:
    print("Eita voce tem mais de um milhao!")

if saldo != 0:
    print("Ao menos, voce esta movimentando a conta...")