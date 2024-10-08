lista = []
for numero in range(10):
    lista.append(numero)
    
lista = [
    numero *2
    for numero in range(10)
]

# print(list(range(10)))
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # aumentar valores dos produtos em 5%
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if(produto['preco'] >= 20 and produto['preco'] * 1.5)
]
# print(*novos_produtos, sep='\n')

# lista = [n for n in range(10)if n < 5] filtro
# print(lista)


