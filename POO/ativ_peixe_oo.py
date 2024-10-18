class Peixe:
    def __init__(self,especie,tipo_de_agua,profundidade_encontrada):
        self.especie = especie
        self.tipo_peixe = tipo_de_agua
        self.profundidade = profundidade_encontrada

        

peixe1 = Peixe('Nemo','Salgada','600')
peixe2 = Peixe('Dory','Salgada','750')
peixe3 = Peixe('Peixe palhaço','Salgada','900')
peixe4= Peixe('Peixe espada','Salgada','1000')
peixe5 = Peixe('Tubarão','Salgada','1500')

lista_peixes = [peixe1,peixe2,peixe3,peixe4,peixe5]


for peixe in lista_peixes:
    print(f'Espécie: {peixe.especie}, Tipo de peixe: {peixe.tipo_peixe}, Profundidade encontrada: {peixe.profundidade}metros')