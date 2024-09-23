#Filme ou série


print("Digite o nome de um filme ou série:")
input()

print("Qual seria sua nota pra avaliar o filme ou série:")
print("1.")
print("2.")
print("3.")
print("4.")
print("5.")

nota = int(input())

match nota:
      case 1:
          print("Péssimo")
          print("Oque não lhe agradou?:")
          input()
      case 2:
          print("Ruim")
          print("Oque não lhe agradou?")
          input()
      case 3:
          print("Razoável")
      case 4:
          print("Bom")
      case 5:
          print("Ótimo")
      case _:
          print("Coloca algo lógico aí")
