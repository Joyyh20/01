#Aluno aprovado ou reprovado

n1 = float(input("1a. nota:"))
n2 = float(input("2a. nota:"))
n3 = float(input("3a. nota:"))
n4 = float(input("4a. nota:"))


media = (n1+n2+n3+n4)/4


if media >= 6:
    print("Estudante aprovado")
else:
    print("Esudante reprovado")

print("A media dele é:", media)    
