
# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x = Criar Arquivo
# r+ - Leitura + Escrita




opcao = ""

opcao = input("Digitar uma poesia [1] / sair do programa [2] / resetar arquivo [3]")

while opcao == "1":
    if opcao == "1":
        txt = input("Digite uma poesia: ")
        arquivo = open("aula13/novo_arquivo.txt","a")
        arquivo.write(f"\nfrase: {txt}")
        opcao = input("Digitar outra poesia [1] / sair do programa [2]")
        arquivo.close()
    

if opcao == "2":
    print("saindo...")
    
elif opcao == "3":
    arquivo = open("aula13/novo_arquivo.txt","w")
    arquivo.write("")
    arquivo.close()


