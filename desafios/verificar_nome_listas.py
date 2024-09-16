lista_nomes = []

for x in range(0,4):
    nome = input("Digite um nome: ")

    lista_nomes.append(nome)

print(lista_nomes)

nome = input("Digite um nome que deseja buscar: ")
if nome in lista_nomes:
    print(f"O nome {nome} ja está cadastrado")
elif nome not in lista_nomes:
    print(f"O nome {nome} não está cadastrado")
