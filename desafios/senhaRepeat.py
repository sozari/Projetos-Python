senha = "2024"
condicao = True
count = 0

while count <=2  and condicao:
     
    entrada = input("Digite sua senha: ")

    if entrada != senha:
       
        count = count +1
        if count <=2:
            print("Tente novamente")
            print("você tem 3 tentativas, esta é sua tentativa numero:" , count)
        else:
            print("esta foi sua terceira tentativa!")
            print("cartao bloqueado")
    elif entrada == senha:
        print("Seu saldo na conta é 50 centavos")
        condicao = False
        
print("programa finalizado")