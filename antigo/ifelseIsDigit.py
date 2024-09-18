print("Este é um programa que verifica se um número é maior que o outro.")
numero1 = input("digite o primeiro número: ")
numero2 = input("digite o segundo número: ")

if numero1.isdigit() and numero2.isdigit():
    if numero1 > numero2:
        print("O número" , numero1 , "é maior que o número" , numero2)
    elif numero1 == numero2:
        print("O número" , numero1 , "é igual que o número" , numero2)
    elif numero1 < numero2:
        print("O número" , numero1 , "é menor que o número" , numero2)
else:
    print("você digitou uma letra")