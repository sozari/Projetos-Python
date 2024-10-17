class Animal:
    def __init__(self,qnt_patas,som_emitido,especie):
        self.patas = qnt_patas
        self.som = som_emitido
        self.espec = especie

    
class Cachorro(Animal):
    def __init__(self, qnt_patas, som_emitido, especie,cor_pelo,nome,raca):
        super().__init__(qnt_patas, som_emitido, especie)
        self.cor = cor_pelo
        self.nome = nome
        self.raca = raca

    def __str__(self):
        return (f"Quantidade de patas:{self.nome} \nsom emitido:{self.som} \nespécie:{self.espec} \nCor do pelo:{self.cor} \nNome:{self.nome} \nRaça:{self.raca} \n")

dogao = Cachorro('4 patas','late alto','cachorro','marrom','Bobson','vira lata')
dog = Cachorro('3 patas','late baixo','cachorro','azul','george','York')

print(dogao)
print(dog)
