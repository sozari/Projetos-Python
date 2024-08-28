
condicao = True
count= 0

while condicao:
    count = 0
    entrada = int(input("Digite um valor para ver a tabuada: "))
    
    while count <= 10:
        print(entrada , "X" , count , entrada * count)
        count = count + 1
 
    
    opcao = input("1- para informar um novo numero / 2- para sair: ")


    if opcao == "1":
        print("continuando...")
    elif opcao == "2":
        print("voce saiu")
        condicao = False
    else:
        print("digito invalido")
