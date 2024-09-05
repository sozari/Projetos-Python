a = ["apple," , "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)  
print(a)
#faz com que uma lista fique dentro da outra (b) dentro de (a)

for item in b:
    a.append(item)
#faz com que cada item da lista entre um por um formando
#uma lista única

print(a)    