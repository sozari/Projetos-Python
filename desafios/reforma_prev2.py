def calculo_beneficio_case():

    print("\n=_Programa feito para voce entender melhor a previdencia_=\n")

    sexo = input("Qual seu sexo? [M] masculino / [F] feminino: ")
    idade_contrib = int(input("Qual idade voce começou a contribuir com a previdencia? "))
    

    if sexo == "M" or sexo == "m":
        idade_masc = 65 - idade_contrib #calculo idade minima
        contribuicao = 40 + idade_contrib
       
        print("Genero masculino")
        print(f"tempo de contribuiçao ate hoje: {idade_masc} anos")
        if idade_masc >= 40:
            print('com essa idade você terá direito a 100'+"%"+' do beneficio')
        elif idade_masc >= 35:
            print('com essa idade você terá direito a 87,5'+"%"+' do beneficio')    
        elif idade_masc >= 30:
            print('com essa idade você terá direito a 77,5'+"%"+' do beneficio')  
        elif idade_masc >= 25:
            print('com essa idade você terá direito a 70'+"%"+' do beneficio')
        elif idade_masc <=24:
            print("Voce ainda nao atingiu o minimo de tempo de contribuição")    
        

    elif sexo == "F" or sexo == "f":
        idade_femi = 62 - idade_contrib
        contribuicao = 40 + idade_contrib
        
        print("Genero feminino")
        print(f"tempo de contribuiçao ate hoje: {idade_femi} anos")
        if idade_femi >= 40:
            print('com esse tempo de contribuição você terá direito a 100'+"%"+' do beneficio')
        elif idade_femi >= 35:
            print('com esse tempo de contribuição você terá direito a 87,5'+"%"+' do beneficio')    
        elif idade_femi >= 30:
            print('com esse tempo de contribuição você terá direito a 77,5'+"%"+' do beneficio')  
        elif idade_femi >= 25:
            print('com esse tempo de contribuição você terá direito a 70'+"%"+' do beneficio')
        elif idade_femi <=24:
            print("Voce ainda nao atingiu o minimo de tempo de contribuição")  
            #return
        
    
    print(f"Voce terá que trbalhar até os {contribuicao} anos para ter direito a 100% do beneficio")
    

calculo_beneficio_case()
