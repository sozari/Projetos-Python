meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
itens = list(meu_dicionario.items())

for i in range(len(itens)):
    chave, valor = itens[i]
    if i == len(itens) - 1:
        print(f'Último item: {chave}: {valor}')
    else:
        print(f'Item: {chave}: {valor}')
