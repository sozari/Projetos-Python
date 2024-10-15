class Aluno:
    def __init__(self,idade,nome_p):
        self.nome = nome_p
        self.idade = idade

    def verifica_idade(self):
        if self.idade >= 18:
            print("O aluno é maior de idade.")
        else:
            print("O aluno é menor de idade.")

    def verifica_nome(self):
        print(f"nome: {self.nome}")

aluno1 = Aluno(20,"joao")
aluno1.verifica_idade()
aluno1.verifica_nome()


# self representa o atributo da classe