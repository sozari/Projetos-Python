#abrindo um arquivo para escrita
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("olá, mundo\n")
    arquivo.write("Este é um exemplo do uso de with")


with open("exemplo.txt", "r" , encoding="utf-8") as f:
    print(f.read())


#O arquivo é automaticamente fechado após o bloco with