class Computador:
    def __init__(self,cpu,qntd_memoria):
        self.cpu = cpu
        self.qntd_memoria = qntd_memoria
        self.ligado = False
        
    def desligar(self):
        self.desligado = False
        print('Desligado')

    def ligar(self):
        self.ligado = True
        print('Ligado')

class Pc_game(Computador):
    def __init__(self, cpu, qntd_memoria):
        super().__init__(cpu, qntd_memoria)
        self.jogando = False
        #self.iniciar_jogo = iniciar_jogo    
        self.jogo_iniciado = False

    def nao_jogando_jogo(self):
        self.jogando = False

    def jogando_jogo(self):
        self.jogando = True

    def jogo_fechar(self):
        self.jogo_iniciado = False
        self.jogando = False

    def jogo_iniciar(self):
        self.jogo_iniciado = True
        self.jogando = True


    def __repr__(self):
        return (f'CPU: {self.cpu}\nQuantidade de memória: {self.qntd_memoria}\n'
                f'Ligado: {self.ligado}\nJogando: {self.jogando}\n'
                f'Jogo iniciado: {self.jogo_iniciado}\n')



pc_meia_boca = Pc_game('i5','18ram')

pc_meia_boca.ligar()
pc_meia_boca.jogo_iniciar() 
print(repr(pc_meia_boca))


pc_meia_boca.jogo_fechar()
print(repr(pc_meia_boca))








    #cpu(str),qntd_memoria(int),ligado(bool)
    # jogando(bool) e o método iniciar_jogo() e o método fechar_jogo().
