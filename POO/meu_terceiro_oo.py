class Aluno:
    def __init__(self,idade_p):
        self.idade = idade_p

    def idade_pessoa(self,):
        print(f'sua idade: {self.idade}')

    #self acessa o atributo da classe

aluno1 = Aluno(2)

aluno1.idade_pessoa()