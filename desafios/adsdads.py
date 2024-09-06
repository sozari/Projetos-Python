user_list = []
while True:

    option = int(input("\n1-Adicionar Novo usuário \n2-mostrar contatos \n3-sair \nInforme uma opção: "))
    if option == 1:
        name, fone, email = (input("Adicionar novo usuário: \nNome: "),input("Telefone:"),input("E-mail"),)
        new_user = (name, fone, email)
        user_list.append(new_user)
        print("\nAdicionando...\n")
        print(new_user, "Adicionado!")

    elif option == 2 and not user_list:
        print("\nNenhum usuário cadastrado. Adicione um usuário primeiro.")
    elif option == 2 and user_list:
        print(f"\nLista de contatos: {user_list}")

    elif option == 3:
        print("\nSaindo...")
        break
    else:
        print("\nInforme uma opção válida")