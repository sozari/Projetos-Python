
def tabela_festa():
    executar_main = True
    bebida = 0
    comida = 0
    transporte = 0
    com_amigos = 0



    print("--Programa farra com os amigos--")

    print("Digite [1] para SIM e [2] para NAO")
    num = int(input("Deseja beber?"))
    if num == 1:
        print("Voce planeja beber")
        bebida += 80
    elif num == 2:
        print("Voce nao planeja beber")
    else:
        print("voce digitou um numero invalido")
        return


    num = int(input("Deseja comer?"))
    if num == 1 and executar_main:
        print("Voce planeja comer")
        comida += 60
    elif num == 2:
        print("Voce nao planeja comer")
    else:
        print("voce digitou um numero invalido")
        return


    num = int(input("Deseja gastar com transporte?"))
    if num == 1:
        print("Voce planeja gastar com transporte")
        transporte += 15
    elif num == 2:
        print("Voce nao planeja gastar com transporte")
    else:
        print("voce digitou um numero invalido")
        executar_main = False
        if not executar_main:
            return

    amigos = int(input("Quantos amigos voce deseja levar?"))
    if amigos >= 0:
        com_amigos = (bebida + comida + transporte) * (1 + amigos)
    else:
        print("valor negativo invalido")
        return


    print(f"O total estimado para a noite é: {com_amigos} reais.")

tabela_festa()

