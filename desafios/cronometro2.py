import time

minutos = int(input("Quantos minutos deseja esperar? "))

min = minutos * 60

for x in range(min):
    print(min)
    min -= 1
    time.sleep(1)
