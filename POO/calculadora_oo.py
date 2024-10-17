class Calculadora:
    def __init__(self) -> None:
        pass
    def soma(self,a,b):
        return a+b
    def diz_oi(self):
        print('oi')
        
obj_calculadora = Calculadora()

print(obj_calculadora.soma(5,5))

obj_calculadora.diz_oi