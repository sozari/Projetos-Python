
condicao = True

while condicao:
    
    entrada = int(input("Digite um valor para ver a tabuada: "))
    print(entrada , "X" , "1" , entrada * 1)
    print(entrada , "X" , "2" , entrada * 2)
    print(entrada , "X" , "3" , entrada * 3)
    print(entrada , "X" , "4" , entrada * 4)
    print(entrada , "X" , "5" , entrada * 5)
    print(entrada , "X" , "6" , entrada * 6)
    print(entrada , "X" , "7" , entrada * 7)
    print(entrada , "X" , "8" , entrada * 8)
    print(entrada , "X" , "9" , entrada * 9)
    print(entrada , "X" , "10" , entrada * 10)
    
    opcao = input("1- para informar um novo numero / 2- para sair: ")


    if opcao == "1":
        print("continuando...")
    elif opcao == "2":
        print("voce saiu")
        condicao = False
    else:
        print("digito invalido")
