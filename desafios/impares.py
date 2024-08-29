num = int(input("digite um para ver todos impares até ele: "))
inicial = 0

while inicial < num:
    inicial += 1
    if inicial % 2 == 1:
        print(inicial)
