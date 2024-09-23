string = "cheve1 : valor1 , chave2: valor , chave3: valor3 "

#Divide a string em pares de chave-valor
pares = [item.strip() for item in string.split(",")]#list compression

#divide cada par pelo dois pontos e remove espaços em branco
lista = [tuple(par.strip().split(": ")) for par in pares]

#print(pares)
print(lista)