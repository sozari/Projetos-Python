class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}"

lista_pessoas = []

# Exemplo de adição dinânima
nomes = ["Alice", "Bob", "Carlos"]
idades = [30,25,40]

for nome,idade in zip(nomes, idades):
    lista_pessoas.append(Pessoa(nome, idade))

    # Exibindo a lista de pessoas
print(lista_pessoas)