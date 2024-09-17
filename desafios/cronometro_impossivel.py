import time

minutos = int(input("Quantos minutos deseja esperar? "))

min_estatico = minutos -1

min = minutos * 60

    
for x in range(min):
    if min <0:
        min_estatico-1
    elif min > 60:
        min_estatico+1 
    print(f"{min_estatico}:{min}")
    min -= 1
    time.sleep(0.1)

print(min_estatico)