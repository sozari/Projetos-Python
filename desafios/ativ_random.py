import random

random_numero = random.randint(1,100)
guess = None #para reservar variavel e nao confundir programadores se usa None
attempts = 0

while guess != random_numero:
    guess = int(input("\nAdivinhe o numero entre 1 e 100: "))
    attempts += 1

    print("tentativa numero:" , attempts ) 

    if guess > random_numero:
        print("\ntente com um numero menor.")
    elif guess < random_numero:
        print("\ntente com um numero maior.")


print("Parabens! Voce adivinhou o numero em" , attempts , "tentativas.")