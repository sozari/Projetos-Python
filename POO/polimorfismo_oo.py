class Shark():
    def swim(self):
        print('O tubarão está nadando.')

    def swim_backward(self):
        print('O tubarão não consegue nadar para trás, mas pode afundar para trás.')

    def skeleton(self):
        print('O esqueleto do tubarão é feito de cartilagem')


class Clownfish(Shark):
    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print('O peixe-alhaço está nadando.')
    
    def swim_backward(self):
        print('O peixe-palhaço pode nadar para trás.')

    def skeleton(self):
        print('O esqueleto do peixe-palhaço é deito de osso')


#sobrescrita de métodos

peixe_palhaco = Clownfish()

peixe_palhaco.swim_backward()