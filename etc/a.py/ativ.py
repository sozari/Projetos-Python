joao = {"nome":"joao","idade":15}
maria = {"nome":"maria","idade":20}
pedro = {"nome":"pedro","idade":27}
def salvar_usuario(path_file, dicionario:dict):
    with open(path_file, 'a') as f:
        for chave, valor in dicionario.items():
            f.write(f"{chave}: {valor}\n")


salvar_usuario("usuarios.txt",joao)

salvar_usuario("usuarios.txt",maria)

salvar_usuario("usuarios.txt",pedro)


print(joao)
nome_joao = joao[0].split("")[1]
print(nome_joao)

for indice, joao in enumerate( joao):
    print(f'Nome: {indice}, idade: {joao}')