def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}= {valor}")

minha_funcao(nome="Alice", idade=30, cidade="Porto Alegre")


def minha_outra_funcao(nome,idade):
    print(f"nome: {nome}, idade: {idade}")

minha_outra_funcao("joao", 23)