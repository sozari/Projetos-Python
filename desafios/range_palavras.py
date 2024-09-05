lista = []
tamanho = int(input("Qual o tamanho da lista que deseja preencher?"))
txt = ""

for tamanho in range(0,tamanho):
    txt = input("Digite algo:")
    lista.append(txt)

    print(lista) 
    
print("Você finalizou a lista!")
    