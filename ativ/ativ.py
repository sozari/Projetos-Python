import os

# Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
        for chave, valor in kwargs.items():
            f.write(f"{chave}: {valor}\n")

# Carregar variáveis de um arquivo
def carregar_variaveis(path_file):
    variaveis = {}
    with open(path_file, 'r') as f:
        for line in f:
            chave, valor = line.strip().split(': ')
            variaveis[chave] = valor
    return variaveis


def verificar_primeira_vez():
    match os.path.exists("ativ/a.txt"):
        case True:
            variaveis_carregadas = carregar_variaveis('ativ/a.txt') 
   
            if len(variaveis_carregadas) > 0:
                print(f"seja bem vindo novamente {variaveis_carregadas["nome"]}")
            else:
                nome_v = input("por favor digite seu nome: ")
                tel_v = input("por favor digite seu telefone: ")
                email_v = input("por favor digite seu email: ")

                salvar_variaveis('ativ/a.txt',nome = nome_v, telefone = tel_v, email= email_v)
        case False:
                nome_v =  input("por favor digite seu nome")
                tel_v = input("por favor digite seu telefone: ")
                email_v = input("por favor digite seu email: ")


                salvar_variaveis('ativ/a.txt', nome = nome_v, telefone = tel_v, email= email_v)
   
verificar_primeira_vez()