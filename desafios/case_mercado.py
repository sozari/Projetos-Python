codigo = int(input("Coloque o código do produto: "))

match codigo:
    case 1:
        print("Alimento não-perecivel")
    case 2 | 3 | 4:
        print("Alimento perecível")
    case 5 |6:
        print("Vestuário")
    case 7:
        print("Higiene pessoal")
    case x if x >= 8 and x <= 15:
        print("Limpeza e utensilios domesticos")
    case _:
        print("Código inválido!")