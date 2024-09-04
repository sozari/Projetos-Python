lista = []
texto = ""
resposta = ""

print("GERADOR DE LISTAS")

while resposta != ("nao" or "NAO" or "não" or "NÃO"):
    
    texto = input("Digite algo: ")
    lista.append(texto)
    
    resposta = input("Deseja continuar adcionando a lista?")
    if resposta == "sim":
        print("Próxima palavra...")
    elif resposta == ("nao" or "NAO" or "não" or "NÃO"):
        print("Saindo...")



print(lista)


#while resposta != ("nao" or "NAO" or "não" or "NÃO" or "sim" or "SIM"):

