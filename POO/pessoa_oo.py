class Pessoa:
    nome = ""
    idade = ""

    #podemos criar métodos que modificam os valores da classe.
    def set_nome(self,n):
        self.nome = n

    def set_idade(self,i):
        self.idade = i

    def get_nome(self):
        return (f"o seu nome é {self.nome}\n")
    
    def get_idade(self):
        return (f"a sua idade é {self.idade}\n")
    
    joao = Pessoa()
    

joao = Pessoa()

joao.set_nome("João")
joao.set_idade('23')

print(joao.nome)
print(joao.idade)