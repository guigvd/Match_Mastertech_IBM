def indexador(objeto, indice):
    return objeto[indice]

try:
    print(indexador('Python', 10))
except IndexError:
    print('Index errado :/')