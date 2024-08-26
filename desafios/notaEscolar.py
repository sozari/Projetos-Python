n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
n3 = float(input("Digite sua terceira nota:"))

media = (n1 + n2 + n3) /3


if media < 6.0:
    print("Você ficou com média" , media , "no trimestre, NOTA F")
elif media >= 6 and media <= 7:
    print("Você ficou com média" , media , "no trimestre, NOTA D")
elif media > 7 and media <= 8:
    print("Você ficou com média" , media , "no trimestre, NOTA C")
elif media > 8 and media <= 9:
    print("Você ficou com média" , media , "no trimestre, NOTA B")
elif media > 9 and media <= 10:
    print("Você ficou com média" , media , "no trimestre, NOTA A")
else:
    print("Você digitou valores errados!")