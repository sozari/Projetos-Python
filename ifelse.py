print("Este é um programa que verifica se um número é maior que o outro.")
numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o segundo número: "))

if numero1 > numero2:
    print("O número" , numero1 , "é maior que o número" , numero2)
elif numero1 == numero2:
    print("O número" , numero1 , "é igual que o número" , numero2)
elif numero1 < numero2:
    print("O número" , numero1 , "é menor que o número" , numero2)