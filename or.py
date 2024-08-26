print("1. idoso")
print("2. gestante")
print("4. cadeirante")
print("4. nenhum destes")
resposta=int(input("voce é:"))

if (resposta == 1) or (resposta == 2) or (resposta == 3):
    print("você tem direito a fila prioritária")
else:
    print("você não tem direito a nada. vá para fila e fique quieto")