import os

def carregar_usuarios():
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as u:
           
            for line in u :
                chave,valor = line.strip().split(" | ")
                print(f'{chave} | {valor} ')


carregar_usuarios()