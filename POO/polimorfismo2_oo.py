class Principal():
    def funcaoAntesDepois(self):
        print('ANTES DA MUDANÇA')

class Secundaria(Principal):
    def __init__(self) -> None:
        super().__init__()

    def funcaoAntesDepois(self):
        print('DEPOIS DA MUDANÇA')

antesDepois = Secundaria()
antesDepois.funcaoAntesDepois()