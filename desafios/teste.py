verNotas = input("você quer ver suas notas?")


if verNotas == "sim" or verNotas == "SIM" or verNotas == "s" or verNotas == "S":
    
    n1 = float(input("Digite sua primeira nota:"))
    n2 = float(input("Digite sua segunda nota:"))
    n3 = float(input("Digite sua terceira nota:"))

    media = (n1 + n2 + n3) /3


    if media >= 0.0 and media < 6.0:
        print("Você ficou com média" , media , "no trimestre, NOTA F")
    elif media >= 6.0 and media <= 7.0:
        print("Você ficou com média" , media , "no trimestre, NOTA D")
    elif media > 7.0 and media <= 8.0:
        print("Você ficou com média" , media , "no trimestre, NOTA C")
    elif media > 8.0 and media <= 9.0:
        print("Você ficou com média" , media , "no trimestre, NOTA B")
    elif media > 9.0 and media <= 10.0:
        print("Você ficou com média" , media , "no trimestre, NOTA A")
    else:
        print("Você digitou valores errados!")
else:
    print("até outro dia")