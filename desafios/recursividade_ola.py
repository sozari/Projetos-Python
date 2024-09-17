txt = ""  

def ola_infinito(texto):
    texto = input("digite a 'pare' para sair: ")
    
    if texto == "":
        print("OI")
        ola_infinito(texto)
    elif texto == "pare":
        print("finalizando..")
        return
    
print(ola_infinito(txt))