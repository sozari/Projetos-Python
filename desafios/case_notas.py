n1 = float(input("digite a 1a nota: "))
n2 = float(input("Digite a 2a nota: "))

media = (n1 + n2) / 2

print(f"Média final:{media}")

match media:
    case x if x >= 0 or x <= 4:
        print("reprovado")
    case x if x <=7 or x > 4:
        print("Exame")
    case x if x <= 7.1 or x <=10:
        print("Aprovado")