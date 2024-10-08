# lista = [10, 20, 30, 40, 50] 
# lista.append('kaue')
# print('1',lista)
# nome = lista.pop()#remove o ultimo item da lista
# print('2',lista)
# lista.append(1234)
# print('3',lista)
# del lista[-1]#apaga um indice
# print('4',lista)

# lista.insert(0,5)# adiciona um valor no indice escolhido
# print('5',lista)

# lista.clear()#limpa toda a lista
# print(lista)

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)#Isso nao existe  
# lista_a.extend(lista_b)
# print(lista_a)

lista = ['Santos', 'Kaue', 'Henrique']
lista.append('Messi')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice ])
    
    


   