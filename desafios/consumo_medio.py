
def consumo_medio (distancia,combustivel):
    return distancia / combustivel

distancia = float(input("digite a distancia percorrida pelo automovel em km:"))
combustivel = float(input("digite a combustivel total em litros:"))

consumo_medio_f = consumo_medio(distancia,combustivel)

print("a media de km por litros para fazer esta viagem foi de: %.2f"%(consumo_medio_f))
