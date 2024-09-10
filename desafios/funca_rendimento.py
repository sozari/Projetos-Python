deposito = int(input("Valor depositado: "))

def rendimento_deposito (valor_deposito):
    rendimento_total = valor_deposito + (valor_deposito * 0.007)
    return rendimento_total

total = rendimento_deposito(deposito)

print("O rendimento total foi de:" , total , "R$")