livros = [
    
    {"titulo": "Vozes do vento",
     "autor": "Rafael Costa",
     "ano": 2020,
     "favorito": 0},
     
    {"titulo": "O ultimo verao",
     "autor": "Ana Silva",
     "ano": 2001,
     "favorito": 0},
     
    {"titulo": "Sem fim",
     "autor": "Pedro Lima",
     "ano": 2005,
     "favorito": 0}

]

for livro in livros:
    if livro["titulo"] == "O ultimo verao":
        livro["favorito"] = 1
    print(f"Titulo:{livro["titulo"]} Autor:{livro["autor"]} Ano:{livro["ano"]} Favorito:{livro["favorito"]}")