celsius = int(input("Digite uma temperatura em graus celsius para velo em fahrenheit: "))

def formula_fahrenheit(graus_celsius):
    f = (graus_celsius * 9/5) + 32
    return f

print(formula_fahrenheit(celsius))