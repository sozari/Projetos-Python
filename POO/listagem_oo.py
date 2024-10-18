class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome='{self.nome},idade={self.idade})"
    
pessoa = Pessoa("Alice",30)
print(repr(pessoa))
print(pessoa)