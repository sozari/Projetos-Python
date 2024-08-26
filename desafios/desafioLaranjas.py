qnt_laranjas_pedro = 10

print("Pedro tem " , qnt_laranjas_pedro , "laranjas")

laranjas_retiradas = int(input("Quantas laranjas você quer de Pedro? "))

qnt_laranjas_pedro = qnt_laranjas_pedro - laranjas_retiradas #ou qnt_laranjas_pedro -= laranjas_retiradas 

if qnt_laranjas_pedro > 5:
    print("Pedro ficou com" , qnt_laranjas_pedro , "ele está feliz!")
elif qnt_laranjas_pedro <= 5:
    print("Pedro ficou com" , qnt_laranjas_pedro , "ele está triste!") 


#==