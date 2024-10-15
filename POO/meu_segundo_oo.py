class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("O veículo está ligado.")

    def desligar(self):
        self.ligado = False
        print("O veículo está desligado.")

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

    def vericar_carro(self):
        print(f'marca do veiculo: {self.marca}')
        print(f'Modelo do veiculo: {self.modelo}')


marca_veiculo = input('Marca do veiculo: ')
modelo_veiculo = input('Modelo do veiuclo: ')

veiculo1 = Veiculo(marca_veiculo,modelo_veiculo)
veiculo1.vericar_carro()



class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print("Porta aberta.")
    def fechar_porta(self):
        print("Porta fechada.")


carro1 = Carro('Ferrari','Spider','Vermelho')
carro1.ligar()
carro1.vericar_carro()
