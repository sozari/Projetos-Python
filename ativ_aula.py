import os
from def_carrega_usu import carregar_usuarios

joao = {"nome":"joao","idade":15}
maria = {"nome":"maria","idade":20}
pedro = {"nome":"pedro","idade":27}

def salvar_usuario(path_file, dicionario:dict):
    if os.path.exists(path_file):
        with open(path_file, 'a') as f:

            for i, (chave, valor) in enumerate(dicionario.items()):
                if i == len(dicionario) - 1:
                    f.write(f'{chave}: {valor}\n')
                else:
                    f.write(f'{chave}: {valor} | ')
    else:    
        with open(path_file, 'w') as f:
            for i, (chave, valor) in enumerate(dicionario.items()):
                if i == len(dicionario) - 1:
                    f.write(f'{chave}: {valor}\n')
                else:
                    f.write(f'{chave}: {valor} |')



salvar_usuario("usuarios.txt",joao)

salvar_usuario("usuarios.txt",maria)

salvar_usuario("usuarios.txt",pedro)

carregar_usuarios()



