meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

for i, (chave, valor) in enumerate(meu_dicionario.items()):
    if i == len(meu_dicionario) - 1:
        print(f'Último item: {chave}: {valor}')
    else:
        print(f'Item: {chave}: {valor}')