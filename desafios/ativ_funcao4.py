nome = input("Digite seu nome:")
salario_fixo = int(input("Digite seu salário fixo: "))
total_vendas = int(input("Digite quanto você fez em vendas (em dinheiro): "))
comissao = 15

def salario_e_comissao (salario,vendas,comissao):
    salario_total = salario + ((vendas * comissao) / 100)
    return salario_total

salario_final = salario_e_comissao(salario_fixo,total_vendas,comissao)

print("Nome do trabalhador:" , nome)
print("o salá fixo do trabalhador é:" , salario_fixo)
print("o salário mais comissao do trabalhor é:" , salario_final)

