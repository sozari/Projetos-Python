passaros = ["arara", "papagaio", "canário", "beija-flor", "joao-de-barro"]
            
passaros.pop(-1) #Deleta um indice e o seu valor
print(passaros)

passaros.append("rolinha") #Adiciona esse valor no final da lista
print(passaros)

passaros.insert(0,"angrybird_vermelho") #Insere esse valor no indice zero, 
print(passaros)                         #deslocando o valor anterior para direita

passaros.remove("papagaio") #Remove buscando o valor
print(passaros)

passaros.sort() #Ordena a lista em ordem crescente

passaros.reverse() #Inverte a ordem dos elementos

print(len(passaros)) #Retorna o tamanho da lista

passaros[0] = "" #Atribui um valor ao indice zero (0) ou substitui o anterior