lista = [1,2,3,4,5,6,7,8,9,10]

def retirar_itens():
    global lista
    print(lista)
  
    if len(lista) >0:
        lista.pop(-1)#caso nao tenha (-1) ele automaticamente ira tirar o ultimo
        retirar_itens()
    else:
        print("Lista está vazia")
        return
    
retirar_itens()