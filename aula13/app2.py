import os

#open("caminho,""r")

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x = Criar Arquivo
# r+ - Leitura + Escrita


arquivo = open("aula13/novo_arquivo.txt","x")

arquivo.close

##########################################

os.remove("aula13/teste.txt")

##########################################

if os.path.exists("aula13/novo_arquivo.txt"):
    os.remove("aula13/novo_arquivo.txt")
else:
    print("arquivo nao existe")