banda = input("Qual a melhor banda do mundo?")

if not banda == "rush" and not banda == "RUSH": #ou colocar tudo em ()      if not (banda == "rush" or banda == "RUSH"):
   print("Herege!")                             #e usar "or" entre eles
else:
    print("correto, é o RUSH")