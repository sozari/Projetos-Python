# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x = Criar Arquivo
# r+ - Leitura + Escrita



arquivo = open("aula13/espacamento.txt","r")
linha = arquivo.readline()
while linha:
    linhavazia = linha.strip()
    print(linhavazia)
    linha = arquivo.readline()
    arquivo.close



