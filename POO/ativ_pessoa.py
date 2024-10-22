class Pessoa:
    def __init__(self,nome,hora_trabalho,altura):
        self.nome = nome
        self.hora_trabalho = hora_trabalho
        self.altura = altura

    def dados(self):
        return (f'Nome do individuo: {self.nome}\nHora de trabalho: {self.hora_trabalho}\naltura: {self.altura}m.')

    


nome1 = Pessoa('artur','9:15 até 17:00','1,70')
# nome1.seu_nome()