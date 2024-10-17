class Veiculo:
    def __init__(self,nome_vei,cor_vei,valor_vei,cambio_vei,ano_vei):
        self.nome = nome_vei
        self.cor = cor_vei
        self.valor = valor_vei
        self.cambio = cambio_vei
        self.ano = ano_vei

    def __str__(self):
        return (f"Nome: {self.nome}\nCor: {self.cor}\nValor: R${self.valor}\nCambio:: {self.cambio}\nAno: {self.ano}\n")

bongao = Veiculo('Kia Bongo','Azul','74.900','Manual','2007/2008')
        
print(bongao)