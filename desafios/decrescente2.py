print("este é um programa que lê 3 números e imprime eles em ordem decrescente.")

primeiro = int(input("digite o primeiro número: "))
segundo = int(input("digite o segundo número: "))
terceiro = int(input("digite o terceiro número: "))

print(primeiro,"-",segundo,"-",terceiro)

if primeiro > segundo :
    aux = primeiro
    primeiro = segundo
    segundo = aux

if segundo > primeiro:
    aux = segundo
    segundo = primeiro
    primeiro = aux

if terceiro > segundo :
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro,"-",segundo,"-",terceiro)