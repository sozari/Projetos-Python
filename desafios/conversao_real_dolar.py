real = int(input("Digite quantos reais voce quer converter para dolar"))

def real_para_dolar(pilas):
    dolar = pilas / 5
    return dolar

preco_dolar = real_para_dolar(real)

print(real, "R$ convertido para dolar fica:", preco_dolar , "$")
