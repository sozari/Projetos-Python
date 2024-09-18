import random

porta = "fechada"

vida = 10

gema = 5


count = 0

while count <= 1*5 and vida > 0:

    opcao = input("digite uma opção: 1 - continuar 2 - sair - 3 para exibir status: ")

    if opcao == "1":
        print("opção 1...")
        aleatorio = random.randint(1,10)

        if aleatorio%2==0:
            gema +=1

            if gema >=10:
                vida +=1
                gema = 0

        else:
            vida -=1

    elif opcao =="2":

        print("opção 2...")
        print("você saiu")
        break

    elif opcao =="3":
        print("opção 3...")
        print("vida: ",vida,"gemas: ",gema)

    else:
        print("digito inválido")
   
    if vida <= 0:
        print("você morreu.")
        break

    if count >=5:
        print("porta abriu")
        porta = "aberta"

    count +=1


