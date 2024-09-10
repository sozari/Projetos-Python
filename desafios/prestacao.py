compra = int(input("Descubra o valor de sua compra com 5 prestações sem juros!"))

def prestacao (valor_compra):
    valor_total = valor_compra / 5
    return valor_total

prestacao_final = prestacao(compra)

print(f"valor da compra em 5 prestaçoes ficou em: {prestacao_final} R$")