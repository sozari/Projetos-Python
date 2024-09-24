


def primeira_pergunta_nome():
    print("Seja bem vindo pela primeira vez ao nosso programa!")
    nome = input("qual seu nome?")
    print(f"Seja bem vindo {nome}")
    return nome


nome1 = primeira_pergunta_nome()

print(nome1)

if nome1 == "":
    primeira_pergunta_nome()
else:
    nome_ja_adicionado()


def nome_ja_adicionado(nome1):
    print(f"boas vindas {nome1} é bom te ter aqui de novo")



# Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(arquivo, **kwargs):
    with open(arquivo, 'w') as f:
        for nome, valor in kwargs.items():
            f.write(f"{nome}: {valor}\n")
    

# Carregar variáveis de um arquivo
def carregar_variaveis(arquivo):
    variaveis = {}
    with open(arquivo, 'r') as f:
        for line in f:
            nome, valor = line.strip().split(': ')
            variaveis[nome] = valor
    return variaveis


# Salvar as variáveis em um arquivo chamado "variaveis.txt"
salvar_variaveis('variaveis.txt', nome=nome, idade=idade, cidade=cidade)

# Carregar as variáveis de volta do arquivo
variaveis_carregadas = carregar_variaveis('variaveis.txt')