class Passageiro:

    def __init__(self,nome_p,numero_bag,destino_p,numero_pas,valor_pas):
        self.nome = nome_p
        self.numero_bagaem = numero_bag
        self.destino = destino_p
        self.numero_passagem = numero_pas
        self.valor_passagem = valor_pas

    def __repr__(self):
        return f"Nome: {self.nome}\nNúmero da bagagem: {self.numero_bagaem}\nDestino: {self.destino}\nNúmero da passagem: {self.numero_passagem}\nValor da passagem: R${self.valor_passagem}\n"


passageiro1 = Passageiro('João Souza','5456','Suíça','59785','2600')
passageiro2 = Passageiro('Ana Clara','5123','Belém','42365','1900')
passageiro3 = Passageiro('Claudia Elias','8953','Alemanha','89562','3500')



lista_passageiros = [passageiro1,passageiro2,passageiro3]

#print(lista_passageiros)

for passageiros in lista_passageiros:
    print(f"Nome do passageiro: {passageiros.nome}, Destino: {passageiros.destino}")