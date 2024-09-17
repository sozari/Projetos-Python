lista = ["joao","ana","artur","gabi"]

def add_lista(nome):
    global lista
    lista.append(nome)
    print(lista)

nome = input("Digite um nome para adicionar na lista: ")
add_lista(nome)