contatos = []
condicao = True
opcao = int(input("mostre na tela 1 - adicionar novo contato 2- mostrar contatos 3 - sair."))

while condicao:
    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")

        novo_contato = (nome, telefone, email)

        contatos.append(novo_contato)

        opcao = int(input("1 - adicionar novo contato 2- mostrar contatos 3 - sair."))

    elif opcao == 2:
        print(contatos)
        break
    elif opcao == 3:
        print("finalizando...")
        break
  



