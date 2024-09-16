loop = 1
lista = []

while loop < 10+1:
    num = int(input(f"Digite {loop}o numero:"))
    loop += 1

    lista.append(num) 

print(lista)

lista.reverse()
print(lista)