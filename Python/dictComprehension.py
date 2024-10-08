produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

print(produto.items())


for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

s1 = {i for i in range(10)}
print(s1)
print(dc)