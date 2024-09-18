#open("caminho,""r")

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x = Criar Arquivo
# r+ - Leitura + Escrita

arquivo = open("aula13/teste.txt","r")

print(arquivo.readable()) #retorna true ou false para saber se conseguimos ler o arquivo.

lista = arquivo.readlines() #readlines transforma as linhas do arquivo em uma lista

print(lista)

arquivo.close()