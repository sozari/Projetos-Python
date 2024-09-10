carros = [
    {"marca": "toyota", "modelo": "corolla", "ano": 2022, "cor": "prata", "preco": 25000},
    {"marca": "honda", "modelo": "civic", "ano": 2021, "cor": "preto", "preco": 28000},
    {"marca": "ford", "modelo": "mustang", "ano": 2020, "cor": "vermelho", "preco": 45000},
    {"marca": "chevrolet", "modelo": "camaro", "ano": 2021, "cor": "azul", "preco": 50000},
    {"marca": "tesla", "modelo": "model s", "ano": 2023, "cor": "branco", "preco": 60000},     
]

for carro in carros:
    if carro["marca"] == "ford":
        print(f"Marca:{carro["marca"]} Modelo:{carro["modelo"]} Ano:{carro["ano"]} Cor:{carro["cor"]} Preço:{carro["preco"]}")