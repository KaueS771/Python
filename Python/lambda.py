# lista = [4,32,1,34,5,6,6,21]
# lista.sort(reverse=True)#Ordena a lista

# ensinando python a orderna por nome na dict
lista = [
    {'nome': 'Kaue', 'sobrenome': 'Henrique'},
    {'nome': 'Jesus', 'sobrenome': 'Cristo'},
    {'nome': 'Lionel', 'sobrenome': 'Messi'},
    {'nome': 'Neymar', 'sobrenome': 'Jr'},
    
    
]
# def orderna(item):
    
#     return item['nome']
def exibir(lista):
    for item in lista:
        print(item)
    print()
    


# lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista,  key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)   