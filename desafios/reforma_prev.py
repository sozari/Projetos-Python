
def calculo_beneficio():

    sexo = input("Qual seu sexo? [M] masculino / [F] feminino: ")
    idade = int(input("Qual idade voce começou a contribuir com a previdencia"))

    if sexo == "M" or sexo == "m":
        idade_masc = 65 - idade
        trabalho = 40 + idade
        print("Genero masculino")
        print(f"idade: {idade_masc} anos")
        if idade_masc == 40:
            print('com essa idade você terá direito a 100'+"%"+' do beneficio')
        elif idade_masc == 35:
            print('com essa idade você terá direito a 87,5'+"%"+' do beneficio')    
        elif idade_masc == 30:
            print('com essa idade você terá direito a 77,5'+"%"+' do beneficio')  
        elif idade_masc == 25:
            print('com essa idade você terá direito a 70'+"%"+' do beneficio')  
        
    elif sexo == "F" or sexo == "f":
        idade_femi = 62 - idade
        trabalho = 40 + idade
        print("Genero feminino")
        print(f"idade: {idade_masc} anos")
        if idade_femi == 40:
            print('com essa idade você terá direito a 100'+"%"+' do beneficio')
        elif idade_femi == 35:
            print('com essa idade você terá direito a 87,5'+"%"+' do beneficio')    
        elif idade_femi == 30:
            print('com essa idade você terá direito a 77,5'+"%"+' do beneficio')  
        elif idade_femi == 25:
            print('com essa idade você terá direito a 70'+"%"+' do beneficio')  

    print(f"Voce terá que trbalhar até os {trabalho} anos para ter direito a 100% do beneficio")

calculo_beneficio()