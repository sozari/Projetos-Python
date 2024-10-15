meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
itens = list(meu_dicionario.items())

for chave, valor in itens:
    if (chave, valor) == itens[-1]:
        print(f'Último item: {chave}: {valor}')
    else:
        print(f'Item: {chave}: {valor}')