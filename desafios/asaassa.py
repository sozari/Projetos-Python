import time
print("5 : 0")
segundos = 59
minutos = 4
print(minutos,":", segundos )

while minutos >= 0:
   
    if segundos > -1:
        print(minutos,":", segundos )
        segundos -= 1
        time.sleep (0.1)
        if segundos == -1:
            segundos = 59
            minutos += -1
