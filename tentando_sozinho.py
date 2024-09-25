import os

def salvar_variaveis(caminho_doc, **kwargs): #funcao que puxa o caminho do documento e após o kwargs, que pode puxar quantas variaveis quiser
    with open(caminho_doc, "w") as c:  #"com o caminho aberto para escrever e caso nao exista cria ("w") nomeado como "c" "
        for chave, valor in kwargs.items(): # "para chave, valor em kwagr.items (funcao de .items = Retorna uma lista de pares (chave, valor) do dicionário, o que facilita a iteração sobre os argumentos nomeados.)"
            c.write(f"{chave}:{valor}\n") # usando o caminho dado como "c" iremos escrever as chaves e valores passados para o documento txt

salvar_variaveis("documentao.txt", nome = "joao", telefone = "123")


def carregar_variaveis(caminho_doc): # funcao que ira carregar /ler as variaveis para saber quais informaçoes estao contidas dentro do txt
    variaveis = {}
    with open(caminho_doc, "r") as c:
        for line in c:
            chave,valor = line.strip().split(": ")
            variaveis[chave] = valor
    return variaveis

